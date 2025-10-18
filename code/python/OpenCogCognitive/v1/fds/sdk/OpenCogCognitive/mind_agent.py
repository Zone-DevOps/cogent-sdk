"""
Mind Agents - Autonomous cognitive processing agents

Mind agents perform cognitive tasks on the AtomSpace.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
import threading
import time
from fds.sdk.OpenCogCognitive.atomspace import AtomSpace


class MindAgent(ABC):
    """
    Base class for mind agents.
    
    Mind agents are autonomous cognitive processes that operate on
    the AtomSpace to perform specific cognitive tasks.
    """
    
    def __init__(self, name: Optional[str] = None):
        self.name = name or self.__class__.__name__
        self.frequency = 1.0  # Runs per second
        self.enabled = True
    
    @abstractmethod
    def run(self, atomspace: AtomSpace) -> bool:
        """
        Execute one cycle of the agent's cognitive processing.
        
        Args:
            atomspace: The AtomSpace to operate on
            
        Returns:
            True if processing should continue, False to stop
        """
        pass
    
    def __repr__(self):
        return f"{self.name}(enabled={self.enabled})"


class AttentionAllocationAgent(MindAgent):
    """
    Allocates attention to atoms based on importance.
    
    Implements Importance Diffusion and other attention allocation
    mechanisms.
    """
    
    def __init__(self):
        super().__init__("AttentionAllocationAgent")
    
    def run(self, atomspace: AtomSpace) -> bool:
        """Allocate attention to atoms"""
        atoms = atomspace.get_all_atoms()
        
        # Update attention values based on usage and importance
        for atom in atoms:
            # Decay attention over time
            atom.attention_value.sti *= 0.99
            
            # Boost attention for atoms with high truth values
            if atom.truth_value.confidence > 0.8:
                atom.attention_value.sti = min(1.0, atom.attention_value.sti + 0.01)
        
        return True


class ForgetAgent(MindAgent):
    """
    Removes low-importance atoms from the AtomSpace.
    
    Implements forgetting to manage memory and computational resources.
    """
    
    def __init__(self, forget_threshold: float = 0.1):
        super().__init__("ForgetAgent")
        self.forget_threshold = forget_threshold
    
    def run(self, atomspace: AtomSpace) -> bool:
        """Remove low-importance atoms"""
        atoms = atomspace.get_all_atoms()
        
        atoms_to_remove = [
            atom for atom in atoms 
            if atom.attention_value.sti < self.forget_threshold
        ]
        
        for atom in atoms_to_remove:
            atomspace.remove_atom(atom)
        
        return True


class HebbianLearningAgent(MindAgent):
    """
    Implements Hebbian learning to strengthen frequently co-occurring patterns.
    
    "Neurons that fire together, wire together"
    """
    
    def __init__(self):
        super().__init__("HebbianLearningAgent")
    
    def run(self, atomspace: AtomSpace) -> bool:
        """Strengthen co-occurring patterns"""
        atoms = atomspace.get_all_atoms()
        
        # Strengthen truth values of frequently accessed atoms
        for atom in atoms:
            if atom.attention_value.sti > 0.7:
                # Increase confidence for high-attention atoms
                atom.truth_value.confidence = min(
                    1.0, 
                    atom.truth_value.confidence + 0.01
                )
        
        return True


class CogServer:
    """
    CogServer manages the execution of mind agents.
    
    It schedules and runs mind agents in a coordinated manner.
    """
    
    def __init__(self, atomspace: AtomSpace):
        self.atomspace = atomspace
        self.agents: List[MindAgent] = []
        self.running = False
        self.thread: Optional[threading.Thread] = None
    
    def register_agent(self, agent: MindAgent):
        """Register a mind agent with the CogServer"""
        self.agents.append(agent)
    
    def unregister_agent(self, agent: MindAgent):
        """Unregister a mind agent"""
        if agent in self.agents:
            self.agents.remove(agent)
    
    def start(self, threaded: bool = True):
        """Start the CogServer"""
        self.running = True
        
        if threaded:
            self.thread = threading.Thread(target=self._run_loop)
            self.thread.daemon = True
            self.thread.start()
        else:
            self._run_loop()
    
    def stop(self):
        """Stop the CogServer"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=5.0)
    
    def _run_loop(self):
        """Main execution loop for mind agents"""
        while self.running:
            # Execute each enabled agent
            for agent in self.agents:
                if agent.enabled:
                    try:
                        should_continue = agent.run(self.atomspace)
                        if not should_continue:
                            agent.enabled = False
                    except Exception as e:
                        print(f"Error in agent {agent.name}: {e}")
            
            # Sleep based on fastest agent frequency
            if self.agents:
                max_frequency = max(agent.frequency for agent in self.agents)
                sleep_time = 1.0 / max_frequency if max_frequency > 0 else 1.0
                time.sleep(sleep_time)
            else:
                time.sleep(1.0)
    
    def get_agent_status(self) -> List[dict]:
        """Get status of all registered agents"""
        return [
            {
                "name": agent.name,
                "enabled": agent.enabled,
                "frequency": agent.frequency
            }
            for agent in self.agents
        ]
    
    def __repr__(self):
        return f"CogServer(agents={len(self.agents)}, running={self.running})"
