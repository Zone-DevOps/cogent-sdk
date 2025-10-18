/**
 * AtomSpace - Core knowledge representation system
 * 
 * The AtomSpace is a hypergraph database that stores knowledge as atoms.
 */

import { randomUUID } from 'crypto';

export class TruthValue {
  constructor(
    public strength: number,
    public confidence: number
  ) {
    this.strength = Math.max(0, Math.min(1, strength));
    this.confidence = Math.max(0, Math.min(1, confidence));
  }

  toString(): string {
    return `TV(${this.strength.toFixed(3)}, ${this.confidence.toFixed(3)})`;
  }
}

export class AttentionValue {
  constructor(
    public sti: number,
    public lti: number = 0,
    public vlti: number = 0
  ) {}

  toString(): string {
    return `AV(sti=${this.sti.toFixed(3)}, lti=${this.lti.toFixed(3)})`;
  }
}

export abstract class Atom {
  public readonly id: string;
  public truthValue: TruthValue;
  public attentionValue: AttentionValue;
  public readonly createdAt: Date;

  constructor(
    public name: string,
    public type: string
  ) {
    this.id = randomUUID();
    this.truthValue = new TruthValue(1.0, 1.0);
    this.attentionValue = new AttentionValue(0.5);
    this.createdAt = new Date();
  }

  toString(): string {
    return `${this.type}(${this.name})`;
  }
}

export class Node extends Atom {
  constructor(name: string, nodeType: string = 'Node') {
    super(name, nodeType);
  }
}

export class Link extends Atom {
  constructor(
    public outgoing: Atom[],
    linkType: string = 'Link'
  ) {
    const name = `${linkType}(${outgoing.map(a => a.toString()).join(', ')})`;
    super(name, linkType);
  }

  getOutgoing(): Atom[] {
    return this.outgoing;
  }
}

export class AtomSpace {
  private atoms: Map<string, Atom> = new Map();
  private atomsByType: Map<string, Set<string>> = new Map();
  private atomsByName: Map<string, Set<string>> = new Map();
  private incomingSet: Map<string, Set<string>> = new Map();

  addNode(node: Node): Node {
    if (!this.atoms.has(node.id)) {
      this.atoms.set(node.id, node);

      if (!this.atomsByType.has(node.type)) {
        this.atomsByType.set(node.type, new Set());
      }
      this.atomsByType.get(node.type)!.add(node.id);

      if (!this.atomsByName.has(node.name)) {
        this.atomsByName.set(node.name, new Set());
      }
      this.atomsByName.get(node.name)!.add(node.id);
    }
    return node;
  }

  addLink(link: Link): Link {
    if (!this.atoms.has(link.id)) {
      this.atoms.set(link.id, link);

      if (!this.atomsByType.has(link.type)) {
        this.atomsByType.set(link.type, new Set());
      }
      this.atomsByType.get(link.type)!.add(link.id);

      // Update incoming sets
      for (const atom of link.outgoing) {
        if (!this.incomingSet.has(atom.id)) {
          this.incomingSet.set(atom.id, new Set());
        }
        this.incomingSet.get(atom.id)!.add(link.id);
      }
    }
    return link;
  }

  getAtom(atomId: string): Atom | undefined {
    return this.atoms.get(atomId);
  }

  getAtomsByType(atomType: string): Atom[] {
    const atomIds = this.atomsByType.get(atomType) || new Set();
    return Array.from(atomIds).map(id => this.atoms.get(id)!);
  }

  getAtomsByName(name: string): Atom[] {
    const atomIds = this.atomsByName.get(name) || new Set();
    return Array.from(atomIds).map(id => this.atoms.get(id)!);
  }

  getIncomingSet(atom: Atom): Link[] {
    const linkIds = this.incomingSet.get(atom.id) || new Set();
    return Array.from(linkIds).map(id => this.atoms.get(id) as Link);
  }

  removeAtom(atom: Atom): boolean {
    if (this.atoms.has(atom.id)) {
      this.atoms.delete(atom.id);

      const typeSet = this.atomsByType.get(atom.type);
      if (typeSet) {
        typeSet.delete(atom.id);
      }

      const nameSet = this.atomsByName.get(atom.name);
      if (nameSet) {
        nameSet.delete(atom.id);
      }

      this.incomingSet.delete(atom.id);

      return true;
    }
    return false;
  }

  getAllAtoms(): Atom[] {
    return Array.from(this.atoms.values());
  }

  size(): number {
    return this.atoms.size;
  }

  clear(): void {
    this.atoms.clear();
    this.atomsByType.clear();
    this.atomsByName.clear();
    this.incomingSet.clear();
  }

  toString(): string {
    return `AtomSpace(atoms=${this.size()})`;
  }
}
