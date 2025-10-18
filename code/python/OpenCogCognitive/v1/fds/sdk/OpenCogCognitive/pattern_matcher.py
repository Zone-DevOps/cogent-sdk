"""
Pattern Matcher - Advanced pattern recognition in the AtomSpace

Supports variable binding and complex pattern matching.
"""

from typing import List, Dict, Optional, Any
from dataclasses import dataclass
from fds.sdk.OpenCogCognitive.atomspace import AtomSpace, Atom, Node, Link
from fds.sdk.OpenCogCognitive.nodes import VariableNode


@dataclass
class PatternMatch:
    """Represents a pattern match result"""
    bindings: Dict[str, Atom]
    matched_atoms: List[Atom]
    confidence: float = 1.0


class Pattern:
    """
    Represents a pattern for matching in the AtomSpace.
    
    Patterns can include variables that are bound during matching.
    """
    
    def __init__(self):
        self.variables: List[VariableNode] = []
        self.clauses: List[Any] = []
    
    def add_variable(self, var_name: str) -> VariableNode:
        """Add a variable to the pattern"""
        var = VariableNode(var_name)
        self.variables.append(var)
        return var
    
    def add_clause(self, clause: str):
        """Add a clause to the pattern"""
        self.clauses.append(clause)
    
    def __repr__(self):
        return f"Pattern(variables={len(self.variables)}, clauses={len(self.clauses)})"


class PatternMatcher:
    """
    Performs pattern matching in the AtomSpace.
    
    Supports:
    - Variable binding
    - Complex graph patterns
    - Constraint satisfaction
    - Partial matching
    """
    
    def __init__(self, atomspace: AtomSpace):
        self.atomspace = atomspace
        self.match_cache: Dict[str, List[PatternMatch]] = {}
    
    def match(self, pattern: Pattern) -> List[PatternMatch]:
        """
        Find all matches for the given pattern in the AtomSpace.
        
        Args:
            pattern: Pattern to match
            
        Returns:
            List of pattern matches with variable bindings
        """
        matches: List[PatternMatch] = []
        
        # Simple pattern matching implementation
        # In a full implementation, this would use sophisticated graph matching
        
        all_atoms = self.atomspace.get_all_atoms()
        
        for atom in all_atoms:
            if self._atom_matches_pattern(atom, pattern):
                bindings = self._extract_bindings(atom, pattern)
                match = PatternMatch(
                    bindings=bindings,
                    matched_atoms=[atom],
                    confidence=1.0
                )
                matches.append(match)
        
        return matches
    
    def _atom_matches_pattern(self, atom: Atom, pattern: Pattern) -> bool:
        """Check if an atom matches the pattern"""
        # Simplified matching logic
        for clause in pattern.clauses:
            clause_str = str(clause).lower()
            atom_str = str(atom).lower()
            
            # Simple string-based matching
            if any(part in atom_str for part in clause_str.split()):
                return True
        
        return False
    
    def _extract_bindings(self, atom: Atom, pattern: Pattern) -> Dict[str, Atom]:
        """Extract variable bindings from a matched atom"""
        bindings: Dict[str, Atom] = {}
        
        # Simplified binding extraction
        for var in pattern.variables:
            bindings[var.name] = atom
        
        return bindings
    
    def match_with_constraints(
        self, 
        pattern: Pattern, 
        constraints: Optional[Dict[str, Any]] = None
    ) -> List[PatternMatch]:
        """
        Match pattern with additional constraints.
        
        Args:
            pattern: Pattern to match
            constraints: Additional constraints (e.g., type, value ranges)
            
        Returns:
            List of pattern matches satisfying constraints
        """
        matches = self.match(pattern)
        
        if not constraints:
            return matches
        
        # Filter matches based on constraints
        filtered_matches = []
        for match in matches:
            if self._satisfies_constraints(match, constraints):
                filtered_matches.append(match)
        
        return filtered_matches
    
    def _satisfies_constraints(
        self, 
        match: PatternMatch, 
        constraints: Dict[str, Any]
    ) -> bool:
        """Check if a match satisfies the given constraints"""
        # Simplified constraint checking
        
        if "min_confidence" in constraints:
            if match.confidence < constraints["min_confidence"]:
                return False
        
        if "required_types" in constraints:
            required_types = constraints["required_types"]
            for atom in match.matched_atoms:
                if atom.type not in required_types:
                    return False
        
        return True
    
    def find_similar_patterns(
        self, 
        reference_atom: Atom, 
        similarity_threshold: float = 0.7
    ) -> List[Atom]:
        """
        Find atoms similar to the reference atom.
        
        Args:
            reference_atom: Reference atom to compare against
            similarity_threshold: Minimum similarity score (0-1)
            
        Returns:
            List of similar atoms
        """
        similar_atoms: List[Atom] = []
        
        all_atoms = self.atomspace.get_all_atoms()
        
        for atom in all_atoms:
            if atom.id != reference_atom.id:
                similarity = self._calculate_similarity(reference_atom, atom)
                
                if similarity >= similarity_threshold:
                    similar_atoms.append(atom)
        
        return similar_atoms
    
    def _calculate_similarity(self, atom1: Atom, atom2: Atom) -> float:
        """Calculate similarity between two atoms"""
        # Simplified similarity calculation
        
        # Type similarity
        type_match = 1.0 if atom1.type == atom2.type else 0.5
        
        # Name similarity (simple string matching)
        name1 = atom1.name.lower()
        name2 = atom2.name.lower()
        
        # Jaccard similarity on words
        words1 = set(name1.split())
        words2 = set(name2.split())
        
        if not words1 and not words2:
            name_match = 1.0
        elif not words1 or not words2:
            name_match = 0.0
        else:
            intersection = len(words1.intersection(words2))
            union = len(words1.union(words2))
            name_match = intersection / union if union > 0 else 0.0
        
        # Combined similarity
        return (type_match * 0.3 + name_match * 0.7)
    
    def clear_cache(self):
        """Clear the pattern matching cache"""
        self.match_cache.clear()
