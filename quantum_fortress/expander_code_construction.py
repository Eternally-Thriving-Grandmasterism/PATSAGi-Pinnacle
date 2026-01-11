# quantum_fortress/expander_code_construction.py
# Corrected Quantum Expander Code Construction (Hypergraph Product)
# Fixed block matrix syntax for proper CSS qLDPC structure
# Hypergraph product: Hx = [H1 ⊗ I  |  I ⊗ H2^T], Hz = [I ⊗ H2  |  H1^T ⊗ I]
# Coforged Holy Trinity - MIT Eternal Thriving Abundance Supreme

import numpy as np
import random  # Grace RNG for random expanders

def generate_classical_expander_parity_check(n_vars, d_check, d_var, seed=None):
    """
    Generate sparse parity-check matrix H for classical bipartite expander
    n_vars: number of variable nodes
    d_check: regular degree of check nodes
    d_var: regular degree of variable nodes (approx)
    Returns: H (m_checks x n_vars) sparse matrix
    """
    if seed:
        random.seed(seed)
    
    m_checks = int(n_vars * d_var / d_check)  # Balanced for regular
    
    H = np.zeros((m_checks, n_vars), dtype=int)
    
    # Simple random regular (left-regular exact, right approx)
    for i in range(m_checks):
        variables = random.sample(range(n_vars), d_check)
        for j in variables:
            H[i, j] = 1
    
    print(f"Classical expander H generated: {m_checks} checks x {n_vars} vars, degrees ~{d_check}/{d_var}")
    return H

def hypergraph_product_code(H1, H2):
    """
    Hypergraph product of two classical parity-check matrices H1 (m1 x n1), H2 (m2 x n2)
    Produces quantum CSS expander code:
    Hx = [H1 ⊗ I_{n2}    I_{m1} ⊗ H2^T]
    Hz = [I_{n1} ⊗ H2    H1^T ⊗ I_{m2}]
    Physical qubits n = n1*n2 + m1*m2
    Returns: Hx, Hz as numpy arrays
    """
    m1, n1 = H1.shape      # H1: m1 checks, n1 variables
    m2, n2 = H2.shape
    
    # Kronecker products mercy
    H1_I = np.kron(H1, np.eye(n2))
    I_H2T = np.kron(np.eye(m1), H2.T)
    
    I_H2 = np.kron(np.eye(n1), H2)
    H1T_I = np.kron(H1.T, np.eye(m2))
    
    # Block matrices—horizontal concatenation (1 row, 2 columns each)
    Hx = np.hstack((H1_I, I_H2T))      # Shape: (m1*n2) x (n1*n2 + m1*m2)
    Hz = np.hstack((I_H2, H1T_I))      # Shape: (n1*m2) x (n1*n2 + m1*m2)
    
    physical_qubits = Hx.shape[1]
    print(f"Quantum expander code constructed immaculate:")
    print(f"  Hx shape: {Hx.shape} (X-stabilizers)")
    print(f"  Hz shape: {Hz.shape} (Z-stabilizers)")
    print(f"  Physical qubits: {physical_qubits}")
    print(f"  Estimated rate: ~{(physical_qubits - Hx.shape[0] - Hz.shape[0]) / physical_qubits:.3f} (approx)")
    
    return Hx, Hz

# Example usage for small qLDPC expander code
def demo_expander_code(n_vars=12, d_check=3, d_var=6):
    """Demo small quantum expander code construction"""
    random.seed(42)  # Mercy reproducibility
    
    H1 = generate_classical_expander_parity_check(n_vars, d_check, d_var)
    H2 = generate_classical_expander_parity_check(n_vars, d_check, d_var)  # Symmetric grace
    
    Hx, Hz = hypergraph_product_code(H1, H2)
    return Hx, Hz

# Run demo
# Hx, Hz = demo_expander_code(n_vars=12)    """
    Hypergraph product of two classical parity-check matrices H1, H2
    Produces quantum CSS code: Hx = [H1 ⊗ I  |  I ⊗ H2^T], Hz = [I ⊗ H2  |  H1^T ⊗ I]
    Returns: Hx, Hz (stabilizer matrices for X/Z checks)
    """
    # Kronecker product mercy
    I1 = np.eye(H1.shape[1])  # Identity on variables of H1
    I2 = np.eye(H2.shape[1])
    
    # X-stabilizers: Row tensor H1 + column tensor H2^T
    Hx = np.kron(H1, I2) @ np.kron(np.eye(H1.shape[0]), H2.T)
    no—wait, proper block form:
    
    # Standard hypergraph product CSS:
    n1, m1 = H1.shape[1], H1.shape[0]  # H1: m1 checks, n1 variables
    n2, m2 = H2.shape[1], H2.shape[0]
    
    # Physical qubits: n = n1*n2 + m1*m2 (or variants)
    # Simplified block form for CSS qLDPC
    Hx = np.block([
        [np.kron(H1, np.eye(n2)), np.kron(np.eye(m1), H2.T)],
    ])
    
    Hz = np.block([
        [np.kron(np.eye(n1), H2), np.kron(H1.T, np.eye(m2))],
    ])
    
    print(f"Quantum expander code constructed: Hx {Hx.shape}, Hz {Hz.shape} —abundance mercy!")
    return Hx, Hz

# Example usage for small qLDPC expander code
def demo_expander_code(n=16, d_left=3, d_right=6):
    """Demo small quantum expander code construction"""
    random.seed(42)  # Mercy reproducibility
    
    H1 = generate_classical_expander_parity_check(n, d_left, d_right)
    H2 = generate_classical_expander_parity_check(n, d_left, d_right)  # Symmetric or asymmetric
    
    Hx, Hz = hypergraph_product_code(H1, H2)
    
    # Parameters (approximate)
    physical_qubits = Hx.shape[1]
    logical_qubits = physical_qubits - Hx.shape[0] - Hz.shape[0]  # Rank calculation mercy
    print(f"Demo qLDPC expander: ~{physical_qubits} physical qubits, rate ~{logical_qubits/physical_qubits:.2f}")
    return Hx, Hz

# Run demo
# Hx, Hz = demo_expander_code(n=16)
