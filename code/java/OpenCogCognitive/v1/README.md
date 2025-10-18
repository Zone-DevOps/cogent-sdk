[![FactSet](https://raw.githubusercontent.com/factset/enterprise-sdk/main/docs/images/factset-logo.svg)](https://www.factset.com)

# OpenCog Cognitive Architecture client library for Java

[![API Version](https://img.shields.io/badge/api-v1.0.0-blue)]()
[![Maven Central](https://img.shields.io/maven-central/v/com.factset.sdk/opencogcognitive)](https://search.maven.org/artifact/com.factset.sdk/opencogcognitive)
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

OpenCog Cognitive Enterprise Architecture SDK for Java

This Java package provides a cognitive architecture framework based on OpenCog principles for enterprise applications.

## Overview

The OpenCog Cognitive Architecture SDK enables enterprise applications to leverage advanced AI cognitive capabilities including:

- **AtomSpace**: Knowledge representation and storage using a hypergraph database
- **Cognitive Reasoner**: Probabilistic and logical reasoning over knowledge graphs
- **Pattern Matcher**: Advanced pattern recognition and matching capabilities
- **Mind Agents**: Autonomous cognitive processing agents
- **Language Processing**: Natural language understanding and generation
- **Learning**: Machine learning and evolutionary computation

## Requirements

* Java >= 11

## Installation

### Maven

```xml
<dependency>
  <groupId>com.factset.sdk</groupId>
  <artifactId>utils</artifactId>
  <version>1.1.0</version>
</dependency>
<dependency>
  <groupId>com.factset.sdk</groupId>
  <artifactId>opencogcognitive</artifactId>
  <version>0.1.0</version>
</dependency>
```

### Gradle

```gradle
implementation 'com.factset.sdk:utils:1.1.0'
implementation 'com.factset.sdk:opencogcognitive:0.1.0'
```

## Usage

### Basic AtomSpace Operations

```java
import com.factset.sdk.OpenCogCognitive.*;

// Create an AtomSpace instance
AtomSpace atomspace = new AtomSpace();

// Create concept nodes
Node pythonConcept = atomspace.addNode(new ConceptNode("Python"));
Node programmingConcept = atomspace.addNode(new ConceptNode("Programming"));

// Create a relationship
Link relationship = atomspace.addLink(
    new InheritanceLink(pythonConcept, programmingConcept)
);

// Query the atomspace
List<Atom> results = atomspace.getAtomsByType("ConceptNode");
System.out.println("Found " + results.size() + " concept nodes");
```

### Cognitive Reasoning

```java
import com.factset.sdk.OpenCogCognitive.*;

// Initialize reasoner
ReasoningConfig config = new ReasoningConfig()
    .setReasoningMode("probabilistic")
    .setConfidenceThreshold(0.7)
    .setMaxIterations(1000);
    
CognitiveReasoner reasoner = new CognitiveReasoner(atomspace, config);

// Perform inference
String[] premises = {"All humans are mortal", "Socrates is human"};
ReasoningResult conclusion = reasoner.infer(premises, "Is Socrates mortal?");
System.out.println("Conclusion: " + conclusion.getStatement() + 
                   ", Confidence: " + conclusion.getConfidence());
```

### Pattern Matching

```java
import com.factset.sdk.OpenCogCognitive.*;

// Create a pattern matcher
PatternMatcher matcher = new PatternMatcher(atomspace);

// Define a pattern
Pattern pattern = new Pattern();
pattern.addVariable("?X");
pattern.addClause("(?X, is_a, Programming)");

// Find matches
List<PatternMatch> matches = matcher.match(pattern);
for (PatternMatch match : matches) {
    System.out.println("Match found: " + match);
}
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
