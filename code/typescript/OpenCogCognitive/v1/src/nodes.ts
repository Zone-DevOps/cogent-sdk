/**
 * Node types for the AtomSpace
 */

import { Node } from './atomspace';

export class ConceptNode extends Node {
  constructor(name: string) {
    super(name, 'ConceptNode');
  }
}

export class PredicateNode extends Node {
  constructor(name: string) {
    super(name, 'PredicateNode');
  }
}

export class VariableNode extends Node {
  constructor(name: string) {
    const varName = name.startsWith('$') ? name : `$${name}`;
    super(varName, 'VariableNode');
  }
}

export class SchemaNode extends Node {
  constructor(name: string) {
    super(name, 'SchemaNode');
  }
}

export class WordNode extends Node {
  constructor(name: string) {
    super(name, 'WordNode');
  }
}

export class SentenceNode extends Node {
  constructor(name: string) {
    super(name, 'SentenceNode');
  }
}
