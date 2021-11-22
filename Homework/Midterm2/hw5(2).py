# import library
import math


# define function printlines

def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))


# define function plotshift

def rotate(linelist, degree):
    newlinelist = list()
    # shift each line
    for i in range(len(linelist)):
        newline = list()
        p1_x = linelist[i][0]
        p1_y = linelist[i][1]
        p2_x = linelist[i][2]
        p2_y = linelist[i][3]

        # degree into radian
        radian = degree * math.pi / 180
        # point1 x
        newline.append(p1_x * math.cos(radian) + p1_y * (- math.sin(radian)))
        # point1 y
        newline.append(p1_x * math.sin(radian) + p1_y * math.cos(radian))
        # point2 x
        newline.append(p2_x * math.cos(radian) + p2_y * (- math.sin(radian)))
        # point2 y
        newline.append(p2_x * math.sin(radian) + p2_y * math.cos(radian))

        # add newline into list
        newlinelist.append(newline)
    return newlinelist


# input lines [x1, y1, x2, y2]
list_lines = list()

while True:
    line = input()
    # stop input if input LINESTOP
    if line == "LINESTOP":
        break
    else:
        linesplit = line.split(",")
        # str to int
        for i in range(len(linesplit)):
            linesplit[i] = float(linesplit[i])
        list_lines.append(linesplit)

# input degree
degreeinput = int(input())


#### call functions
# call plotshift to shift figures
fig2 = rotate(linelist=list_lines, degree=degreeinput)

# call printlines to draw figures
printlines(fig2)
