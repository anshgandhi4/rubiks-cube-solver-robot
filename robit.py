# import serial
# import time
#
# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)
#
# while True:
#     arduino.write(bytes(input("Input: ") + '\n', 'utf-8'))
#     time.sleep(0.05)
#     print(str(arduino.readline(), 'utf-8'))
