using System;
using System.Collections.Generic;
using System.Collections.Concurrent;
using System.Linq;

namespace FactSet.SDK.OpenCogCognitive
{
    /// <summary>
    /// AtomSpace - Core knowledge representation system
    /// 
    /// The AtomSpace is a hypergraph database that stores knowledge as atoms.
    /// </summary>
    public class AtomSpace
    {
        private readonly ConcurrentDictionary<string, Atom> atoms;
        private readonly ConcurrentDictionary<string, HashSet<string>> atomsByType;
        private readonly ConcurrentDictionary<string, HashSet<string>> atomsByName;
        private readonly ConcurrentDictionary<string, HashSet<string>> incomingSet;
        private readonly object lockObject = new object();

        public AtomSpace()
        {
            atoms = new ConcurrentDictionary<string, Atom>();
            atomsByType = new ConcurrentDictionary<string, HashSet<string>>();
            atomsByName = new ConcurrentDictionary<string, HashSet<string>>();
            incomingSet = new ConcurrentDictionary<string, HashSet<string>>();
        }

        public Node AddNode(Node node)
        {
            if (!atoms.ContainsKey(node.Id))
            {
                atoms[node.Id] = node;

                lock (lockObject)
                {
                    if (!atomsByType.ContainsKey(node.Type))
                        atomsByType[node.Type] = new HashSet<string>();
                    atomsByType[node.Type].Add(node.Id);

                    if (!atomsByName.ContainsKey(node.Name))
                        atomsByName[node.Name] = new HashSet<string>();
                    atomsByName[node.Name].Add(node.Id);
                }
            }
            return node;
        }

        public Link AddLink(Link link)
        {
            if (!atoms.ContainsKey(link.Id))
            {
                atoms[link.Id] = link;

                lock (lockObject)
                {
                    if (!atomsByType.ContainsKey(link.Type))
                        atomsByType[link.Type] = new HashSet<string>();
                    atomsByType[link.Type].Add(link.Id);

                    // Update incoming sets
                    foreach (var atom in link.Outgoing)
                    {
                        if (!incomingSet.ContainsKey(atom.Id))
                            incomingSet[atom.Id] = new HashSet<string>();
                        incomingSet[atom.Id].Add(link.Id);
                    }
                }
            }
            return link;
        }

        public Atom GetAtom(string atomId)
        {
            atoms.TryGetValue(atomId, out var atom);
            return atom;
        }

        public List<Atom> GetAtomsByType(string atomType)
        {
            if (!atomsByType.TryGetValue(atomType, out var atomIds))
                return new List<Atom>();

            return atomIds.Select(id => atoms[id]).ToList();
        }

        public List<Atom> GetAtomsByName(string name)
        {
            if (!atomsByName.TryGetValue(name, out var atomIds))
                return new List<Atom>();

            return atomIds.Select(id => atoms[id]).ToList();
        }

        public List<Link> GetIncomingSet(Atom atom)
        {
            if (!incomingSet.TryGetValue(atom.Id, out var linkIds))
                return new List<Link>();

            return linkIds.Select(id => atoms[id] as Link).Where(l => l != null).ToList();
        }

        public bool RemoveAtom(Atom atom)
        {
            if (atoms.TryRemove(atom.Id, out _))
            {
                lock (lockObject)
                {
                    if (atomsByType.TryGetValue(atom.Type, out var typeSet))
                        typeSet.Remove(atom.Id);

                    if (atomsByName.TryGetValue(atom.Name, out var nameSet))
                        nameSet.Remove(atom.Id);

                    incomingSet.TryRemove(atom.Id, out _);
                }
                return true;
            }
            return false;
        }

        public List<Atom> GetAllAtoms()
        {
            return atoms.Values.ToList();
        }

        public int Size => atoms.Count;

        public void Clear()
        {
            atoms.Clear();
            atomsByType.Clear();
            atomsByName.Clear();
            incomingSet.Clear();
        }

        public override string ToString()
        {
            return $"AtomSpace(atoms={Size})";
        }
    }
}
