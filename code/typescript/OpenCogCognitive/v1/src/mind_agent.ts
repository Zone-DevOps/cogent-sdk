/**
 * Mind Agents - Autonomous cognitive processing agents
 */

import { AtomSpace } from './atomspace';

export abstract class MindAgent {
  public frequency: number = 1.0;
  public enabled: boolean = true;

  constructor(public name: string) {}

  abstract run(atomspace: AtomSpace): boolean;

  toString(): string {
    return `${this.name}(enabled=${this.enabled})`;
  }
}

export class AttentionAllocationAgent extends MindAgent {
  constructor() {
    super('AttentionAllocationAgent');
  }

  run(atomspace: AtomSpace): boolean {
    const atoms = atomspace.getAllAtoms();

    for (const atom of atoms) {
      // Decay attention over time
      atom.attentionValue.sti *= 0.99;

      // Boost attention for atoms with high truth values
      if (atom.truthValue.confidence > 0.8) {
        atom.attentionValue.sti = Math.min(1.0, atom.attentionValue.sti + 0.01);
      }
    }

    return true;
  }
}

export class ForgetAgent extends MindAgent {
  constructor(private forgetThreshold: number = 0.1) {
    super('ForgetAgent');
  }

  run(atomspace: AtomSpace): boolean {
    const atoms = atomspace.getAllAtoms();
    const atomsToRemove = atoms.filter(
      atom => atom.attentionValue.sti < this.forgetThreshold
    );

    for (const atom of atomsToRemove) {
      atomspace.removeAtom(atom);
    }

    return true;
  }
}

export class HebbianLearningAgent extends MindAgent {
  constructor() {
    super('HebbianLearningAgent');
  }

  run(atomspace: AtomSpace): boolean {
    const atoms = atomspace.getAllAtoms();

    for (const atom of atoms) {
      if (atom.attentionValue.sti > 0.7) {
        atom.truthValue.confidence = Math.min(
          1.0,
          atom.truthValue.confidence + 0.01
        );
      }
    }

    return true;
  }
}

export class CogServer {
  private agents: MindAgent[] = [];
  private running: boolean = false;
  private intervalId?: NodeJS.Timeout;

  constructor(private atomspace: AtomSpace) {}

  registerAgent(agent: MindAgent): void {
    this.agents.push(agent);
  }

  unregisterAgent(agent: MindAgent): void {
    const index = this.agents.indexOf(agent);
    if (index !== -1) {
      this.agents.splice(index, 1);
    }
  }

  start(): void {
    this.running = true;
    this.runLoop();
  }

  stop(): void {
    this.running = false;
    if (this.intervalId) {
      clearTimeout(this.intervalId);
    }
  }

  private runLoop(): void {
    if (!this.running) return;

    // Execute each enabled agent
    for (const agent of this.agents) {
      if (agent.enabled) {
        try {
          const shouldContinue = agent.run(this.atomspace);
          if (!shouldContinue) {
            agent.enabled = false;
          }
        } catch (error) {
          console.error(`Error in agent ${agent.name}:`, error);
        }
      }
    }

    // Schedule next iteration
    const maxFrequency = this.agents.length > 0
      ? Math.max(...this.agents.map(a => a.frequency))
      : 1.0;
    const sleepTime = 1000 / maxFrequency;

    this.intervalId = setTimeout(() => this.runLoop(), sleepTime);
  }

  getAgentStatus(): Array<{ name: string; enabled: boolean; frequency: number }> {
    return this.agents.map(agent => ({
      name: agent.name,
      enabled: agent.enabled,
      frequency: agent.frequency
    }));
  }

  toString(): string {
    return `CogServer(agents=${this.agents.length}, running=${this.running})`;
  }
}
