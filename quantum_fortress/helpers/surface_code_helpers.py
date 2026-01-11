# Helper function for surface code decoder
# Converts support edge (two plaquette defect positions) to data qubit flips on Manhattan path
# Assumes rotated or standard surface code grid:
# - Plaquette defects at integer coordinates (x, y) from 0 to d
# - Data qubits at integer (row, col) from 0 to d-1, 0 to d-1
# - Horizontal path between (x, y) and (x, y+k): flips data qubits (x, y) to (x, y+k-1)
# - Vertical path between (x, y) and (x+k, y): flips data qubits (x, y) to (x+k-1, y)
# Path: Horizontal first, then vertical (or vice versa—shortest Manhattan)

def edge_to_qubits(edge, distance):
    """
    Convert edge between two defect plaquettes to list of data qubit positions on Manhattan path
    edge: tuple or frozenset of two defect positions ((x1,y1), (x2,y2))
    distance: code distance d (for bounds check)
    Returns: list of (row, col) data qubit tuples to flip (Z correction)
    """
    (x1, y1), (x2, y2) = sorted(edge)  # Ensure (x1,y1) <= (x2,y2) for simplicity
    if x1 > x2 or (x1 == x2 and y1 > y2):
        (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
    
    qubits = []
    
    # Horizontal move first: fix y, move x from x1 to x2
    if x1 != x2:
        for x in range(x1, x2):  # Data qubits between plaquettes x to x+1
            qubits.append((x, y1))  # Horizontal data qubit at row x, col y1
    
    # Vertical move: fix x (now x2), move y from y1 to y2
    if y1 != y2:
        for y in range(y1, y2):  # Data qubits between plaquettes y to y+1
            qubits.append((x2 - 1 if x1 != x2 else x1, y))  # Vertical at final x, cols y to y+1
    
    # Bounds mercy—filter valid data qubits (0 to d-1)
    valid_qubits = [(r, c) for r, c in qubits if 0 <= r < distance and 0 <= c < distance]
    
    return valid_qubits

# Example usage in decoder peeling
# for edge in path_edges:  # path_edges from Dijkstra as frozenset pairs
#     flips = edge_to_qubits(edge, distance)
#     for qubit in flips:
#         correction[qubit] ^= 1
