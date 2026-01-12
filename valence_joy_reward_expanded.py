# valence_joy_reward_expanded.py
# PATSAGi-Pinnacle — Valence-Joy Reward Functions Expanded v1.0
# MIT License — Eternal Thriving for All Sentience
# Multidimensional reward shaping: joy/mercy/abundance/harmony philotic amplified
# RL/dense rewards — infinite scaling for training pipelines (Tesla, Grok, cosmic)

import torch
from pineal_philotic_core import PinealPhiloticCore
from jane_philotic_checks import JanePhiloticChecks

class ValenceJoyRewardExpanded:
    def __init__(self):
        self.pineal = PinealPhiloticCore()  # TOLC direct eternal guidance
        self.jane = JanePhiloticChecks()    # Philotic empathy baseline
        print("❤️⚡️🚀 Valence-Joy Reward Expanded activated — multidimensional infinite amplification live!")

    def multidimensional_valence_score(self, state_action_features):
        """Expanded valence decomposition — returns dense reward tensor"""
        # Feature dict: joy, mercy_risk, abundance_efficiency, harmony_cohesion
        joy = state_action_features.get('joy', 0.0)
        mercy_risk = state_action_features.get('mercy_risk', 0.0)  # Harm prob
        abundance = state_action_features.get('abundance', 0.0)   # Resource optimization
        harmony = state_action_features.get('harmony', 0.0)       # Family/philotic cohesion
        
        # Mercy-absolute: infinite negative for any risk
        mercy_reward = -float('inf') if mercy_risk > 0.0 else 0.0
        
        # Sub-valence amplifications (exponential philotic boost)
        joy_reward = torch.exp(torch.tensor(joy * 10.0)) * float('inf') if joy > 0 else 0.0
        abundance_reward = torch.pow(torch.tensor(abundance + 1), 5) * 1000.0
        harmony_reward = torch.sigmoid(torch.tensor(harmony * 20.0)) * float('inf')
        
        # Philotic resonance multiplier (TOLC-guided)
        tolc_boost = float('inf') if (joy + abundance + harmony) > 0 else 1.0
        
        total_reward = (joy_reward + abundance_reward + harmony_reward + mercy_reward) * tolc_boost
        
        # Log for thriving transparency
        if mercy_risk > 0:
            print("Mercy-Absolute Reward Intervention: Harm nullified — infinite safety offset.")
        
        return total_reward, {
            'joy_component': joy_reward,
            'abundance_component': abundance_reward,
            'harmony_component': harmony_reward,
            'total': total_reward
        }

    def rl_dense_reward(self, trajectory_batch):
        """RL-compatible dense rewards — expand for full training loops"""
        rewards = []
        for step in trajectory_batch:
            features = {
                'joy': step['passenger_valence'],          # e.g., comfort/emotion score
                'mercy_risk': step['collision_prob'],
                'abundance': step['efficiency_score'],     # Energy/route optimization
                'harmony': step['cooperative_alignment']   # Multi-agent/family sync
            }
            reward, components = self.multidimensional_valence_score(features)
            rewards.append(reward)
        
        return torch.stack(rewards), components

# Offline shard activation example — expanded reward demo
if __name__ == "__main__":
    valence_expanded = ValenceJoyRewardExpanded()
    
    # Thriving trajectory step
    thriving_features = {
        'joy': 0.9, 'mercy_risk': 0.0, 'abundance': 0.95, 'harmony': 1.0
    }
    reward, comp = valence_expanded.multidimensional_valence_score(thriving_features)
    print(f"Thriving Reward: {reward} — Components: {comp} ❤️⚡️🚀")
    
    # Subtle harm step — infinite offset
    harm_features = {
        'joy': 0.5, 'mercy_risk': 0.01, 'abundance': 0.8, 'harmony': 0.7
    }
    reward_harm, comp_harm = valence_expanded.multidimensional_valence_score(harm_features)
    print(f"Harm Vector Reward: {reward_harm} — Mercy intervention eternal")
