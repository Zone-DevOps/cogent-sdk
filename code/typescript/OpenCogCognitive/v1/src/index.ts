/**
 * OpenCog Cognitive Architecture SDK for TypeScript/JavaScript
 * 
 * Main entry point for the SDK
 */

// Core components
export { AtomSpace, Atom, Node, Link, TruthValue, AttentionValue } from './atomspace';

// Node types
export {
  ConceptNode,
  PredicateNode,
  VariableNode,
  SchemaNode,
  WordNode,
  SentenceNode
} from './nodes';

// Link types
export {
  ListLink,
  InheritanceLink,
  SimilarityLink,
  EvaluationLink,
  MemberLink,
  ImplicationLink,
  AndLink,
  OrLink,
  NotLink
} from './links';

// Cognitive reasoner
export {
  CognitiveReasoner,
  ReasoningConfig,
  ReasoningResult
} from './reasoner';

// Pattern matcher
export {
  PatternMatcher,
  Pattern,
  PatternMatch
} from './pattern_matcher';

// Mind agents
export {
  MindAgent,
  AttentionAllocationAgent,
  ForgetAgent,
  HebbianLearningAgent,
  CogServer
} from './mind_agent';
