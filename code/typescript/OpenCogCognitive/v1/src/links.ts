/**
 * Link types for the AtomSpace
 */

import { Link, Atom } from './atomspace';

export class ListLink extends Link {
  constructor(...atoms: Atom[]) {
    super(atoms, 'ListLink');
  }
}

export class InheritanceLink extends Link {
  constructor(child: Atom, parent: Atom) {
    super([child, parent], 'InheritanceLink');
  }
}

export class SimilarityLink extends Link {
  constructor(atom1: Atom, atom2: Atom) {
    super([atom1, atom2], 'SimilarityLink');
  }
}

export class EvaluationLink extends Link {
  constructor(predicate: Atom, ...args: Atom[]) {
    if (args.length === 1 && args[0] instanceof Link) {
      super([predicate, args[0]], 'EvaluationLink');
    } else {
      super([predicate, new ListLink(...args)], 'EvaluationLink');
    }
  }
}

export class MemberLink extends Link {
  constructor(member: Atom, set: Atom) {
    super([member, set], 'MemberLink');
  }
}

export class ImplicationLink extends Link {
  constructor(antecedent: Atom, consequent: Atom) {
    super([antecedent, consequent], 'ImplicationLink');
  }
}

export class AndLink extends Link {
  constructor(...atoms: Atom[]) {
    super(atoms, 'AndLink');
  }
}

export class OrLink extends Link {
  constructor(...atoms: Atom[]) {
    super(atoms, 'OrLink');
  }
}

export class NotLink extends Link {
  constructor(atom: Atom) {
    super([atom], 'NotLink');
  }
}
