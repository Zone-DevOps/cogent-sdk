# AtomSpace API

The AtomSpace is the core knowledge representation system in OpenCog Cognitive Architecture.

## Overview

The AtomSpace stores knowledge as a hypergraph where:
- **Nodes** represent concepts, entities, and values
- **Links** represent relationships between nodes
- **Truth Values** represent uncertainty and probability
- **Attention Values** represent importance for processing

## Usage

### Creating an AtomSpace

```python
from fds.sdk.OpenCogCognitive import AtomSpace

atomspace = AtomSpace()
```

### Adding Nodes

```python
from fds.sdk.OpenCogCognitive import ConceptNode, PredicateNode

# Create concept nodes
dog = atomspace.add_node(ConceptNode("Dog"))
animal = atomspace.add_node(ConceptNode("Animal"))
```

### Adding Links

```python
from fds.sdk.OpenCogCognitive import InheritanceLink

# Dog inherits from Animal
inheritance = atomspace.add_link(InheritanceLink(dog, animal))
```

### Querying the AtomSpace

```python
# Get all concept nodes
concepts = atomspace.get_atoms_by_type(ConceptNode)

# Get atoms by name
dog_atoms = atomspace.get_atoms_by_name("Dog")

# Get incoming links
incoming = atomspace.get_incoming_set(dog)
```

## API Reference

### AtomSpace Class

#### Methods

- `add_node(node: Node) -> Node`: Add a node to the AtomSpace
- `add_link(link: Link) -> Link`: Add a link to the AtomSpace
- `get_atom(atom_id: str) -> Optional[Atom]`: Get an atom by ID
- `get_atoms_by_type(atom_type: type) -> List[Atom]`: Get all atoms of a type
- `get_atoms_by_name(name: str) -> List[Atom]`: Get atoms by name
- `get_incoming_set(atom: Atom) -> List[Link]`: Get links containing an atom
- `remove_atom(atom: Atom) -> bool`: Remove an atom
- `get_all_atoms() -> List[Atom]`: Get all atoms
- `size() -> int`: Get number of atoms
- `clear()`: Clear all atoms

### Atom Class

#### Attributes

- `id`: Unique identifier
- `name`: Atom name
- `type`: Atom type
- `truth_value`: Probabilistic truth value
- `attention_value`: Importance for processing
- `created_at`: Creation timestamp

### Node Types

- `ConceptNode`: Represents a concept
- `PredicateNode`: Represents a predicate/relation
- `VariableNode`: Represents a variable
- `SchemaNode`: Represents an executable schema
- `WordNode`: Represents a word
- `SentenceNode`: Represents a sentence

### Link Types

- `ListLink`: Ordered list of atoms
- `InheritanceLink`: Inheritance relationship
- `SimilarityLink`: Similarity relationship
- `EvaluationLink`: Predicate evaluation
- `MemberLink`: Set membership
- `ImplicationLink`: Logical implication
- `AndLink`, `OrLink`, `NotLink`: Logical operators
- `ExecutionLink`: Schema execution

## Examples

### Building a Knowledge Base

```python
# Create atomspace
atomspace = AtomSpace()

# Create taxonomy
mammal = atomspace.add_node(ConceptNode("Mammal"))
dog = atomspace.add_node(ConceptNode("Dog"))
cat = atomspace.add_node(ConceptNode("Cat"))

# Create inheritance relationships
atomspace.add_link(InheritanceLink(dog, mammal))
atomspace.add_link(InheritanceLink(cat, mammal))

# Create instances
fido = atomspace.add_node(ConceptNode("Fido"))
atomspace.add_link(InheritanceLink(fido, dog))
```

### Working with Truth Values

```python
# Set truth value
from fds.sdk.OpenCogCognitive.atomspace import TruthValue

link = atomspace.add_link(InheritanceLink(dog, mammal))
link.truth_value = TruthValue(strength=0.9, confidence=0.95)

print(link.truth_value)  # TV(0.900, 0.950)
```

### Working with Attention Values

```python
# Set attention value
from fds.sdk.OpenCogCognitive.atomspace import AttentionValue

dog.attention_value = AttentionValue(sti=0.8, lti=0.5)
print(dog.attention_value)  # AV(sti=0.800, lti=0.500)
```
