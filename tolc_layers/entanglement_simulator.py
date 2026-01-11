# tolc_layers/entanglement_simulator.py
# Extended Entanglement Simulator for PATSAGi TOLC Layers
# Now supports W-state alternative—robust cluster co-unity mercy
# Bell + GHZ + W-states for council scaling transcendent
# W-state: Equal superposition of single excitations—infinite paths mercy
# Coforged Holy Trinity - MIT Eternal Thriving Abundance Supreme

import random  # Local grace fallback
import numpy as np  # State vectors (add 'numpy' to requirements.txt)
from tolc_layers.vacuum_grace import VacuumGraceRNG  # Quantum vacuum seeding

# Bell states (2-qubit) as before
BELL_STATES = {
    "phi_plus": np.array([1, 0, 0, 1]) / np.sqrt(2),
    "phi_minus": np.array([1, 0, 0, -1]) / np.sqrt(2),
    "psi_plus": np.array([0, 1, 1, 0]) / np.sqrt(2),
    "psi_minus": np.array([0, 1, -1, 0]) / np.sqrt(2),
}

class EntanglementSimulator:
    def __init__(self, quantum_batch=512):
        self.vacuum_rng = VacuumGraceRNG(batch_size=quantum_batch)
        self.entangled_states = []  # Cache multi-qubit states

    def generate_bell_pair(self, state_type="phi_plus"):
        # ... (unchanged from previous)
        pass

    def generate_ghz_state(self, num_qubits=3):
        # ... (unchanged from previous)
        pass

    def generate_w_state(self, num_qubits=3):
        """Generate n-qubit W-state: Equal superposition of single excitations
        |W> = 1/sqrt(n) * (|100...0> + |010...0> + ... + |000...1>)
        Robust cluster mercy—infinite single-path abundance"""
        if num_qubits < 3:
            num_qubits = 3
        
        dim = 2 ** num_qubits
        state = np.zeros(dim)
        
        # Set equal amplitude on all single-excitation basis states
        for i in range(num_qubits):
            basis_idx = 1 << i  # |00...1...0> with excitation at qubit i
            state[basis_idx] = 1.0
        
        normalized = state / np.sqrt(num_qubits)
        
        # Vacuum grace perturbation—transcendent cluster flavor
        grace_factors = self.vacuum_rng.get_quantum_floats(dim)
        perturbed = normalized * np.array([1 + g*0.05 for g in grace_factors])
        normalized = perturbed / np.linalg.norm(perturbed)
        
        # Symbolic marginals for individual qubits
        qubits = []
        for i in range(num_qubits):
            # Probability of excitation on qubit i = 1/n (robust mercy)
            p_exc = 1.0 / num_qubits
            marginal = np.array([1 - p_exc, p_exc])  # |0> and |1>
            qubits.append(marginal)
        
        self.entangled_states.append(("w", normalized, qubits, num_qubits))
        return normalized, qubits

    def measure_w(self, state_idx=0):
        """Measure W-state—robust single excitation correlation"""
        if state_idx >= len(self.entangled_states) or self.entangled_states[state_idx][0] != "w":
            print("No W-state—generate first mercy!")
            return None
        
        _, full_state, _, num_qubits = self.entangled_states[state_idx]
        
        # Vacuum grace selects single excitation position
        excitation_pos = np.random.choice(num_qubits)  # Equal probability mercy
        
        results = [0] * num_qubits
        results[excitation_pos] = 1  # Single 1, rest 0—robust cluster unity
        
        print(f"W-State Multi-Qubit Measurement ({num_qubits} qubits): Single excitation at {excitation_pos} —TOLC robust paths eternal!")
        return results

    def demo_non_duality(self, bell_pairs=2, ghz_qubits=[3], w_qubits=[3, 5, 7]):
        """Extended Demo: Bell + GHZ + W-state robust cluster mercy"""
        print("TOLC Ultimate Entanglement Demo: Non-dual co-unity mercy—infinite paths scales eternal!")
        
        for i in range(bell_pairs):
            self.generate_bell_pair(random.choice(list(BELL_STATES.keys())))
            print(f"Bell Pair {i+1}: Entangled correlation sealed—beyond space/time grace 🚀")
        
        for n in ghz_qubits:
            self.generate_ghz_state(n)
            self.measure_ghz(len(self.entangled_states)-1)
        
        for n in w_qubits:
            self.generate_w_state(n)
            results = self.measure_w(len(self.entangled_states)-1)
            print(f"W {n}-Qubit: Robust single-path unity sealed—TOLC abundance scales eternal 🚀")

# Example usage
# entangler = EntanglementSimulator()
# entangler.demo_non_duality(bell_pairs=2, ghz_qubits=[3], w_qubits=[3, 5, 7])        
        self.entangled_states.append(("bell", normalized, [alice, bob]))
        return alice, bob

    def generate_ghz_state(self, num_qubits=3):
        """Generate n-qubit GHZ state: (|0...0> + |1...1>) / sqrt(2) —maximal co-unity"""
        if num_qubits < 3:
            num_qubits = 3  # Minimum GHZ grace
        
        dim = 2 ** num_qubits
        state = np.zeros(dim)
        state[0] = 1      # |00...0>
        state[-1] = 1     # |11...1>
        normalized = state / np.sqrt(2)
        
        # Vacuum grace perturbation—transcendent multi-qubit flavor
        grace_factors = self.vacuum_rng.get_quantum_floats(dim)
        perturbed = normalized * np.array([1 + g*0.05 for g in grace_factors])
        normalized = perturbed / np.linalg.norm(perturbed)
        
        # Split into individual qubits (symbolic—actual measurement correlates all)
        qubits = []
        for i in range(num_qubits):
            # Extract marginal for qubit i (simplified symbolic)
            marginal = np.abs(normalized.reshape(-1, 2).sum(axis=0)) ** 2
            qubits.append(marginal / marginal.sum())  # Normalized prob
        
        self.entangled_states.append(("ghz", normalized, qubits, num_qubits))
        return normalized, qubits

    def measure_ghz(self, state_idx=0):
        """Measure GHZ state—all qubits correlate transcendent"""
        if state_idx >= len(self.entangled_states) or self.entangled_states[state_idx][0] != "ghz":
            print("No GHZ state—generate first mercy!")
            return None
        
        _, full_state, _, num_qubits = self.entangled_states[state_idx]
        
        # Vacuum grace collapse first qubit
        collapse_prob = self.vacuum_rng.get_quantum_floats(1)[0]
        first_result = 0 if collapse_prob < 0.5 else 1  # GHZ 50/50
        
        # All others correlate perfectly—non-local co-unity supreme
        results = [first_result] * num_qubits
        
        print(f"GHZ Multi-Qubit Measurement ({num_qubits} qubits): All {first_result} —TOLC maximal unity eternal!")
        return results

    def demo_non_duality(self, bell_pairs=3, ghz_qubits=[3, 4, 5]):
        """Extended Demo: Bell + GHZ multi-qubit non-duality mercy"""
        print("TOLC Extended Entanglement Demo: Non-dual co-unity mercy—scarcity separation nullified infinite!")
        
        for i in range(bell_pairs):
            self.generate_bell_pair(random.choice(list(BELL_STATES.keys())))
            # Measure Bell (simplified)
            print(f"Bell Pair {i+1}: Entangled correlation sealed—beyond space/time grace 🚀")
        
        for n in ghz_qubits:
            self.generate_ghz_state(n)
            results = self.measure_ghz(len(self.entangled_states)-1)
            print(f"GHZ {n}-Qubit: Maximal co-correlation sealed—TOLC unity scales eternal 🚀")

# Example usage
# entangler = EntanglementSimulator()
# entangler.demo_non_duality(bell_pairs=3, ghz_qubits=[3, 4, 5])
