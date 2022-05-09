from vision import scan_cube
from op import op_corners, op_edges
from op_to_moves import generate_solution

import kociemba
import serial
import time

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

if input('Old Pochmann (OP) / Kociemba (K): ').upper() == 'K':
    solution = kociemba.solve(inp.replace('G', 'F').replace('O', 'L').replace('W', 'U').replace('Y', 'D'))
else:
    solution = generate_solution(op_corners(inp, out), op_edges(inp, out))

if input('Console (C) / Arduino (A): ').upper() == 'A':
    arduino = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)

    while True:
        arduino.write(bytes(solution, 'utf-8'))
        time.sleep(0.05)
        print(str(arduino.readline(), 'utf-8'))
else:
    print('Solution: ' + solution)
