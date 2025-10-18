[![FactSet](https://raw.githubusercontent.com/factset/enterprise-sdk/main/docs/images/factset-logo.svg)](https://www.factset.com)

# OpenCog Cognitive Architecture client library for .NET

[![API Version](https://img.shields.io/badge/api-v1.0.0-blue)]()
[![Nuget](https://img.shields.io/nuget/v/FactSet.SDK.OpenCogCognitive)](https://www.nuget.org/packages/FactSet.SDK.OpenCogCognitive)
[![Apache-2 license](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](https://www.apache.org/licenses/LICENSE-2.0)

OpenCog Cognitive Enterprise Architecture SDK for .NET

This .NET package provides a cognitive architecture framework based on OpenCog principles for enterprise applications.

## Overview

The OpenCog Cognitive Architecture SDK enables enterprise applications to leverage advanced AI cognitive capabilities including:

- **AtomSpace**: Knowledge representation and storage using a hypergraph database
- **Cognitive Reasoner**: Probabilistic and logical reasoning over knowledge graphs
- **Pattern Matcher**: Advanced pattern recognition and matching capabilities
- **Mind Agents**: Autonomous cognitive processing agents
- **Language Processing**: Natural language understanding and generation
- **Learning**: Machine learning and evolutionary computation

## Requirements

* .NET Standard 2.0 or higher

## Installation

### Package Manager

```powershell
Install-Package FactSet.SDK.Utils
Install-Package FactSet.SDK.OpenCogCognitive -Version 0.1.0
```

### .NET CLI

```bash
dotnet add package FactSet.SDK.Utils
dotnet add package FactSet.SDK.OpenCogCognitive --version 0.1.0
```

## Usage

### Basic AtomSpace Operations

```csharp
using FactSet.SDK.OpenCogCognitive;

// Create an AtomSpace instance
var atomspace = new AtomSpace();

// Create concept nodes
var pythonConcept = atomspace.AddNode(new ConceptNode("Python"));
var programmingConcept = atomspace.AddNode(new ConceptNode("Programming"));

// Create a relationship
var relationship = atomspace.AddLink(
    new InheritanceLink(pythonConcept, programmingConcept)
);

// Query the atomspace
var results = atomspace.GetAtomsByType("ConceptNode");
Console.WriteLine($"Found {results.Count} concept nodes");
```

### Cognitive Reasoning

```csharp
using FactSet.SDK.OpenCogCognitive;

// Initialize reasoner
var config = new ReasoningConfig
{
    ReasoningMode = "probabilistic",
    ConfidenceThreshold = 0.7,
    MaxIterations = 1000
};
var reasoner = new CognitiveReasoner(atomspace, config);

// Perform inference
var premises = new[] { "All humans are mortal", "Socrates is human" };
var conclusion = reasoner.Infer(premises, "Is Socrates mortal?");
Console.WriteLine($"Conclusion: {conclusion.Statement}, Confidence: {conclusion.Confidence}");
```

### Pattern Matching

```csharp
using FactSet.SDK.OpenCogCognitive;

// Create a pattern matcher
var matcher = new PatternMatcher(atomspace);

// Define a pattern
var pattern = new Pattern();
pattern.AddVariable("?X");
pattern.AddClause("(?X, is_a, Programming)");

// Find matches
var matches = matcher.Match(pattern);
foreach (var match in matches)
{
    Console.WriteLine($"Match found: {match}");
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
