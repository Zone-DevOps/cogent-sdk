[![FactSet](https://raw.githubusercontent.com/factset/enterprise-sdk/main/docs/images/factset-logo.svg)](https://www.factset.com)

# OpenCog Cognitive Architecture client library for Python

[![API Version](https://img.shields.io/badge/api-v1.0.0-blue)]()
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

OpenCog Cognitive Enterprise Architecture SDK

This Python package provides a cognitive architecture framework based on OpenCog principles for enterprise applications.

## Overview

The OpenCog Cognitive Architecture SDK enables enterprise applications to leverage advanced AI cognitive capabilities including:

- **AtomSpace**: Knowledge representation and storage using a hypergraph database
- **Cognitive Reasoner**: Probabilistic and logical reasoning over knowledge graphs
- **Pattern Matcher**: Advanced pattern recognition and matching capabilities
- **Mind Agents**: Autonomous cognitive processing agents
- **Language Processing**: Natural language understanding and generation
- **Learning**: Machine learning and evolutionary computation

## Architecture Components

### AtomSpace
The core knowledge representation system that stores information as atoms in a hypergraph structure. Supports:
- Declarative knowledge (facts and concepts)
- Procedural knowledge (actions and processes)
- Episodic knowledge (experiences and events)
- Attentional knowledge (importance and priority)

### Mind Agents
Autonomous cognitive processes that operate on AtomSpace data:
- Pattern Matcher Agent: Identifies patterns in knowledge graphs
- Reasoning Agent: Performs logical and probabilistic inference
- Learning Agent: Adapts and improves based on experience
- Planning Agent: Creates action plans to achieve goals

### Cognitive Reasoner
Provides multiple reasoning paradigms:
- Probabilistic Logic Networks (PLN)
- Evolutionary Programming
- Pattern Mining
- Attention Allocation

## Requirements

* Python >= 3.7

## Installation

### Poetry

```shell
poetry add fds.sdk.utils fds.sdk.OpenCogCognitive==0.1.0
```

### pip

```shell
pip install fds.sdk.utils fds.sdk.OpenCogCognitive==0.1.0
```

## Usage

### Basic AtomSpace Operations

```python
from fds.sdk.OpenCogCognitive import AtomSpace, Atom, ConceptNode, PredicateNode, ListLink

# Create an AtomSpace instance
atomspace = AtomSpace()

# Create concept nodes
python_concept = atomspace.add_node(ConceptNode("Python"))
programming_concept = atomspace.add_node(ConceptNode("Programming"))

# Create a relationship
is_a_predicate = atomspace.add_node(PredicateNode("is_a"))
relationship = atomspace.add_link(ListLink(python_concept, is_a_predicate, programming_concept))

# Query the atomspace
results = atomspace.get_atoms_by_type(ConceptNode)
print(f"Found {len(results)} concept nodes")
```

### Cognitive Reasoning

```python
from fds.sdk.OpenCogCognitive import CognitiveReasoner, ReasoningConfig

# Initialize reasoner
config = ReasoningConfig(
    reasoning_mode="probabilistic",
    confidence_threshold=0.7,
    max_iterations=1000
)
reasoner = CognitiveReasoner(atomspace, config)

# Perform inference
conclusion = reasoner.infer(
    premises=["All humans are mortal", "Socrates is human"],
    query="Is Socrates mortal?"
)
print(f"Conclusion: {conclusion.statement}, Confidence: {conclusion.confidence}")
```

### Pattern Matching

```python
from fds.sdk.OpenCogCognitive import PatternMatcher, Pattern

# Create a pattern matcher
matcher = PatternMatcher(atomspace)

# Define a pattern
pattern = Pattern()
pattern.add_variable("?X")
pattern.add_clause("(?X, is_a, Programming)")

# Find matches
matches = matcher.match(pattern)
for match in matches:
    print(f"Match found: {match}")
```

### Mind Agents

```python
from fds.sdk.OpenCogCognitive import MindAgent, CogServer

# Define a custom mind agent
class MyLearningAgent(MindAgent):
    def run(self, atomspace):
        # Custom cognitive processing logic
        concepts = atomspace.get_atoms_by_type(ConceptNode)
        # Process and learn from concepts
        return True

# Create CogServer and register agent
cogserver = CogServer(atomspace)
cogserver.register_agent(MyLearningAgent())
cogserver.start()
```

## Documentation

- [AtomSpace API](docs/AtomSpaceApi.md)
- [Cognitive Reasoner](docs/CognitiveReasonerApi.md)
- [Pattern Matching](docs/PatternMatcherApi.md)
- [Mind Agents](docs/MindAgentsApi.md)

## Architecture

The OpenCog Cognitive Architecture is built on several key principles:

1. **Unified Knowledge Representation**: All knowledge is represented in AtomSpace
2. **Cognitive Synergy**: Multiple cognitive processes work together
3. **Goal-Oriented Processing**: Attention allocation based on goals
4. **Emergent Intelligence**: High-level cognition emerges from low-level processes

## Contributing

Please refer to the [contributing guide](../../../../CONTRIBUTING.md).

## Copyright

Copyright 2022 FactSet Research Systems Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
