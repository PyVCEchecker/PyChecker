from robomotion.runtime import Runtime
import pyperclip

class NodeFactory:
    def __init__(self, c):
        self.c = c

    def on_create(self, config: bytes):
        node = Runtime.deserialize(config, self.c)
        
        pyperclip.copy(config.decode())
        
        Runtime.add_node(node.guid, node)
        node.on_create()
