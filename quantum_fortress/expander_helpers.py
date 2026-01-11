# quantum_fortress/expander_helpers.py
# Quantum Expander Code Helpers for PATSAGi TOLC Layers
# Useful functions for classical expander generation, hypergraph product CSS construction,
# basic parameter estimation, and simple decoding demo
# Sparse graph abundance—low overhead qLDPC mercy supreme
# Coforged Holy Trinity - MIT Eternal Thriving Abundance Supreme

import numpy as np
import random  # Grace RNG for random expanders (replace with structured for optimal)
import math

def generate_classical_expander_parity_check(n_vars, d_check, d_var, seed=None):
    """
    Generate sparse parity-check matrix H for classical bipartite expander
    n_vars: number of variable nodes
    d_check: regular degree of check nodes (left-regular)
    d_var: approximate degree of variable nodes
    seed: for reproducibility mercy
    Returns: H (m_checks x n_vars) sparse matrix as np.array
    """
    if seed:
        random.seed(seed)
        np.random.seed(seed)
    
    m_checks = int(n_vars * d_var / d_check)  # Balanced checks
    
    # Random left-regular bipartite graph (simple configuration model approximation)
    H = np.zeros((m_checks, n_vars), dtype=int)
    
    # Stub lists for configuration model mercy (exact degrees)
    check_stubs = list(range(m_checks)) * d_check
    var_stubs = list(range(n_vars)) * d_var
    
    random.shuffle(check_stubs)
    random.shuffle(var_stubs)
    
    # Pair stubs—allow multi-edges/loops (real expanders avoid, but demo mercy)
    for i in range(len(check_stubs)):
        check = check_stubs[i]
        var = var_stubs[i]
        H[check, var] = 1  # Or +=1 for multi-edges
    
    print(f"Classical expander H generated: {m_checks} checks x {n_vars} vars, degrees ~{d_check}/{d_var}")
    return H

def estimate_expander_parameters(H):
    """
    Estimate rate and approximate distance for classical expander H
    Returns: dict with 'rate', 'min_distance_estimate'
    """
    m, n = H.shape
    rate = 1 - m / n if n > 0 else 0
    
    # Simple min distance estimate: smallest column weight (lower bound)
    col_weights = np.sum(H, axis=0)
    min_dist = np.min(col_weights[col_weights > 0]) if np.any(col_weights > 0) else 0
    
    return {"rate": rate, "min_distance_estimate": min_dist}

def hypergraph_product_css(H1, H2):
    """
    Hypergraph product of two classical parity-check matrices → quantum CSS qLDPC
    Hx = [H1 ⊗ I_{n2}    I_{m1} ⊗ H2^T]
    Hz = [I_{n1} ⊗ H2    H1^T ⊗ I_{m2}]
    Returns: Hx, Hz np arrays + parameter dict
    """
    m1, n1 = H1.shape
    m2, n2 = H2.shape
    
    # Kronecker mercy
    H1_I_n2 = np.kron(H1, np.eye(n2))
    I_m1_H2T = np.kron(np.eye(m1), H2.T)
    
    I_n1_H2 = np.kron(np.eye(n1), H2)
    H1T_I_m2 = np.kron(H1.T, np.eye(m2))
    
    # Block horizontal stack
    Hx = np.hstack((H1_I_n2, I_m1_H2T))
    Hz = np.hstack((I_n1_H2, H1T_I_m2))
    
    physical = Hx.shape[1]
    stabilizers = Hx.shape[0] + Hz.shape[0]
    logical_est = physical - stabilizers  # Approximate (rank mercy)
    
    params = {
        "physical_qubits": physical,
        "x_stabilizers": Hx.shape[0],
        "z_stabilizers": Hz.shape[0],
        "logical_qubits_est": logical_est,
        "rate_est": logical_est / physical if physical > 0 else 0
    }
    
    print(f"Quantum expander CSS constructed immaculate—rate ~{params['rate_est']:.3f}")
    return Hx, Hz, params

def simple_flip_decoder(H, syndrome, max_iters=10):
    """
    Simple small-set flip decoder demo for classical expander (or CSS projection)
    syndrome: 1D array length m_checks
    Returns: estimated error vector (n_vars length)
    """
    m, n = H.shape
    error = np.zeros(n, dtype=int)
    current_synd = syndrome.copy()
    
    for iter in range(max_iters):
        flips = 0
        # Find variables flipping most unsatisfied checks
        unsatisfied = np.dot(H, error) % 2 != current_synd
        weights = np.dot(H.T, unsatisfied.astype(int))
        
        # Flip highest weight variables (greedy mercy)
        to_flip = np.where(weights == weights.max())[0]
        for v in to_flip:
            error[v] ^= 1
            flips += 1
        
        if flips == 0:
            break
    
    print(f"Simple flip decoder converged in {iter+1} iterations—residual syndrome {np.sum(np.dot(H, error) % 2 != syndrome)}")
    return error

# Demo function
def demo_expander_helpers(n_vars=20, d_check=4, d_var=6):
    """Demo full helper workflow"""
    H_class = generate_classical_expander_parity_check(n_vars, d_check, d_var, seed=42)
    params = estimate_expander_parameters(H_class)
    print(f"Classical params: {params}")
    
    Hx, Hz, q_params = hypergraph_product_css(H_class, H_class)  # Symmetric grace
    print(f"Quantum params: {q_params}")
    
    # Mock syndrome + decode demo (project to classical)
    syndrome_mock = np.random.choice([0,1], size=H_class.shape[0])
    correction = simple_flip_decoder(H_class, syndrome_mock)
    
    return Hx, Hz, q_params

# Run demo
# demo_expander_helpers()
