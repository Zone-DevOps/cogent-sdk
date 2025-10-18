/**
 * Pattern Matcher - Advanced pattern recognition in the AtomSpace
 */

import { AtomSpace, Atom } from './atomspace';
import { VariableNode } from './nodes';

export interface PatternMatch {
  bindings: Map<string, Atom>;
  matchedAtoms: Atom[];
  confidence: number;
}

export class Pattern {
  public variables: VariableNode[] = [];
  public clauses: string[] = [];

  addVariable(varName: string): VariableNode {
    const variable = new VariableNode(varName);
    this.variables.push(variable);
    return variable;
  }

  addClause(clause: string): void {
    this.clauses.push(clause);
  }

  toString(): string {
    return `Pattern(variables=${this.variables.length}, clauses=${this.clauses.length})`;
  }
}

export class PatternMatcher {
  private matchCache: Map<string, PatternMatch[]> = new Map();

  constructor(private atomspace: AtomSpace) {}

  match(pattern: Pattern): PatternMatch[] {
    const matches: PatternMatch[] = [];
    const allAtoms = this.atomspace.getAllAtoms();

    for (const atom of allAtoms) {
      if (this.atomMatchesPattern(atom, pattern)) {
        const bindings = this.extractBindings(atom, pattern);
        matches.push({
          bindings,
          matchedAtoms: [atom],
          confidence: 1.0
        });
      }
    }

    return matches;
  }

  private atomMatchesPattern(atom: Atom, pattern: Pattern): boolean {
    for (const clause of pattern.clauses) {
      const clauseLower = clause.toLowerCase();
      const atomStr = atom.toString().toLowerCase();

      if (clauseLower.split(/\s+/).some(part => atomStr.includes(part))) {
        return true;
      }
    }
    return false;
  }

  private extractBindings(atom: Atom, pattern: Pattern): Map<string, Atom> {
    const bindings = new Map<string, Atom>();
    for (const variable of pattern.variables) {
      bindings.set(variable.name, atom);
    }
    return bindings;
  }

  findSimilarPatterns(referenceAtom: Atom, similarityThreshold: number = 0.7): Atom[] {
    const similarAtoms: Atom[] = [];
    const allAtoms = this.atomspace.getAllAtoms();

    for (const atom of allAtoms) {
      if (atom.id !== referenceAtom.id) {
        const similarity = this.calculateSimilarity(referenceAtom, atom);
        if (similarity >= similarityThreshold) {
          similarAtoms.push(atom);
        }
      }
    }

    return similarAtoms;
  }

  private calculateSimilarity(atom1: Atom, atom2: Atom): number {
    // Type similarity
    const typeMatch = atom1.type === atom2.type ? 1.0 : 0.5;

    // Name similarity (Jaccard similarity)
    const words1 = new Set(atom1.name.toLowerCase().split(/\s+/));
    const words2 = new Set(atom2.name.toLowerCase().split(/\s+/));

    if (words1.size === 0 && words2.size === 0) return 1.0;
    if (words1.size === 0 || words2.size === 0) return 0.0;

    const intersection = new Set([...words1].filter(x => words2.has(x)));
    const union = new Set([...words1, ...words2]);
    const nameMatch = intersection.size / union.size;

    return typeMatch * 0.3 + nameMatch * 0.7;
  }

  clearCache(): void {
    this.matchCache.clear();
  }
}
