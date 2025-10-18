"""
Node types for the AtomSpace

Nodes represent concepts, entities, and variables.
"""

from fds.sdk.OpenCogCognitive.atomspace import Node


class ConceptNode(Node):
    """Represents a concept or category"""
    
    def __init__(self, name: str):
        super().__init__(name, "ConceptNode")


class PredicateNode(Node):
    """Represents a predicate or relation"""
    
    def __init__(self, name: str):
        super().__init__(name, "PredicateNode")


class VariableNode(Node):
    """Represents a variable for pattern matching"""
    
    def __init__(self, name: str):
        if not name.startswith("$"):
            name = f"${name}"
        super().__init__(name, "VariableNode")


class SchemaNode(Node):
    """Represents an executable schema or procedure"""
    
    def __init__(self, name: str):
        super().__init__(name, "SchemaNode")


class GroundedSchemaNode(Node):
    """Represents a grounded procedure (implemented in code)"""
    
    def __init__(self, name: str, procedure=None):
        super().__init__(name, "GroundedSchemaNode")
        self.procedure = procedure
    
    def execute(self, *args):
        """Execute the grounded procedure"""
        if self.procedure:
            return self.procedure(*args)
        return None


class AnchorNode(Node):
    """Represents an anchor point in the AtomSpace"""
    
    def __init__(self, name: str):
        super().__init__(name, "AnchorNode")


class WordNode(Node):
    """Represents a word in natural language"""
    
    def __init__(self, name: str):
        super().__init__(name, "WordNode")


class SentenceNode(Node):
    """Represents a sentence in natural language"""
    
    def __init__(self, name: str):
        super().__init__(name, "SentenceNode")
