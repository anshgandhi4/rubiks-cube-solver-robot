from vision import scan_cube
from op import op_corners, op_edges
from op_to_moves import generate_solution
import kociemba

# inp = 'WBWRWOORRBGGORBBBRYWYWGYOROGGWYYWWRGBYBGOOOGYRORYBWYBG'
inp = input('Cube State: ')
if len(inp) != 54:
    inp = scan_cube()
    print(inp)
else:
    inp = inp.upper()

out = input('Final Cube State: ')
if len(out) != 54:
    out = 'WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB'
    print(out)
else:
    out = out.upper()

alg = input('Kociemba (K) / Old Pochmann (OP): ')
print('Solution:')
if alg.upper() == 'K':
    print(kociemba.solve(inp.replace('G', 'F').replace('O', 'L').replace('W', 'U').replace('Y', 'D')))
else:
    print(generate_solution(op_corners(inp, out), op_edges(inp, out)))
