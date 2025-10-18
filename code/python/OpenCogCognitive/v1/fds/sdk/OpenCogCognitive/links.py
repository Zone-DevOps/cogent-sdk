"""
Link types for the AtomSpace

Links represent relationships between atoms.
"""

from typing import List
from fds.sdk.OpenCogCognitive.atomspace import Link, Atom


class ListLink(Link):
    """Represents an ordered list of atoms"""
    
    def __init__(self, *atoms: Atom):
        super().__init__(list(atoms), "ListLink")


class InheritanceLink(Link):
    """Represents an inheritance relationship (A inherits from B)"""
    
    def __init__(self, child: Atom, parent: Atom):
        super().__init__([child, parent], "InheritanceLink")


class SimilarityLink(Link):
    """Represents a similarity relationship"""
    
    def __init__(self, atom1: Atom, atom2: Atom):
        super().__init__([atom1, atom2], "SimilarityLink")


class EvaluationLink(Link):
    """Represents the evaluation of a predicate on arguments"""
    
    def __init__(self, predicate: Atom, *args: Atom):
        if len(args) == 1 and isinstance(args[0], Link):
            super().__init__([predicate, args[0]], "EvaluationLink")
        else:
            from fds.sdk.OpenCogCognitive.links import ListLink
            arg_list = ListLink(*args)
            super().__init__([predicate, arg_list], "EvaluationLink")


class MemberLink(Link):
    """Represents set membership (A is a member of set B)"""
    
    def __init__(self, member: Atom, set_atom: Atom):
        super().__init__([member, set_atom], "MemberLink")


class SubsetLink(Link):
    """Represents subset relationship (A is a subset of B)"""
    
    def __init__(self, subset: Atom, superset: Atom):
        super().__init__([subset, superset], "SubsetLink")


class ImplicationLink(Link):
    """Represents logical implication (A implies B)"""
    
    def __init__(self, antecedent: Atom, consequent: Atom):
        super().__init__([antecedent, consequent], "ImplicationLink")


class AndLink(Link):
    """Represents logical AND"""
    
    def __init__(self, *atoms: Atom):
        super().__init__(list(atoms), "AndLink")


class OrLink(Link):
    """Represents logical OR"""
    
    def __init__(self, *atoms: Atom):
        super().__init__(list(atoms), "OrLink")


class NotLink(Link):
    """Represents logical NOT"""
    
    def __init__(self, atom: Atom):
        super().__init__([atom], "NotLink")


class ExecutionLink(Link):
    """Represents the execution of a schema with arguments"""
    
    def __init__(self, schema: Atom, *args: Atom):
        if len(args) == 1 and isinstance(args[0], Link):
            super().__init__([schema, args[0]], "ExecutionLink")
        else:
            from fds.sdk.OpenCogCognitive.links import ListLink
            arg_list = ListLink(*args)
            super().__init__([schema, arg_list], "ExecutionLink")


class ContextLink(Link):
    """Represents a context for other links"""
    
    def __init__(self, context: Atom, statement: Atom):
        super().__init__([context, statement], "ContextLink")
