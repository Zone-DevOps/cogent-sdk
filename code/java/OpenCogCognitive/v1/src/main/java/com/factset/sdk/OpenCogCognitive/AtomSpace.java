package com.factset.sdk.OpenCogCognitive;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

/**
 * AtomSpace - Core knowledge representation system
 * 
 * The AtomSpace is a hypergraph database that stores knowledge as atoms.
 */
public class AtomSpace {
    private final Map<String, Atom> atoms;
    private final Map<String, Set<String>> atomsByType;
    private final Map<String, Set<String>> atomsByName;
    private final Map<String, Set<String>> incomingSet;
    
    public AtomSpace() {
        this.atoms = new ConcurrentHashMap<>();
        this.atomsByType = new ConcurrentHashMap<>();
        this.atomsByName = new ConcurrentHashMap<>();
        this.incomingSet = new ConcurrentHashMap<>();
    }
    
    public Node addNode(Node node) {
        if (!atoms.containsKey(node.getId())) {
            atoms.put(node.getId(), node);
            
            atomsByType.computeIfAbsent(node.getType(), k -> ConcurrentHashMap.newKeySet())
                      .add(node.getId());
            
            atomsByName.computeIfAbsent(node.getName(), k -> ConcurrentHashMap.newKeySet())
                      .add(node.getId());
        }
        return node;
    }
    
    public Link addLink(Link link) {
        if (!atoms.containsKey(link.getId())) {
            atoms.put(link.getId(), link);
            
            atomsByType.computeIfAbsent(link.getType(), k -> ConcurrentHashMap.newKeySet())
                      .add(link.getId());
            
            // Update incoming sets
            for (Atom atom : link.getOutgoing()) {
                incomingSet.computeIfAbsent(atom.getId(), k -> ConcurrentHashMap.newKeySet())
                          .add(link.getId());
            }
        }
        return link;
    }
    
    public Optional<Atom> getAtom(String atomId) {
        return Optional.ofNullable(atoms.get(atomId));
    }
    
    public List<Atom> getAtomsByType(String atomType) {
        Set<String> atomIds = atomsByType.getOrDefault(atomType, Collections.emptySet());
        List<Atom> result = new ArrayList<>();
        for (String id : atomIds) {
            Atom atom = atoms.get(id);
            if (atom != null) {
                result.add(atom);
            }
        }
        return result;
    }
    
    public List<Atom> getAtomsByName(String name) {
        Set<String> atomIds = atomsByName.getOrDefault(name, Collections.emptySet());
        List<Atom> result = new ArrayList<>();
        for (String id : atomIds) {
            Atom atom = atoms.get(id);
            if (atom != null) {
                result.add(atom);
            }
        }
        return result;
    }
    
    public List<Link> getIncomingSet(Atom atom) {
        Set<String> linkIds = incomingSet.getOrDefault(atom.getId(), Collections.emptySet());
        List<Link> result = new ArrayList<>();
        for (String id : linkIds) {
            Atom a = atoms.get(id);
            if (a instanceof Link) {
                result.add((Link) a);
            }
        }
        return result;
    }
    
    public boolean removeAtom(Atom atom) {
        if (atoms.containsKey(atom.getId())) {
            atoms.remove(atom.getId());
            
            Set<String> typeSet = atomsByType.get(atom.getType());
            if (typeSet != null) {
                typeSet.remove(atom.getId());
            }
            
            Set<String> nameSet = atomsByName.get(atom.getName());
            if (nameSet != null) {
                nameSet.remove(atom.getId());
            }
            
            incomingSet.remove(atom.getId());
            
            return true;
        }
        return false;
    }
    
    public List<Atom> getAllAtoms() {
        return new ArrayList<>(atoms.values());
    }
    
    public int size() {
        return atoms.size();
    }
    
    public void clear() {
        atoms.clear();
        atomsByType.clear();
        atomsByName.clear();
        incomingSet.clear();
    }
    
    @Override
    public String toString() {
        return String.format("AtomSpace(atoms=%d)", size());
    }
}
