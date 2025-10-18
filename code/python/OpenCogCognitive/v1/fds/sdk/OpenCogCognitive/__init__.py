"""
OpenCog Cognitive Architecture SDK for Python

This package provides cognitive AI capabilities based on OpenCog architecture.
"""

__version__ = "0.1.0"

from fds.sdk.OpenCogCognitive.atomspace import AtomSpace, Atom, Node, Link
from fds.sdk.OpenCogCognitive.nodes import ConceptNode, PredicateNode, VariableNode
from fds.sdk.OpenCogCognitive.links import ListLink, InheritanceLink, EvaluationLink
from fds.sdk.OpenCogCognitive.reasoner import CognitiveReasoner, ReasoningConfig
from fds.sdk.OpenCogCognitive.pattern_matcher import PatternMatcher, Pattern
from fds.sdk.OpenCogCognitive.mind_agent import MindAgent, CogServer
from fds.sdk.OpenCogCognitive.configuration import Configuration

__all__ = [
    'AtomSpace',
    'Atom',
    'Node',
    'Link',
    'ConceptNode',
    'PredicateNode',
    'VariableNode',
    'ListLink',
    'InheritanceLink',
    'EvaluationLink',
    'CognitiveReasoner',
    'ReasoningConfig',
    'PatternMatcher',
    'Pattern',
    'MindAgent',
    'CogServer',
    'Configuration',
]
