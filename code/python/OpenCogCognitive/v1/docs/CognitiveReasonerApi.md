# Cognitive Reasoner API

The Cognitive Reasoner performs reasoning over knowledge in the AtomSpace.

## Overview

The reasoner supports multiple reasoning paradigms:
- **Probabilistic Logic Networks (PLN)**: Probabilistic inference
- **Logical Reasoning**: Classical logical inference
- **Pattern-based Reasoning**: Inference based on pattern matching

## Usage

### Basic Reasoning

```python
from fds.sdk.OpenCogCognitive import CognitiveReasoner, ReasoningConfig, AtomSpace

# Create atomspace and reasoner
atomspace = AtomSpace()
config = ReasoningConfig(
    reasoning_mode="probabilistic",
    confidence_threshold=0.7,
    max_iterations=1000
)
reasoner = CognitiveReasoner(atomspace, config)

# Perform inference
result = reasoner.infer(
    premises=["All humans are mortal", "Socrates is human"],
    query="Is Socrates mortal?"
)

print(f"Conclusion: {result.statement}")
print(f"Confidence: {result.confidence}")
```

### Applying Inference Rules

```python
from fds.sdk.OpenCogCognitive import InheritanceLink, ConceptNode

# Create knowledge
dog = atomspace.add_node(ConceptNode("Dog"))
mammal = atomspace.add_node(ConceptNode("Mammal"))
animal = atomspace.add_node(ConceptNode("Animal"))

link1 = atomspace.add_link(InheritanceLink(dog, mammal))
link2 = atomspace.add_link(InheritanceLink(mammal, animal))

# Apply transitivity rule
result = reasoner.apply_inference_rule(
    "inheritance_transitivity",
    link1,
    link2
)
# Result: Dog inherits from Animal
```

## API Reference

### CognitiveReasoner Class

#### Constructor

```python
CognitiveReasoner(atomspace: AtomSpace, config: Optional[ReasoningConfig] = None)
```

#### Methods

- `infer(premises: List[str], query: str) -> ReasoningResult`: Perform inference
- `apply_inference_rule(rule_name: str, *atoms: Atom) -> Optional[Atom]`: Apply a rule
- `get_reasoning_history() -> List[ReasoningResult]`: Get reasoning history
- `clear_history()`: Clear reasoning history

### ReasoningConfig Class

#### Attributes

- `reasoning_mode`: "probabilistic", "logical", or "evolutionary"
- `confidence_threshold`: Minimum confidence for conclusions (0-1)
- `max_iterations`: Maximum reasoning iterations
- `learning_rate`: Learning rate for adaptive reasoning
- `attention_allocation`: Enable attention-based processing

### ReasoningResult Class

#### Attributes

- `statement`: Conclusion statement
- `confidence`: Confidence in the conclusion (0-1)
- `supporting_evidence`: List of supporting atoms
- `reasoning_chain`: Steps in the reasoning process

## Inference Rules

### Inheritance Transitivity

If A inherits from B and B inherits from C, then A inherits from C.

```python
result = reasoner.apply_inference_rule(
    "inheritance_transitivity",
    inheritance_link1,
    inheritance_link2
)
```

### Modus Ponens

If A and (A implies B), then B.

```python
result = reasoner.apply_inference_rule(
    "modus_ponens",
    fact,
    implication_link
)
```

## Examples

### Complex Reasoning Chain

```python
# Build knowledge base
human = atomspace.add_node(ConceptNode("Human"))
mortal = atomspace.add_node(ConceptNode("Mortal"))
socrates = atomspace.add_node(ConceptNode("Socrates"))

atomspace.add_link(InheritanceLink(human, mortal))
atomspace.add_link(InheritanceLink(socrates, human))

# Perform multi-step reasoning
result = reasoner.infer(
    premises=[
        "All humans are mortal",
        "Socrates is a human"
    ],
    query="Is Socrates mortal?"
)

print(f"Conclusion: {result.statement} (confidence: {result.confidence:.2f})")
```
