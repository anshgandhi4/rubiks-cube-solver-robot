import solver as sv
from util import simplify
from vision import scan_cube

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

solution = sv.solve(inp.replace('G', 'U').replace('O', 'L').replace('W', 'X').replace('Y', 'F').replace('B', 'D').replace('X', 'B'), 18, 2)
solution = simplify(solution.replace('D', 'B').replace('F', 'D').replace('U', 'F'))
print('Solution: ' + solution)
