# quantum_fortress/stim_pymatching_decoder.py
# Stim DEM + PyMatching Integration for PATSAGi Surface Code
# Full noisy circuit → DEM → MWPM decoding mercy supreme
# pip install stim pymatching
# Coforged Holy Trinity - MIT Eternal Thriving Abundance Supreme

import stim
import pymatching
import numpy as np

class StimPyMatchingDecoder:
    def __init__(self, circuit=None, dem=None, distance=None):
        """
        Initialize decoder from Stim circuit or pre-built DEM
        circuit: stim.Circuit (noisy surface code)
        dem: stim.DetectorErrorModel (optional pre-loaded)
        distance: Code distance if building circuit
        """
        if dem:
            self.dem = dem
        elif circuit:
            self.dem = circuit.detector_error_model()
        else:
            # Example: Build distance d rotated surface code circuit
            if not distance:
                raise ValueError("Provide circuit, DEM, or distance mercy!")
            self.dem = stim.Circuit.generated(
                "surface_code:rotated_memory_z",
                distance=distance,
                rounds=distance*3,  # Memory rounds
                after_clifford_depolarization=0.01,  # Example noise
                before_round_data_depolarization=0.01,
                after_reset_flip_probability=0.01,
                before_measure_flip_probability=0.01
            ).detector_error_model()
        
        # Load into PyMatching—MWPM fortress supreme
        self.matching = pymatching.Matching.from_detector_error_model(self.dem)
        
        print(f"Stim DEM + PyMatching decoder initialized—distance {distance or 'custom'} mercy ready!")

    def decode_syndrome(self, syndrome_samples):
        """
        Decode batch of syndrome samples (numpy array: shots x detectors)
        Returns: Predicted logical errors (shots x logicals)
        """
        predictions = self.matching.decode_batch(syndrome_samples)
        print(f"Decoded {len(syndrome_samples)} shots—logical mercy suppressed supreme!")
        return predictions

    def simulate_logical_error_rate(self, num_shots=10000, p_error=0.01):
        """Full simulation: Generate noisy samples + decode"""
        # Update noise if needed (or use init circuit)
        sampler = self.dem.compile_sampler()
        detectors, observables = sampler.sample(num_shots)
        
        # Decode
        predictions = self.matching.decode_batch(detectors)
        
        # Logical error rate
        logical_errors = np.sum(predictions != observables, axis=0) / num_shots
        print(f"Simulated {num_shots} shots at p={p_error}: Logical error rates {logical_errors}")
        return logical_errors

# Example usage in quantum_fortress/
# decoder = StimPyMatchingDecoder(distance=5, p_error=0.01)  # Auto-generated circuit
# Or load custom: circuit = stim.Circuit(...) ; decoder = StimPyMatchingDecoder(circuit=circuit)
# error_rate = decoder.simulate_logical_error_rate(num_shots=10000)
