"""
AtomSpace - Core knowledge representation system

The AtomSpace is a hypergraph database that stores knowledge as atoms.
"""

from typing import List, Dict, Optional, Set, Any
import uuid
from datetime import datetime


class Atom:
    """Base class for all atoms (nodes and links)"""
    
    def __init__(self, name: str, atom_type: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.type = atom_type
        self.truth_value = TruthValue(1.0, 1.0)  # strength, confidence
        self.attention_value = AttentionValue(0.5)  # importance
        self.created_at = datetime.now()
        
    def __repr__(self):
        return f"{self.type}({self.name})"
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        return isinstance(other, Atom) and self.id == other.id


class Node(Atom):
    """A node in the AtomSpace (represents a concept or entity)"""
    
    def __init__(self, name: str, node_type: str = "Node"):
        super().__init__(name, node_type)


class Link(Atom):
    """A link in the AtomSpace (represents a relationship)"""
    
    def __init__(self, outgoing: List[Atom], link_type: str = "Link"):
        name = f"{link_type}({', '.join(str(a) for a in outgoing)})"
        super().__init__(name, link_type)
        self.outgoing = outgoing
    
    def get_outgoing(self) -> List[Atom]:
        """Get the atoms this link connects"""
        return self.outgoing


class TruthValue:
    """Probabilistic truth value (strength and confidence)"""
    
    def __init__(self, strength: float, confidence: float):
        self.strength = max(0.0, min(1.0, strength))
        self.confidence = max(0.0, min(1.0, confidence))
    
    def __repr__(self):
        return f"TV({self.strength:.3f}, {self.confidence:.3f})"


class AttentionValue:
    """Attention value for importance-based processing"""
    
    def __init__(self, sti: float, lti: float = 0.0, vlti: float = 0.0):
        self.sti = sti  # Short-term importance
        self.lti = lti  # Long-term importance
        self.vlti = vlti  # Very long-term importance
    
    def __repr__(self):
        return f"AV(sti={self.sti:.3f}, lti={self.lti:.3f})"


class AtomSpace:
    """
    The AtomSpace is a hypergraph database for knowledge representation.
    
    It stores atoms (nodes and links) and provides operations for querying
    and manipulating the knowledge graph.
    """
    
    def __init__(self):
        self.atoms: Dict[str, Atom] = {}
        self.atoms_by_type: Dict[str, Set[str]] = {}
        self.atoms_by_name: Dict[str, Set[str]] = {}
        self.incoming_set: Dict[str, Set[str]] = {}  # Maps atom ID to links containing it
        
    def add_node(self, node: Node) -> Node:
        """Add a node to the AtomSpace"""
        if node.id not in self.atoms:
            self.atoms[node.id] = node
            
            if node.type not in self.atoms_by_type:
                self.atoms_by_type[node.type] = set()
            self.atoms_by_type[node.type].add(node.id)
            
            if node.name not in self.atoms_by_name:
                self.atoms_by_name[node.name] = set()
            self.atoms_by_name[node.name].add(node.id)
        
        return node
    
    def add_link(self, link: Link) -> Link:
        """Add a link to the AtomSpace"""
        if link.id not in self.atoms:
            self.atoms[link.id] = link
            
            if link.type not in self.atoms_by_type:
                self.atoms_by_type[link.type] = set()
            self.atoms_by_type[link.type].add(link.id)
            
            # Update incoming sets
            for atom in link.outgoing:
                if atom.id not in self.incoming_set:
                    self.incoming_set[atom.id] = set()
                self.incoming_set[atom.id].add(link.id)
        
        return link
    
    def get_atom(self, atom_id: str) -> Optional[Atom]:
        """Get an atom by its ID"""
        return self.atoms.get(atom_id)
    
    def get_atoms_by_type(self, atom_type: type) -> List[Atom]:
        """Get all atoms of a specific type"""
        type_name = atom_type.__name__ if hasattr(atom_type, '__name__') else str(atom_type)
        atom_ids = self.atoms_by_type.get(type_name, set())
        return [self.atoms[aid] for aid in atom_ids]
    
    def get_atoms_by_name(self, name: str) -> List[Atom]:
        """Get all atoms with a specific name"""
        atom_ids = self.atoms_by_name.get(name, set())
        return [self.atoms[aid] for aid in atom_ids]
    
    def get_incoming_set(self, atom: Atom) -> List[Link]:
        """Get all links that contain this atom"""
        link_ids = self.incoming_set.get(atom.id, set())
        return [self.atoms[lid] for lid in link_ids]
    
    def remove_atom(self, atom: Atom) -> bool:
        """Remove an atom from the AtomSpace"""
        if atom.id in self.atoms:
            # Remove from main dictionary
            del self.atoms[atom.id]
            
            # Remove from type index
            if atom.type in self.atoms_by_type:
                self.atoms_by_type[atom.type].discard(atom.id)
            
            # Remove from name index
            if atom.name in self.atoms_by_name:
                self.atoms_by_name[atom.name].discard(atom.id)
            
            # Remove from incoming sets
            if atom.id in self.incoming_set:
                del self.incoming_set[atom.id]
            
            return True
        return False
    
    def get_all_atoms(self) -> List[Atom]:
        """Get all atoms in the AtomSpace"""
        return list(self.atoms.values())
    
    def size(self) -> int:
        """Get the number of atoms in the AtomSpace"""
        return len(self.atoms)
    
    def clear(self):
        """Clear all atoms from the AtomSpace"""
        self.atoms.clear()
        self.atoms_by_type.clear()
        self.atoms_by_name.clear()
        self.incoming_set.clear()
    
    def __repr__(self):
        return f"AtomSpace(atoms={self.size()})"
