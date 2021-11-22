# define function printlines

def printlines(linelist):
    for i, aline in enumerate(linelist):
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" % (i, aline[0], aline[1], aline[2], aline[3]))


# define function plotshift

def plotshift(linelist, xshift=0, yshift=0):
    # shift each line
    for i in range(len(linelist)):
        # shift x
        for j in range(0, 3, 2):
            linelist[i][j] += xshift
        # shift y
        for k in range(1, 4, 2):
            linelist[i][k] += yshift
    return linelist


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

# input shift
line2 = input()
shift = line2.split(",")
for i in range(len(shift)):
    shift[i] = float(shift[i])

x = shift[0]
y = shift[1]


#### call functions
# call plotshift to shift figures
fig2 = plotshift(list_lines, x, y)

# call printlines to draw figures
printlines(fig2)
