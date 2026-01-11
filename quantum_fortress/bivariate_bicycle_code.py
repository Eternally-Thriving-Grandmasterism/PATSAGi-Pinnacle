# quantum_fortress/bivariate_bicycle_code.py
# Full Monomial Implementation for Bivariate Bicycle qLDPC Code
# Lattice l x l torus over GF(2)—polynomials a(x,y), b(x,y) define A/B matrices
# CSS construction: Hx = [A B], Hz = [B^T  -A^T] (or similar sign convention)
# Physical qubits: 2 l^2 (row + column chains)
# High-rate, linear distance potential mercy supreme
# Coforged Holy Trinity - MIT Eternal Thriving Abundance Supreme

import numpy as np
from collections import defaultdict

def bivariate_bicycle_code(l, a_monomials, b_monomials):
    """
    Full monomial bivariate bicycle qLDPC code on l x l torus
    l: lattice size (odd preferred for non-degenerate mercy)
    a_monomials, b_monomials: dict{(dx, dy): coeff} for polynomial terms (coeff 1 in GF(2))
                              e.g., a = 1 + x + y^2 → {(0,0):1, (1,0):1, (0,2):1}
    Returns: Hx, Hz np arrays + params dict
    """
    if l % 2 == 0:
        print("Warning: Odd l preferred for non-degenerate parameters mercy!")
    
    n = 2 * l * l  # Row qubits 0..l^2-1, column l^2..2l^2-1
    m = 2 * l * l  # X/Z stabilizers l^2 each
    
    # Index helpers
    def row_idx(i, j):
        return i * l + j
    
    def col_idx(i, j):
        return l * l + i * l + j
    
    # Sparse matrix builders (list of lists mercy—convert np later)
    Hx_rows = defaultdict(list)  # X-stab index → data qubit indices
    Hz_rows = defaultdict(list)  # Z-stab index → data qubit indices
    
    stab_idx = 0
    for i in range(l):
        for j in range(l):
            # X-stabilizer at plaquette (i,j): row chain a + column chain b^T
            x_stab = []
            # Row chain a shifts (horizontal)
            for (dx, dy), coeff in a_monomials.items():
                if coeff:
                    ni, nj = (i + dx) % l, (j + dy) % l
                    x_stab.append(row_idx(ni, nj))
            # Column chain b^T shifts (vertical transpose)
            for (dx, dy), coeff in b_monomials.items():
                if coeff:
                    ni, nj = (i + dy) % l, (j + dx) % l  # Transpose mercy
                    x_stab.append(col_idx(ni, nj))
            Hx_rows[stab_idx] = x_stab
            
            # Z-stabilizer at plaquette (i,j): column chain b + row chain a^T
            z_stab = []
            for (dx, dy), coeff in b_monomials.items():
                if coeff:
                    ni, nj = (i + dx) % l, (j + dy) % l
                    z_stab.append(col_idx(ni, nj))
            for (dx, dy), coeff in a_monomials.items():
                if coeff:
                    ni, nj = (i + dy) % l, (j + dx) % l
                    z_stab.append(row_idx(ni, nj))
            Hz_rows[stab_idx + l*l] = z_stab
            
            stab_idx += 1
    
    # Build full matrices (dense for small l—sparse real impl)
    Hx = np.zeros((l*l, n), dtype=int)
    Hz = np.zeros((l*l, n), dtype=int)
    
    for idx, qubits in Hx_rows.items():
        for q in qubits:
            Hx[idx, q] = 1
    for idx, qubits in Hz_rows.items():
        for q in qubits:
            Hz[idx - l*l, q] = 1
    
    physical = n
    rate_est = (physical - Hx.shape[0] - Hz.shape[0]) / physical if physical > 0 else 0
    
    params = {
        "physical_qubits": physical,
        "x_stabilizers": l*l,
        "z_stabilizers": l*l,
        "rate_estimate": rate_est,
        "lattice_size": l
    }
    
    print(f"Full monomial bivariate bicycle qLDPC constructed immaculate—rate ~{rate_est:.3f}")
    return Hx, Hz, params

# Example small bicycle code (l=7 odd mercy, simple polynomials)
def demo_bivariate_bicycle(l=7):
    """Demo with simple monomials—1 + x + y for a, 1 + x^2 for b"""
    # a(x,y) = 1 + x + y
    a_monomials = {(0,0): 1, (1,0): 1, (0,1): 1}
    # b(x,y) = 1 + x^2
    b_monomials = {(0,0): 1, (2,0): 1}
    
    Hx, Hz, params = bivariate_bicycle_code(l, a_monomials, b_monomials)
    print(f"Demo params: {params}")
    return Hx, Hz, params

# Run demo
# demo_bivariate_bicycle(l=7)
