# def function
def plotmirror(linelist, horv="h", loc=0):
    afigure = list()
    # each line
    for i in linelist:
        x1 = i[0]
        y1 = i[1]
        x2 = i[2]
        y2 = i[3]

        if horv == "h":
            y = loc
            if y1 >= y and y2 >= y:
                newline = [x1, y1 - 2 * (y1 - y), x2, y2 - 2 * (y2 - y)]
            elif y1 >= y and y2 < y: 
                newline = [x1, y1 - 2 * (y1 - y), x2, y2 + 2 * (y - y2)]                
            elif y1 < y and y2 >= y:
                newline = [x1, y1 + 2 * (y - y1), x2, y2 - 2 * (y2 - y)]
            elif y1 < y and y2 < y:
                newline = [x1, y1 + 2 * (y - y1), x2, y2 + 2 * (y - y2)]
            afigure.append(newline)
        elif horv == "v":
            x = loc
            if x1 >= x and x2 >= x:
                newline = [x1 - 2 * (x1 - x), y1, x2 - 2 * (x2 - x), y2]
            elif x1 >= x and x2 < x: 
                newline = [x1 - 2 * (x1 - x), y1, x2 + 2 * (x - x2), y2]                
            elif x1 < x and x2 >= x:
                newline = [x1 + 2 * (x - x1), y1, x2 - 2 * (x2 - x), y2]
            elif x1 < x and x2 < x:
                newline = [x1 + 2 * (x - x1), y1, x2 + 2 * (x - x2), y2]
            afigure.append(newline)
    return afigure


# define function printlines

def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))


# input lines unti "LINESTOP"
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

line2 = input()
horv_input = line2.split(",")[0]
loc_input = float(line2.split(",")[1])

printlines(plotmirror(linelist=list_lines, horv=horv_input, loc=loc_input))