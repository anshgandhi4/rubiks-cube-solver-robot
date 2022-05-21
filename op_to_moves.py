from util import reverse

corner_setups = {
    'A': None,
    'B': "R2",
    'C': "R2 D'",
    'D': "F2",
    'E': None,
    'F': "F' D",
    'G': "F'",
    'H': "D' R",
    'I': "F R'",
    'J': "R'",
    'K': "R' D'",
    'L': "F2 R'",
    'M': "F",
    'N': "R' F",
    'O': "R2 F",
    'P': "F D",
    'Q': "R D'",
    'R': None,
    'S': "D F'",
    'T': "R",
    'U': "D",
    'V': "",
    'W': "D'",
    'X': "D2"
}
edge_setups = {
    'A': "R2 U' R2",
    'B': None,
    'C': "R2 U R2",
    'D': "",
    'E': "L' U B' U'",
    'F': "U' F U",
    'G': "D F L' F'",
    'H': "U B' U'",
    'I': "R F' L' R'",
    'J': "U2 R U2",
    'K': "F L' F'",
    'L': "L'",
    'M': None,
    'N': "U B U'",
    'O': "D' F L' F'",
    'P': "U' F' U",
    'Q': "R' B L R",
    'R': "L",
    'S': "D2 F L' F'",
    'T': "U2 R' U2",
    'U': "D' L2",
    'V': "D2 L2",
    'W': "D L2",
    'X': "L2"
}

def gen_corner_moves(positions):
    y_perm = " (R U' R' U' R U R' F' R U R' U' R' F R) "
    output = ''
    for position in positions:
        output += corner_setups[position] + y_perm + reverse(corner_setups[position]) + '\n'
    return output

def gen_parity(corner_positions, edge_positions):
    r_perm = "(R U R' F' R U2 R' U2 R' F R U R U2 R' U')\n"
    return r_perm if len(corner_positions) % 2 == 1 and len(edge_positions) % 2 == 1 else ''

def gen_edge_moves(positions):
    t_perm = " (R U R' U' R' F R2 U' R' U' R U R' F') "
    output = ''
    for position in positions:
        output += edge_setups[position] + t_perm + reverse(edge_setups[position]) + '\n'
    return output

def generate_solution(corner_positions, edge_positions):
    solution = gen_corner_moves(corner_positions) + '\n\n' + gen_parity(corner_positions, edge_positions) + '\n\n' + gen_edge_moves(edge_positions)
    return solution if solution != '' else 'Already Solved!'
