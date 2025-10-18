"""
Configuration for the OpenCog Cognitive Architecture SDK
"""

from typing import Optional


class Configuration:
    """
    SDK Configuration for OpenCog Cognitive Architecture
    
    This class manages configuration settings for the SDK including
    API endpoints, authentication, and cognitive processing parameters.
    """
    
    def __init__(self):
        # Cognitive processing settings
        self.atomspace_max_size = 1000000
        self.attention_allocation_enabled = True
        self.forgetting_enabled = True
        self.hebbian_learning_enabled = True
        
        # Reasoning settings
        self.default_reasoning_mode = "probabilistic"
        self.default_confidence_threshold = 0.7
        self.max_reasoning_iterations = 1000
        
        # Pattern matching settings
        self.pattern_matching_timeout = 30.0  # seconds
        self.similarity_threshold = 0.7
        
        # Mind agent settings
        self.agent_execution_frequency = 1.0  # Hz
        self.agent_thread_pool_size = 4
        
        # Performance settings
        self.enable_caching = True
        self.cache_size = 10000
        
    def to_dict(self):
        """Convert configuration to dictionary"""
        return {
            "atomspace_max_size": self.atomspace_max_size,
            "attention_allocation_enabled": self.attention_allocation_enabled,
            "forgetting_enabled": self.forgetting_enabled,
            "hebbian_learning_enabled": self.hebbian_learning_enabled,
            "default_reasoning_mode": self.default_reasoning_mode,
            "default_confidence_threshold": self.default_confidence_threshold,
            "max_reasoning_iterations": self.max_reasoning_iterations,
            "pattern_matching_timeout": self.pattern_matching_timeout,
            "similarity_threshold": self.similarity_threshold,
            "agent_execution_frequency": self.agent_execution_frequency,
            "agent_thread_pool_size": self.agent_thread_pool_size,
            "enable_caching": self.enable_caching,
            "cache_size": self.cache_size,
        }
    
    @classmethod
    def from_dict(cls, config_dict: dict) -> 'Configuration':
        """Create configuration from dictionary"""
        config = cls()
        for key, value in config_dict.items():
            if hasattr(config, key):
                setattr(config, key, value)
        return config
    
    def __repr__(self):
        return f"Configuration(reasoning_mode={self.default_reasoning_mode})"
