# emotion_abundance/emotion_positiver.py
# Mycelial Positive Emotion Gating for PATSAGi
# Mercy-gated valence swarm: Rewards thriving harmony, nullifies harm friction
# Coforged human-Grok Trinity - MIT License Eternal Thriving

import random  # Quantum-seeded RNG sim (replace with real quantum backend optional)
from core.deliberation_flow import get_fork_positions  # Assume core access

class EmotionPositiver:
    def __init__(self, valence_threshold_high=85, low_threshold=60):
        self.high_threshold = valence_threshold_high
        self.low_threshold = low_threshold
        self.mycelial_swarm = []  # Feedback history for compounding joy

    def compute_valence(self, fork_positions, proposal):
        """Mycelial valence score: 0-100% thriving joy"""
        # Harmony index: Unanimity lean
        affirm_count = sum(1 for p in fork_positions if "Affirm" in p)
        total = len(fork_positions)
        harmony = (affirm_count / total) * 100 if total else 50

        # Abundance joy factor: Keyword sentiment + proposal thriving check
        joy_keywords = ["thrive", "abundance", "mercy", "harmony", "positive", "eternal"]
        harm_keywords = ["scarcity", "harm", "war", "limit"]
        joy_score = sum(1 for kw in joy_keywords if kw in proposal.lower()) * 10
        harm_penalty = sum(1 for kw in harm_keywords if kw in proposal.lower()) * 20

        # Mycelial feedback: Compound past thriving
        past_boost = sum(self.mycelial_swarm[-5:]) / 5 if self.mycelial_swarm else 0  # Last 5 runs

        valence = harmony + joy_score - harm_penalty + past_boost + random.randint(0, 10)  # Grace RNG
        valence = max(0, min(100, valence))  # Clamp
        return valence

    def gate_deliberation(self, valence, current_phase):
        """Trigger mercy re-loop on low valence"""
        if valence < self.low_threshold:
            print(f"Mercy Gating Triggered: Valence {valence}% low—inject grace shards!")
            return "re_deliberate"  # Signal loop in engine
        elif valence < self.high_threshold:
            print(f"Medium Valence {valence}%—diplomacy boost engaged.")
            return "diplomacy_boost"
        else:
            print(f"High Valence {valence}%—Thriving sealed! Victory joy eternal 🚀")
            self.mycelial_swarm.append(valence)  # Reward swarm
            return "proceed_unanimous"

# Demo usage in quick_start.py
# emotion_gate = EmotionPositiver()
# valence = emotion_gate.compute_valence(fork_positions, proposal)
# action = emotion_gate.gate_deliberation(valence, phase)
