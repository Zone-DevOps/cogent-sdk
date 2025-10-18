"""
OpenCog Cognitive Architecture - Comprehensive Example

This example demonstrates the key features of the OpenCog Cognitive Architecture SDK.
"""

from fds.sdk.OpenCogCognitive import (
    AtomSpace,
    ConceptNode,
    PredicateNode,
    InheritanceLink,
    EvaluationLink,
    ListLink,
    CognitiveReasoner,
    ReasoningConfig,
    PatternMatcher,
    Pattern,
    MindAgent,
    CogServer,
    AttentionAllocationAgent,
    HebbianLearningAgent
)


def example_basic_atomspace():
    """Example 1: Basic AtomSpace Operations"""
    print("=" * 60)
    print("Example 1: Basic AtomSpace Operations")
    print("=" * 60)
    
    # Create an AtomSpace
    atomspace = AtomSpace()
    
    # Create nodes
    dog = atomspace.add_node(ConceptNode("Dog"))
    cat = atomspace.add_node(ConceptNode("Cat"))
    mammal = atomspace.add_node(ConceptNode("Mammal"))
    animal = atomspace.add_node(ConceptNode("Animal"))
    
    # Create inheritance relationships
    atomspace.add_link(InheritanceLink(dog, mammal))
    atomspace.add_link(InheritanceLink(cat, mammal))
    atomspace.add_link(InheritanceLink(mammal, animal))
    
    # Query the atomspace
    concepts = atomspace.get_atoms_by_type(ConceptNode)
    print(f"Total concepts: {len(concepts)}")
    
    # Get incoming links
    mammal_children = atomspace.get_incoming_set(mammal)
    print(f"Things that inherit from Mammal: {len(mammal_children)}")
    
    print(f"AtomSpace size: {atomspace.size()} atoms\n")


def example_cognitive_reasoning():
    """Example 2: Cognitive Reasoning"""
    print("=" * 60)
    print("Example 2: Cognitive Reasoning")
    print("=" * 60)
    
    atomspace = AtomSpace()
    
    # Configure reasoner
    config = ReasoningConfig(
        reasoning_mode="probabilistic",
        confidence_threshold=0.7,
        max_iterations=1000
    )
    reasoner = CognitiveReasoner(atomspace, config)
    
    # Example 1: Classic syllogism
    result = reasoner.infer(
        ["All humans are mortal", "Socrates is human"],
        "Is Socrates mortal?"
    )
    print(f"Query: {result.statement}")
    print(f"Confidence: {result.confidence:.2f}")
    print(f"Supporting premises: {result.reasoning_chain}\n")
    
    # Example 2: Multiple premises
    result = reasoner.infer(
        [
            "Python is a programming language",
            "Programming languages are tools",
            "Tools help developers"
        ],
        "Does Python help developers?"
    )
    print(f"Query: {result.statement}")
    print(f"Confidence: {result.confidence:.2f}\n")


def example_pattern_matching():
    """Example 3: Pattern Matching"""
    print("=" * 60)
    print("Example 3: Pattern Matching")
    print("=" * 60)
    
    atomspace = AtomSpace()
    
    # Build a knowledge base
    programming_langs = ["Python", "Java", "C++", "JavaScript", "Go"]
    programming = atomspace.add_node(ConceptNode("Programming Language"))
    
    for lang in programming_langs:
        lang_node = atomspace.add_node(ConceptNode(lang))
        atomspace.add_link(InheritanceLink(lang_node, programming))
    
    # Create a pattern matcher
    matcher = PatternMatcher(atomspace)
    
    # Define a pattern to find all programming languages
    pattern = Pattern()
    var_x = pattern.add_variable("?X")
    pattern.add_clause("ConceptNode")
    
    # Find matches
    matches = matcher.match(pattern)
    print(f"Pattern: Find all ConceptNodes")
    print(f"Matches found: {len(matches)}")
    
    # Find similar patterns
    python_node = atomspace.get_atoms_by_name("Python")[0]
    similar = matcher.find_similar_patterns(python_node, similarity_threshold=0.5)
    print(f"\nAtoms similar to Python: {len(similar)}")
    for atom in similar[:3]:  # Show first 3
        print(f"  - {atom}\n")


def example_knowledge_base():
    """Example 4: Building a Knowledge Base"""
    print("=" * 60)
    print("Example 4: Building a Knowledge Base")
    print("=" * 60)
    
    atomspace = AtomSpace()
    
    # Create a taxonomy
    entities = {
        "Animal": ["Mammal", "Bird", "Fish"],
        "Mammal": ["Dog", "Cat", "Human"],
        "Bird": ["Eagle", "Sparrow"],
        "Dog": ["Labrador", "Poodle"]
    }
    
    nodes = {}
    for entity in ["Animal", "Mammal", "Bird", "Fish", "Dog", "Cat", 
                   "Human", "Eagle", "Sparrow", "Labrador", "Poodle"]:
        nodes[entity] = atomspace.add_node(ConceptNode(entity))
    
    # Build inheritance hierarchy
    for parent, children in entities.items():
        for child in children:
            atomspace.add_link(InheritanceLink(nodes[child], nodes[parent]))
    
    # Add properties
    has_fur = atomspace.add_node(PredicateNode("has_fur"))
    can_fly = atomspace.add_node(PredicateNode("can_fly"))
    
    atomspace.add_link(EvaluationLink(has_fur, nodes["Mammal"]))
    atomspace.add_link(EvaluationLink(can_fly, nodes["Bird"]))
    
    print(f"Knowledge base created with {atomspace.size()} atoms")
    print(f"Concepts: {len(atomspace.get_atoms_by_type(ConceptNode))}")
    print(f"Predicates: {len(atomspace.get_atoms_by_type(PredicateNode))}")
    print(f"Inheritance links: {len(atomspace.get_atoms_by_type(InheritanceLink))}\n")


def example_mind_agents():
    """Example 5: Mind Agents and CogServer"""
    print("=" * 60)
    print("Example 5: Mind Agents and CogServer")
    print("=" * 60)
    
    atomspace = AtomSpace()
    
    # Add some test data
    for i in range(10):
        node = atomspace.add_node(ConceptNode(f"Concept_{i}"))
        node.attention_value.sti = 0.5 + (i * 0.05)
        node.truth_value.confidence = 0.6 + (i * 0.02)
    
    # Create CogServer
    cogserver = CogServer(atomspace)
    
    # Register agents
    cogserver.register_agent(AttentionAllocationAgent())
    cogserver.register_agent(HebbianLearningAgent())
    
    print(f"Registered {len(cogserver.agents)} agents")
    
    # Show agent status
    for status in cogserver.get_agent_status():
        print(f"  - {status['name']}: {'enabled' if status['enabled'] else 'disabled'}")
    
    # Run agents once (non-threaded for example)
    print("\nRunning agents...")
    initial_avg_sti = sum(a.attention_value.sti for a in atomspace.get_all_atoms()) / atomspace.size()
    
    for agent in cogserver.agents:
        agent.run(atomspace)
    
    final_avg_sti = sum(a.attention_value.sti for a in atomspace.get_all_atoms()) / atomspace.size()
    
    print(f"Average STI before: {initial_avg_sti:.3f}")
    print(f"Average STI after: {final_avg_sti:.3f}")
    print("Agents modified attention values\n")


def example_advanced_reasoning():
    """Example 6: Advanced Reasoning with Rules"""
    print("=" * 60)
    print("Example 6: Advanced Reasoning with Rules")
    print("=" * 60)
    
    atomspace = AtomSpace()
    
    # Build knowledge
    dog = atomspace.add_node(ConceptNode("Dog"))
    mammal = atomspace.add_node(ConceptNode("Mammal"))
    animal = atomspace.add_node(ConceptNode("Animal"))
    
    link1 = atomspace.add_link(InheritanceLink(dog, mammal))
    link2 = atomspace.add_link(InheritanceLink(mammal, animal))
    
    # Create reasoner
    reasoner = CognitiveReasoner(atomspace)
    
    # Apply inference rule: transitivity
    result = reasoner.apply_inference_rule(
        "inheritance_transitivity",
        link1,
        link2
    )
    
    if result:
        print(f"Inference rule applied successfully")
        print(f"Conclusion: {result}")
    else:
        print("Could not apply inference rule")
    
    print()


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("OpenCog Cognitive Architecture - Examples")
    print("=" * 60 + "\n")
    
    example_basic_atomspace()
    example_cognitive_reasoning()
    example_pattern_matching()
    example_knowledge_base()
    example_mind_agents()
    example_advanced_reasoning()
    
    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
