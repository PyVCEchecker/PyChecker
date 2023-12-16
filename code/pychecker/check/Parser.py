import abc
import ast as ast39
from typed_ast import ast27


class Parser(metaclass=abc.ABCMeta):
    def __init__(self, ast, next_parser=None):
        self.next_parser = next_parser
        self._ast = ast

    def parse_modules(self, code: str)->set[str]:
        try:
            root_node = self._ast.parse(code)
        except SyntaxError:
            if self.next_parser is None:
                return set()
            return self.next_parser.parse_modules(code)
        else:
            modules = set()
            modules = self._parse_body(root_node.body, modules)
            return modules

    def parse_modules_only_top(self, code: str) -> set[str]:
        try:
            root_node = self._ast.parse(code)
        except SyntaxError:
            if self.next_parser is None:
                return set()
            return self.next_parser.parse_modules(code)
        else:
            modules = set()
            for node in root_node.body:
                if isinstance(node, self._ast.Import):
                    modules = modules.union(self._parse_import_node(node))
                elif isinstance(node, self._ast.ImportFrom):
                    modules = modules.union(self._parse_importfrom_node(node))
            return modules

    def _parse_body(self, body, modules: set)->set[str]:
        for node in body:
            if isinstance(node, self._ast.Import):
                modules = modules.union(self._parse_import_node(node))
            if isinstance(node, self._ast.ImportFrom):
                modules = modules.union(self._parse_importfrom_node(node))
            if self._has_body(node):
                node_body = node.body
                modules = self._parse_body(node_body, modules)
                if isinstance(node, self._ast.If):
                    node_body = node.orelse
                    modules = self._parse_body(node_body, modules)
        return modules

    def _has_body(self, node)->bool:
        types = [self._ast.ClassDef, self._ast.FunctionDef, self._ast.If, self._ast.For, self._ast.While]
        try:
            self._ast.__getattribute__("Try")
        except AttributeError:
            types.append(self._ast.TryExcept)
        else:
            types.append(self._ast.Try)
        for tp in types:
            if isinstance(node, tp):
                return True
        return False

    @staticmethod
    @abc.abstractmethod
    def _parse_import_node(node)->set[str]:
        pass

    @staticmethod
    @abc.abstractmethod
    def _parse_importfrom_node(node)->set[str]:
        pass


class TopLevelParser(Parser):
    @staticmethod
    def _parse_import_node(node)->set[str]:
        top_levels = set()
        stmts = node.names
        for stmt in stmts:
            top_levels.add(stmt.name.split('.')[0])
        return top_levels

    @staticmethod
    def _parse_importfrom_node(node)->set[str]:
        module = node.module
        if node.level != 0:
            return set()  # relative import
        if module:
            top_level = module.split('.')[0]
            return {top_level, }
        else:
            return set()


class SecondLevelParser(Parser):
    @staticmethod
    def _parse_import_node(node)->set[str]:
        second_levels = set()
        stmts = node.names
        for stmt in stmts:
            parts = stmt.name.split('.')
            if len(parts) < 2:
                continue
            second_level = "{}.{}".format(parts[0], parts[1])
            second_levels.add(second_level)
        return second_levels

    @staticmethod
    def _parse_importfrom_node(node)->set[str]:
        second_levels = set()
        if node.level != 0:
            return set()  # relative import
        module = node.module
        stmts = ["{}.{}".format(module, n.name) for n in node.names]
        for stmt in stmts:
            parts = stmt.split('.')
            if len(parts) < 2:
                continue
            second_level = "{}.{}".format(parts[0], parts[1])
            second_levels.add(second_level)
        return second_levels


class ParserFactory:
    @staticmethod
    def make_parser(parser_type)->Parser:
        if parser_type == "top_level":
            parser = TopLevelParser(ast39, next_parser=TopLevelParser(ast27))
            return parser
        elif parser_type == "second_level":
            parser = SecondLevelParser(ast39, next_parser=SecondLevelParser(ast27))
            return parser
        return None

