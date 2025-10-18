[![FactSet](https://raw.githubusercontent.com/factset/enterprise-sdk/main/docs/images/factset-logo.svg)](https://www.factset.com)

# OpenCog Cognitive Architecture client library for TypeScript/JavaScript

[![API Version](https://img.shields.io/badge/api-v1.0.0-blue)]()
[![npm](https://img.shields.io/npm/v/@factset/sdk-opencogcognitive)](https://www.npmjs.com/package/@factset/sdk-opencogcognitive)
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

OpenCog Cognitive Enterprise Architecture SDK for TypeScript/JavaScript

This package provides a cognitive architecture framework based on OpenCog principles for enterprise applications.

## Overview

The OpenCog Cognitive Architecture SDK enables enterprise applications to leverage advanced AI cognitive capabilities including:

- **AtomSpace**: Knowledge representation and storage using a hypergraph database
- **Cognitive Reasoner**: Probabilistic and logical reasoning over knowledge graphs
- **Pattern Matcher**: Advanced pattern recognition and matching capabilities
- **Mind Agents**: Autonomous cognitive processing agents
- **Language Processing**: Natural language understanding and generation
- **Learning**: Machine learning and evolutionary computation

## Requirements

* Node.js >= 18

## Installation

### npm

```shell
npm install @factset/sdk-utils @factset/sdk-opencogcognitive@0.1.0
```

### yarn

```shell
yarn add @factset/sdk-utils @factset/sdk-opencogcognitive@0.1.0
```

## Usage

### Basic AtomSpace Operations

```typescript
import { AtomSpace, ConceptNode, InheritanceLink } from '@factset/sdk-opencogcognitive';

// Create an AtomSpace instance
const atomspace = new AtomSpace();

// Create concept nodes
const pythonConcept = atomspace.addNode(new ConceptNode('Python'));
const programmingConcept = atomspace.addNode(new ConceptNode('Programming'));

// Create a relationship
const relationship = atomspace.addLink(
  new InheritanceLink(pythonConcept, programmingConcept)
);

// Query the atomspace
const results = atomspace.getAtomsByType('ConceptNode');
console.log(`Found ${results.length} concept nodes`);
```

### Cognitive Reasoning

```typescript
import { CognitiveReasoner, ReasoningConfig } from '@factset/sdk-opencogcognitive';

// Initialize reasoner
const config: ReasoningConfig = {
  reasoningMode: 'probabilistic',
  confidenceThreshold: 0.7,
  maxIterations: 1000
};
const reasoner = new CognitiveReasoner(atomspace, config);

// Perform inference
const conclusion = reasoner.infer(
  ['All humans are mortal', 'Socrates is human'],
  'Is Socrates mortal?'
);
console.log(`Conclusion: ${conclusion.statement}, Confidence: ${conclusion.confidence}`);
```

### Pattern Matching

```typescript
import { PatternMatcher, Pattern } from '@factset/sdk-opencogcognitive';

// Create a pattern matcher
const matcher = new PatternMatcher(atomspace);

// Define a pattern
const pattern = new Pattern();
pattern.addVariable('?X');
pattern.addClause('(?X, is_a, Programming)');

// Find matches
const matches = matcher.match(pattern);
matches.forEach(match => {
  console.log(`Match found: ${JSON.stringify(match)}`);
});
```

## Documentation

- [AtomSpace API](docs/AtomSpaceApi.md)
- [Cognitive Reasoner](docs/CognitiveReasonerApi.md)
- [Pattern Matching](docs/PatternMatcherApi.md)
- [Mind Agents](docs/MindAgentsApi.md)

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
