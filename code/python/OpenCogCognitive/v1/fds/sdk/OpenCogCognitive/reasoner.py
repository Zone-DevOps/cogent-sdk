"""
Cognitive Reasoner - Performs reasoning over the AtomSpace

Supports multiple reasoning paradigms including probabilistic logic
and pattern-based inference.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from fds.sdk.OpenCogCognitive.atomspace import AtomSpace, Atom, Link
from fds.sdk.OpenCogCognitive.nodes import ConceptNode, PredicateNode
from fds.sdk.OpenCogCognitive.links import InheritanceLink, ImplicationLink


@dataclass
class ReasoningConfig:
    """Configuration for the cognitive reasoner"""
    reasoning_mode: str = "probabilistic"  # "probabilistic", "logical", "evolutionary"
    confidence_threshold: float = 0.7
    max_iterations: int = 1000
    learning_rate: float = 0.01
    attention_allocation: bool = True


@dataclass
class ReasoningResult:
    """Result of a reasoning operation"""
    statement: str
    confidence: float
    supporting_evidence: List[Atom]
    reasoning_chain: List[str]


class CognitiveReasoner:
    """
    Performs cognitive reasoning over knowledge in the AtomSpace.
    
    Supports multiple reasoning paradigms:
    - Probabilistic Logic Networks (PLN)
    - Logical inference
    - Pattern-based reasoning
    - Evolutionary learning
    """
    
    def __init__(self, atomspace: AtomSpace, config: Optional[ReasoningConfig] = None):
        self.atomspace = atomspace
        self.config = config or ReasoningConfig()
        self.reasoning_history: List[ReasoningResult] = []
    
    def infer(self, premises: List[str], query: str) -> ReasoningResult:
        """
        Perform inference from premises to answer a query.
        
        Args:
            premises: List of premise statements
            query: Query to answer
            
        Returns:
            ReasoningResult with conclusion and confidence
        """
        # Simple rule-based reasoning for demonstration
        confidence = 0.8
        
        # Check if query can be directly answered from premises
        for premise in premises:
            if query.lower() in premise.lower():
                confidence = 0.95
                break
        
        # Apply transitivity rules
        if self.config.reasoning_mode == "probabilistic":
            confidence = self._apply_probabilistic_reasoning(premises, query)
        elif self.config.reasoning_mode == "logical":
            confidence = self._apply_logical_reasoning(premises, query)
        
        result = ReasoningResult(
            statement=query,
            confidence=confidence,
            supporting_evidence=[],
            reasoning_chain=premises
        )
        
        self.reasoning_history.append(result)
        return result
    
    def _apply_probabilistic_reasoning(self, premises: List[str], query: str) -> float:
        """Apply probabilistic logic network reasoning"""
        # Simplified PLN reasoning
        base_confidence = 0.7
        
        # Increase confidence based on number of supporting premises
        confidence_boost = min(0.2, len(premises) * 0.05)
        
        return min(0.99, base_confidence + confidence_boost)
    
    def _apply_logical_reasoning(self, premises: List[str], query: str) -> float:
        """Apply logical inference"""
        # Simplified logical reasoning
        # In a full implementation, this would use first-order logic
        
        if any(query.lower() in premise.lower() for premise in premises):
            return 0.95
        
        return 0.6
    
    def apply_inference_rule(self, rule_name: str, *atoms: Atom) -> Optional[Atom]:
        """
        Apply a specific inference rule to atoms.
        
        Args:
            rule_name: Name of the inference rule
            atoms: Input atoms for the rule
            
        Returns:
            Inferred atom or None
        """
        if rule_name == "inheritance_transitivity":
            return self._inheritance_transitivity(*atoms)
        elif rule_name == "modus_ponens":
            return self._modus_ponens(*atoms)
        
        return None
    
    def _inheritance_transitivity(self, *atoms: Atom) -> Optional[Atom]:
        """
        Apply inheritance transitivity: If A inherits B and B inherits C, then A inherits C.
        """
        if len(atoms) >= 2:
            # Look for inheritance chain
            inheritance_links = [a for a in atoms if isinstance(a, InheritanceLink)]
            
            if len(inheritance_links) >= 2:
                # Create new inheritance link
                link1, link2 = inheritance_links[0], inheritance_links[1]
                
                if link1.outgoing[1] == link2.outgoing[0]:
                    new_link = InheritanceLink(link1.outgoing[0], link2.outgoing[1])
                    return self.atomspace.add_link(new_link)
        
        return None
    
    def _modus_ponens(self, *atoms: Atom) -> Optional[Atom]:
        """
        Apply modus ponens: If A and (A implies B), then B.
        """
        # Simplified implementation
        if len(atoms) >= 2:
            for atom in atoms:
                if isinstance(atom, ImplicationLink):
                    antecedent = atom.outgoing[0]
                    consequent = atom.outgoing[1]
                    
                    # Check if antecedent is present
                    if antecedent in atoms:
                        return consequent
        
        return None
    
    def get_reasoning_history(self) -> List[ReasoningResult]:
        """Get the history of reasoning operations"""
        return self.reasoning_history
    
    def clear_history(self):
        """Clear the reasoning history"""
        self.reasoning_history.clear()
