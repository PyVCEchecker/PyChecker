from robomotion.node import Node


def node_decorator(*args, **kwargs):
    def wrapper(cls):
        class NewCls(cls):
            def __init__(self):
                self.cls = cls
                self.name = ''
                self.title = ''
                self.color = ''
                self.continueOnError=False
                self.icon = ''
                self.editor = None
                self.inputs = 1
                self.outputs = 1

            def __getattribute__(self, s):
                if s in kwargs:
                    return kwargs[s]

                return super().__getattribute__(s)

        return NewCls
    return wrapper
