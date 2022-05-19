import cv2
import numpy as np

cube_width = 3
width_pixels = cube_width*3
hsvColors = {'B': [[0, 100, 100], [30, 255, 255]],
             'G': [[30, 100, 100], [75, 255, 255]],
             'R': [[118, 120, 120], [140, 255, 255]],
             'O': [[100, 120, 120], [118, 255, 255]],
             'W': [[0, 0, 75], [180, 45, 255]],
             'Y': [[75, 100, 100], [100, 255, 255]]}
rgbColors = {'B': (255, 0, 0),
             'G': (0, 255, 0),
             'R': (0, 0, 255),
             'O': (0, 125, 255),
             'W': (255, 255, 255),
             'Y': (0, 255, 255)}

data = [['' for i in range(width_pixels)] for j in range(width_pixels)]

img = cv2.imread('amogusmod.png', cv2.IMREAD_COLOR)
print(img.shape)
width = img.shape[1]
height = img.shape[0]
if height > width:
    cropped = img[:width, :width]
elif width > height:
    cropped = img[:height, :height]
else:
    cropped = img
print(cropped.shape)

hsv = cv2.cvtColor(cropped, cv2.COLOR_RGB2HSV)
pixels = cropped.copy()
line_interval = round(cropped.shape[0] / width_pixels)
print(line_interval)
print()

for i in range(width_pixels):
    for j in range(width_pixels):
        x = i * line_interval
        y = j * line_interval

        bestColor = 'W'
        bestValue = 0
        for key in ['B', 'G', 'R', 'O', 'W', 'Y']:
            color = hsvColors[key]
            in_range = cv2.inRange(hsv[x: x + line_interval, y: y + line_interval], np.array(color[0]), np.array(color[1]))
            avg = np.average(in_range)
            if avg > bestValue:
                bestValue = avg
                bestColor = key
        # print(bestColor)
        data[i][j] = bestColor
        pixels[x: x + line_interval, y: y + line_interval] = rgbColors[bestColor]

for i in range(width_pixels+1):
    thick = 5 if i % cube_width == 0 else 1
    x = i * line_interval
    cv2.line(pixels, (x, 0), (x, height), (0, 0, 0), thickness=thick)
    cv2.line(pixels, (0, x), (height, x), (0, 0, 0), thickness=thick)

print(data)
# cv2.imshow('img', cropped)
cv2.imshow('img2', pixels)
cv2.waitKey(0)
