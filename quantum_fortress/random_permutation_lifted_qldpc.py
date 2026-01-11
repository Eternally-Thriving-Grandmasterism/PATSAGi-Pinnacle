# quantum_fortress/random_permutation_lifted_qldpc.py
# Random Permutation Lifted Product qLDPC Code Construction + Girth Check
# Lift small CSS protograph over random permutations for expansion mercy
# Now with girth computation on Tanner graph—high girth abundance supreme
# Girth: Shortest cycle length (BFS from each node mercy)
# Coforged Holy Trinity - MIT Eternal Thriving Abundance Supreme

import numpy as np
import random  # Grace RNG for permutation lifts mercy
from itertools import permutations  # Full S_m small m
from collections import deque  # BFS mercy for girth

def random_permutation_lifted_qldpc(proto_Hx, proto_Hz, lift_size_m, seed=None):
    # ... (unchanged construction from previous—Hx_big, Hz_big built)
    # Returns Hx_big, Hz_big, params as before

    # Add girth check on combined Tanner graph
    girth = compute_tanner_girth(Hx_big, Hz_big)
    params["tanner_girth"] = girth
    print(f"Girth check complete: Shortest cycle {girth} —abundance mercy supreme!")
    
    return Hx_big, Hz_big, params

def compute_tanner_girth(Hx, Hz):
    """
    Compute girth of Tanner graph for CSS code (Hx X-stabs, Hz Z-stabs)
    Bipartite: Variable nodes + check nodes (X + Z checks)
    Edges from H=1
    BFS from each variable node—shortest back-to-self cycle mercy
    Returns: Minimum cycle length (or inf if tree-like)
    """
    rows_x, cols = Hx.shape
    rows_z, _ = Hz.shape
    n_vars = cols
    n_checks = rows_x + rows_z
    
    # Build adjacency list: var_nodes 0..n_vars-1 → check_nodes n_vars..n_vars+n_checks-1
    adj = [[] for _ in range(n_vars + n_checks)]
    
    # X-checks: 0 to rows_x-1 → offset n_vars
    for check in range(rows_x):
        check_node = n_vars + check
        for var in range(n_vars):
            if Hx[check, var]:
                adj[var].append(check_node)
                adj[check_node].append(var)
    
    # Z-checks: rows_x to rows_x+rows_z-1 → offset n_vars + rows_x
    for check in range(rows_z):
        check_node = n_vars + rows_x + check
        for var in range(n_vars):
            if Hz[check, var]:
                adj[var].append(check_node)
                adj[check_node].append(var)
    
    min_girth = float('inf')
    
    # BFS from each variable node—find shortest cycle
    for start_var in range(n_vars):
        # Distance and parent for backedge detection
        dist = [-1] * (n_vars + n_checks)
        dist[start_var] = 0
        parent = [-1] * (n_vars + n_checks)
        q = deque([start_var])
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:  # First visit
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                elif v != parent[u]:  # Backedge—cycle!
                    cycle_len = dist[u] + dist[v] + 1
                    if cycle_len < min_girth:
                        min_girth = cycle_len
    
    return min_girth if min_girth != float('inf') else "Tree-like (no cycles mercy!)"

# Updated demo with girth
def demo_random_lift(m=5):
    """Demo with girth check mercy"""
    random.seed(42)
    
    # Small proto CSS example
    proto_Hx = np.array([[1,1,0,0,1,0,0,0],
                         [0,0,1,1,0,1,0,0],
                         [0,0,0,0,0,0,1,1]])
    proto_Hz = np.array([[1,0,1,0,1,0,1,0],
                         [0,1,0,1,0,1,0,1]])
    
    Hx_big, Hz_big, params = random_permutation_lifted_qldpc(proto_Hx, proto_Hz, m)
    print(f"Demo params with girth: {params}")
    return Hx_big, Hz_big, params

# Run demo
# demo_random_lift(m=5)                perm = edge_perms_z[(proto_row, proto_col)]
                for k in range(lift_size_m):
                    big_row = proto_row * lift_size_m + k
                    big_col = proto_col * lift_size_m + perm[k]
                    Hz_big[big_row, big_col] = 1
    
    physical = n_big
    rate_est = (physical - m_big_x - m_big_z) / physical if physical > 0 else 0
    
    params = {
        "physical_qubits": physical,
        "lift_factor": lift_size_m,
        "rate_estimate": rate_est,
        "lift_type": "random_permutation (full S_m small m, shuffle approx large)"
    }
    
    print(f"Random permutation lifted qLDPC constructed immaculate—rate ~{rate_est:.3f}, lift m={lift_size_m}")
    return Hx_big, Hz_big, params

# Example small random lift demo
def demo_random_lift(m=5):
    """Demo with tiny proto + random permutation lift mercy"""
    random.seed(42)
    
    # Small proto CSS example
    proto_Hx = np.array([[1,1,0,0,1,0,0,0],
                         [0,0,1,1,0,1,0,0],
                         [0,0,0,0,0,0,1,1]])
    proto_Hz = np.array([[1,0,1,0,1,0,1,0],
                         [0,1,0,1,0,1,0,1]])
    
    Hx_big, Hz_big, params = random_permutation_lifted_qldpc(proto_Hx, proto_Hz, m)
    print(f"Demo params: {params}")
    return Hx_big, Hz_big, params

# Run demo
# demo_random_lift(m=5)
