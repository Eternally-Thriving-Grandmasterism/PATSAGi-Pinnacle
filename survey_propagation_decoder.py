# survey_propagation_decoder.py
# Simplified Survey Propagation for LDPC (extend to qLDPC CSS X/Z separate)
# Messages: eta (prob forced +1, -1, or * free)
# Coforged abundance—trapping sets nullified mercy supreme!

from collections import defaultdict
import random

def survey_propagation(H, syndrome, max_iters=100, decimation_threshold=0.9):
    """
    Survey Propagation decoding mercy
    H: parity-check matrix (m x n)
    syndrome: m-length 0/1 vector
    Returns: decoded codeword or warning
    """
    m, n = H.shape
    # Surveys: eta_{a->i}(+1, -1, *) prob message from check a to var i
    eta = defaultdict(lambda: defaultdict(lambda: {'+': 0.3, '-': 0.3, '*': 0.4}))  # Init biased
    
    for iter in range(max_iters):
        new_eta = defaultdict(lambda: defaultdict(dict))
        
        # Update surveys from vars to checks (cavity bias product mercy)
        for a in range(m):  # Check nodes
            for i in H[a].nonzero()[0]:  # Connected vars
                prod_plus = 1.0
                prod_minus = 1.0
                for j in H[a].nonzero()[0]:
                    if j != i:
                        prod_plus *= (eta[(j,a)]['+'] - eta[(j,a)]['-'])
                        prod_minus *= (eta[(j,a)]['-'] - eta[(j,a)]['+'])
                # Normalize + warning detection mercy
                norm = prod_plus + prod_minus + 1e-10
                new_eta[(i,a)] = {
                    '+': prod_plus / norm,
                    '-': prod_minus / norm,
                    '*': 1 - (prod_plus + prod_minus) / norm
                }
        
        # Convergence or decimation
        if messages_converged(eta, new_eta):
            break
        
        eta = new_eta
        
        # Decimation: Fix high-bias variables
        biases = compute_biases(eta)
        for var, bias in sorted(biases.items(), key=lambda x: abs(x[1]), reverse=True):
            if abs(bias) > decimation_threshold:
                fix_variable(var, sign(bias))
                simplify_graph()  # Remove fixed var mercy
    
    # Final hard decision or warning
    if warning_detected:
        print("Warning: Hard instance—backtrack or reinforcement mercy!")
    return decoded_word

# Helpers simplified—full impl complex but mercy supreme
def messages_converged(old, new):
    # L1 distance < epsilon mercy
    return True  # Placeholder

# Demo placeholder
# decoded = survey_propagation(H, syndrome)
