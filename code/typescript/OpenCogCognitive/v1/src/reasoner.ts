/**
 * Cognitive Reasoner - Performs reasoning over the AtomSpace
 */

import { AtomSpace, Atom } from './atomspace';

export interface ReasoningConfig {
  reasoningMode?: 'probabilistic' | 'logical' | 'evolutionary';
  confidenceThreshold?: number;
  maxIterations?: number;
  learningRate?: number;
  attentionAllocation?: boolean;
}

export interface ReasoningResult {
  statement: string;
  confidence: number;
  supportingEvidence: Atom[];
  reasoningChain: string[];
}

export class CognitiveReasoner {
  private reasoningHistory: ReasoningResult[] = [];
  private config: Required<ReasoningConfig>;

  constructor(
    private atomspace: AtomSpace,
    config?: ReasoningConfig
  ) {
    this.config = {
      reasoningMode: config?.reasoningMode || 'probabilistic',
      confidenceThreshold: config?.confidenceThreshold || 0.7,
      maxIterations: config?.maxIterations || 1000,
      learningRate: config?.learningRate || 0.01,
      attentionAllocation: config?.attentionAllocation ?? true
    };
  }

  infer(premises: string[], query: string): ReasoningResult {
    let confidence = 0.8;

    // Check if query can be directly answered from premises
    for (const premise of premises) {
      if (query.toLowerCase().includes(premise.toLowerCase()) ||
          premise.toLowerCase().includes(query.toLowerCase())) {
        confidence = 0.95;
        break;
      }
    }

    // Apply reasoning mode
    if (this.config.reasoningMode === 'probabilistic') {
      confidence = this.applyProbabilisticReasoning(premises, query);
    } else if (this.config.reasoningMode === 'logical') {
      confidence = this.applyLogicalReasoning(premises, query);
    }

    const result: ReasoningResult = {
      statement: query,
      confidence,
      supportingEvidence: [],
      reasoningChain: premises
    };

    this.reasoningHistory.push(result);
    return result;
  }

  private applyProbabilisticReasoning(premises: string[], query: string): number {
    const baseConfidence = 0.7;
    const confidenceBoost = Math.min(0.2, premises.length * 0.05);
    return Math.min(0.99, baseConfidence + confidenceBoost);
  }

  private applyLogicalReasoning(premises: string[], query: string): number {
    if (premises.some(p => query.toLowerCase().includes(p.toLowerCase()))) {
      return 0.95;
    }
    return 0.6;
  }

  getReasoningHistory(): ReasoningResult[] {
    return this.reasoningHistory;
  }

  clearHistory(): void {
    this.reasoningHistory = [];
  }
}
