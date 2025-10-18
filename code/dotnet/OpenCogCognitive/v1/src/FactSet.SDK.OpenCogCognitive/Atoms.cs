using System;
using System.Collections.Generic;
using System.Linq;

namespace FactSet.SDK.OpenCogCognitive
{
    /// <summary>
    /// Base class for all atoms (nodes and links)
    /// </summary>
    public abstract class Atom
    {
        public string Id { get; }
        public string Name { get; }
        public string Type { get; }
        public TruthValue TruthValue { get; set; }
        public AttentionValue AttentionValue { get; set; }
        public DateTime CreatedAt { get; }

        protected Atom(string name, string type)
        {
            Id = Guid.NewGuid().ToString();
            Name = name;
            Type = type;
            TruthValue = new TruthValue(1.0, 1.0);
            AttentionValue = new AttentionValue(0.5);
            CreatedAt = DateTime.UtcNow;
        }

        public override string ToString()
        {
            return $"{Type}({Name})";
        }

        public override bool Equals(object obj)
        {
            if (obj is Atom other)
                return Id == other.Id;
            return false;
        }

        public override int GetHashCode()
        {
            return Id.GetHashCode();
        }
    }

    /// <summary>
    /// A node in the AtomSpace (represents a concept or entity)
    /// </summary>
    public class Node : Atom
    {
        public Node(string name, string nodeType = "Node") : base(name, nodeType)
        {
        }
    }

    /// <summary>
    /// A link in the AtomSpace (represents a relationship)
    /// </summary>
    public class Link : Atom
    {
        public List<Atom> Outgoing { get; }

        public Link(List<Atom> outgoing, string linkType = "Link") 
            : base(CreateLinkName(linkType, outgoing), linkType)
        {
            Outgoing = outgoing;
        }

        private static string CreateLinkName(string linkType, List<Atom> outgoing)
        {
            var atomsStr = string.Join(", ", outgoing.Select(a => a.ToString()));
            return $"{linkType}({atomsStr})";
        }

        public List<Atom> GetOutgoing() => Outgoing;
    }

    /// <summary>
    /// Probabilistic truth value
    /// </summary>
    public class TruthValue
    {
        private double strength;
        private double confidence;

        public double Strength
        {
            get => strength;
            set => strength = Math.Max(0.0, Math.Min(1.0, value));
        }

        public double Confidence
        {
            get => confidence;
            set => confidence = Math.Max(0.0, Math.Min(1.0, value));
        }

        public TruthValue(double strength, double confidence)
        {
            Strength = strength;
            Confidence = confidence;
        }

        public override string ToString()
        {
            return $"TV({Strength:F3}, {Confidence:F3})";
        }
    }

    /// <summary>
    /// Attention value for importance-based processing
    /// </summary>
    public class AttentionValue
    {
        public double Sti { get; set; }  // Short-term importance
        public double Lti { get; set; }  // Long-term importance
        public double Vlti { get; set; } // Very long-term importance

        public AttentionValue(double sti, double lti = 0.0, double vlti = 0.0)
        {
            Sti = sti;
            Lti = lti;
            Vlti = vlti;
        }

        public override string ToString()
        {
            return $"AV(sti={Sti:F3}, lti={Lti:F3})";
        }
    }

    /// <summary>
    /// ConceptNode - Represents a concept or category
    /// </summary>
    public class ConceptNode : Node
    {
        public ConceptNode(string name) : base(name, "ConceptNode")
        {
        }
    }

    /// <summary>
    /// PredicateNode - Represents a predicate or relation
    /// </summary>
    public class PredicateNode : Node
    {
        public PredicateNode(string name) : base(name, "PredicateNode")
        {
        }
    }

    /// <summary>
    /// VariableNode - Represents a variable for pattern matching
    /// </summary>
    public class VariableNode : Node
    {
        public VariableNode(string name) 
            : base(name.StartsWith("$") ? name : $"${name}", "VariableNode")
        {
        }
    }

    /// <summary>
    /// InheritanceLink - Represents an inheritance relationship
    /// </summary>
    public class InheritanceLink : Link
    {
        public InheritanceLink(Atom child, Atom parent) 
            : base(new List<Atom> { child, parent }, "InheritanceLink")
        {
        }
    }

    /// <summary>
    /// ListLink - Represents an ordered list of atoms
    /// </summary>
    public class ListLink : Link
    {
        public ListLink(params Atom[] atoms) 
            : base(atoms.ToList(), "ListLink")
        {
        }
    }

    /// <summary>
    /// EvaluationLink - Represents the evaluation of a predicate
    /// </summary>
    public class EvaluationLink : Link
    {
        public EvaluationLink(Atom predicate, params Atom[] args) 
            : base(CreateEvalList(predicate, args), "EvaluationLink")
        {
        }

        private static List<Atom> CreateEvalList(Atom predicate, Atom[] args)
        {
            if (args.Length == 1 && args[0] is Link)
                return new List<Atom> { predicate, args[0] };
            else
                return new List<Atom> { predicate, new ListLink(args) };
        }
    }
}
