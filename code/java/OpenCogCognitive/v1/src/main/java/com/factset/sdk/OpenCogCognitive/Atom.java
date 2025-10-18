package com.factset.sdk.OpenCogCognitive;

import java.time.Instant;
import java.util.UUID;

/**
 * Base class for all atoms (nodes and links)
 */
public abstract class Atom {
    private final String id;
    private final String name;
    private final String type;
    private TruthValue truthValue;
    private AttentionValue attentionValue;
    private final Instant createdAt;
    
    public Atom(String name, String type) {
        this.id = UUID.randomUUID().toString();
        this.name = name;
        this.type = type;
        this.truthValue = new TruthValue(1.0, 1.0);
        this.attentionValue = new AttentionValue(0.5);
        this.createdAt = Instant.now();
    }
    
    public String getId() {
        return id;
    }
    
    public String getName() {
        return name;
    }
    
    public String getType() {
        return type;
    }
    
    public TruthValue getTruthValue() {
        return truthValue;
    }
    
    public void setTruthValue(TruthValue truthValue) {
        this.truthValue = truthValue;
    }
    
    public AttentionValue getAttentionValue() {
        return attentionValue;
    }
    
    public void setAttentionValue(AttentionValue attentionValue) {
        this.attentionValue = attentionValue;
    }
    
    public Instant getCreatedAt() {
        return createdAt;
    }
    
    @Override
    public String toString() {
        return String.format("%s(%s)", type, name);
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Atom)) return false;
        Atom other = (Atom) obj;
        return id.equals(other.id);
    }
    
    @Override
    public int hashCode() {
        return id.hashCode();
    }
}

/**
 * TruthValue - Probabilistic truth value
 */
class TruthValue {
    private double strength;
    private double confidence;
    
    public TruthValue(double strength, double confidence) {
        this.strength = Math.max(0.0, Math.min(1.0, strength));
        this.confidence = Math.max(0.0, Math.min(1.0, confidence));
    }
    
    public double getStrength() {
        return strength;
    }
    
    public void setStrength(double strength) {
        this.strength = Math.max(0.0, Math.min(1.0, strength));
    }
    
    public double getConfidence() {
        return confidence;
    }
    
    public void setConfidence(double confidence) {
        this.confidence = Math.max(0.0, Math.min(1.0, confidence));
    }
    
    @Override
    public String toString() {
        return String.format("TV(%.3f, %.3f)", strength, confidence);
    }
}

/**
 * AttentionValue - Attention value for importance-based processing
 */
class AttentionValue {
    private double sti;  // Short-term importance
    private double lti;  // Long-term importance
    private double vlti; // Very long-term importance
    
    public AttentionValue(double sti) {
        this(sti, 0.0, 0.0);
    }
    
    public AttentionValue(double sti, double lti) {
        this(sti, lti, 0.0);
    }
    
    public AttentionValue(double sti, double lti, double vlti) {
        this.sti = sti;
        this.lti = lti;
        this.vlti = vlti;
    }
    
    public double getSti() {
        return sti;
    }
    
    public void setSti(double sti) {
        this.sti = sti;
    }
    
    public double getLti() {
        return lti;
    }
    
    public void setLti(double lti) {
        this.lti = lti;
    }
    
    public double getVlti() {
        return vlti;
    }
    
    public void setVlti(double vlti) {
        this.vlti = vlti;
    }
    
    @Override
    public String toString() {
        return String.format("AV(sti=%.3f, lti=%.3f)", sti, lti);
    }
}
