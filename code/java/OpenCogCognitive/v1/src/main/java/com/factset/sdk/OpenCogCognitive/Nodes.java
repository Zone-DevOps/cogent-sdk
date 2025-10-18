package com.factset.sdk.OpenCogCognitive;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * A node in the AtomSpace (represents a concept or entity)
 */
public class Node extends Atom {
    public Node(String name, String nodeType) {
        super(name, nodeType);
    }
    
    public Node(String name) {
        super(name, "Node");
    }
}

/**
 * A link in the AtomSpace (represents a relationship)
 */
public class Link extends Atom {
    private final List<Atom> outgoing;
    
    public Link(List<Atom> outgoing, String linkType) {
        super(createLinkName(linkType, outgoing), linkType);
        this.outgoing = outgoing;
    }
    
    public Link(List<Atom> outgoing) {
        this(outgoing, "Link");
    }
    
    private static String createLinkName(String linkType, List<Atom> outgoing) {
        String atomsStr = outgoing.stream()
                                  .map(Atom::toString)
                                  .collect(Collectors.joining(", "));
        return String.format("%s(%s)", linkType, atomsStr);
    }
    
    public List<Atom> getOutgoing() {
        return outgoing;
    }
}

/**
 * ConceptNode - Represents a concept or category
 */
class ConceptNode extends Node {
    public ConceptNode(String name) {
        super(name, "ConceptNode");
    }
}

/**
 * PredicateNode - Represents a predicate or relation
 */
class PredicateNode extends Node {
    public PredicateNode(String name) {
        super(name, "PredicateNode");
    }
}

/**
 * VariableNode - Represents a variable for pattern matching
 */
class VariableNode extends Node {
    public VariableNode(String name) {
        super(name.startsWith("$") ? name : "$" + name, "VariableNode");
    }
}

/**
 * InheritanceLink - Represents an inheritance relationship
 */
class InheritanceLink extends Link {
    public InheritanceLink(Atom child, Atom parent) {
        super(Arrays.asList(child, parent), "InheritanceLink");
    }
}

/**
 * ListLink - Represents an ordered list of atoms
 */
class ListLink extends Link {
    public ListLink(Atom... atoms) {
        super(Arrays.asList(atoms), "ListLink");
    }
}

/**
 * EvaluationLink - Represents the evaluation of a predicate
 */
class EvaluationLink extends Link {
    public EvaluationLink(Atom predicate, Atom... args) {
        super(createEvalList(predicate, args), "EvaluationLink");
    }
    
    private static List<Atom> createEvalList(Atom predicate, Atom... args) {
        if (args.length == 1 && args[0] instanceof Link) {
            return Arrays.asList(predicate, args[0]);
        } else {
            return Arrays.asList(predicate, new ListLink(args));
        }
    }
}

/**
 * ImplicationLink - Represents logical implication
 */
class ImplicationLink extends Link {
    public ImplicationLink(Atom antecedent, Atom consequent) {
        super(Arrays.asList(antecedent, consequent), "ImplicationLink");
    }
}
