#!/usr/bin/python
# just to be able to run it directly,
# interpreted as a comment when run as 
# 'python graphreader.py'

from PIL import Image, ImageDraw
import numpy as np
import argparse

parser = argparse.ArgumentParser(description = "A very, VERY primitive command-line tool for reading data from images of graphs.")

parser.add_argument('-f', metavar='FILE', type=str, help='image file name')
parser.add_argument('-F', metavar='FORMAT', type=str, default='Pair: ({0}, {1})', help='result output fromat. {0} for X, {1} for Y.')
parser.add_argument('-t', metavar='THESHOLD', type=int, default=50, help='threshold at witch graph line is reconized')
parser.add_argument('-x1', metavar='X1', type=float, default=0, help='X range beginning')
parser.add_argument('-x2', metavar='X2', type=float, default=1, help='X range end')
parser.add_argument('-y1', metavar='Y1', type=float, default=0, help='Y range beginning')
parser.add_argument('-y2', metavar='Y2', type=float, default=1, help='Y range end')
parser.add_argument('-i', action='store_const', const=True, default=False, help='inverse image')

args = parser.parse_args()
print("Image file: ", args.f)

threshold = args.t

image = Image.open(args.f).convert('L')
image = np.array(image)

print("Image loaded. Processing...")

per = 0

for i in range(0, len(image)):
    if (int(i * 1.0 / len(image) * 10) > per):
        per = int(i * 1.0 / len(image) * 10)
        print(per * 10, "%")
    for j in range(0, len(image[i])):
        if (args.i and image[i][j] >= threshold) or ((not args.i) and image[i][j] < threshold):
            image[i][j] = 0
        else:
            image[i][j] = 255

print("Done!")

print("x range: [", args.x1, "; ", args.x2, "]")
print("y range: [", args.y1, "; ", args.y2, "]")

while 1:
    print("Enter x value ('q' to exit): ")
    xval = input()
    if xval == 'q':
        break

    xval = float(xval)
    xval_p = (xval - args.x1) / (args.x2 - args.x1)
    xval_i = int(xval_p * (len(image[0]) - 1))

    image2 = np.copy(image)

    yval_i = -1
    for y in range(0, len(image)):
        if image[y][xval_i] == 0:
            yval_i = y
            break
        image2[y][xval_i] = 0

    im2 = Image.fromarray(image2, 'L')
    im2.save('temp.png')

    if yval_i == -1:
        print("Not found!")
        continue
    yval = (yval_i * 1.0 / len(image)) * (args.y1 - args.y2) + args.y2

    print(args.F.format(xval, yval))
