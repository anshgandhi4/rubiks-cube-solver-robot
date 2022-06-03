import cv2
import numpy as np

blue = green = red = orange = white = yellow = 0
hsvColors = {'B': [blue, [0, 100, 100], [30, 255, 255]],
             'G': [green, [30, 100, 100], [75, 255, 255]],
             'R': [red, [118, 120, 120], [140, 255, 255]],
             'O': [orange, [100, 120, 120], [118, 255, 255]],
             'W': [white, [0, 0, 75], [180, 45, 255]],
             'Y': [yellow, [75, 100, 100], [100, 255, 255]]}
rgbColors = {'B': (255, 0, 0),
             'G': (0, 255, 0),
             'R': (0, 0, 255),
             'O': (0, 125, 255),
             'W': (255, 255, 255),
             'Y': (0, 255, 255)}
data = [['' for i in range(9)] for j in range(6)]

def nothing(para):
    pass

def scan_cube():
    print(' U\nLFRB\n D\nURFDLB')
    output = ''
    cv2.namedWindow('Selection')
    cv2.createTrackbar('Selection', 'Selection', 0, 6, nothing)
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    scan = True

    while scan:
        img = cam.read()[1]
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        for i in range(0, 3):
            for j in range(0, 3):
                x = 240 + 120 * j
                y = 105 + 120 * i
                bestColor = 'W'
                bestValue = 0
                for key in ['B', 'G', 'R', 'O', 'W', 'Y']:
                    color = hsvColors[key]
                    color[0] = cv2.inRange(hsv[y - 60: y + 60, x - 60: x + 60], np.array(color[1]), np.array(color[2]))
                    cv2.morphologyEx(color[0], cv2.MORPH_OPEN, (1, 1), color[0])
                    cv2.morphologyEx(color[0], cv2.MORPH_CLOSE, (1, 1), color[0])
                    avg = np.average(color[0])
                    if avg > bestValue:
                        bestValue = avg
                        bestColor = key

                selection = cv2.getTrackbarPos('Selection', 'Selection')
                if selection != 6:
                    data[selection][3 * i + j] = bestColor
                    cv2.rectangle(img, (x - 57, y - 57), (x + 57, y + 57), rgbColors[bestColor], 3)
                    img[y - 57: y + 57, x - 57: x + 57] = cv2.addWeighted(img[y - 57: y + 57, x - 57: x + 57], 0.4, np.full((114, 114, 3), rgbColors[bestColor], dtype = np.uint8), 0.6, 0)
                else:
                    output = ''
                    for face in range(6):
                        output += ''.join(data[face])
                    scan = False

        cv2.imshow('Rubik\'s Cube Test', img)
        cv2.waitKey(1)

    cam.release()
    cv2.destroyAllWindows()

    return output
