import numpy as np


def parseInput(file):

    with open(file, "r") as inputFile: 
        lines = []
        for count, line in enumerate(inputFile):
            rawPoints = line.split(' -> ')

            lines.append([parsePoint(x) for x in rawPoints])

    return lines


def parsePoint(point):
    arrPoint = point.split(',')
    return (int(arrPoint[0]), int(arrPoint[1]))


def numVents(fieldArray):
    return (fieldArray >= 2).sum()


def part1(input):
    ventField = np.zeros((1000,1000))

    for line in input:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if (x1==x2) or (y1==y2):
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    ventField[x,y] += 1

    return numVents(ventField)
    

def part2(input):
    ventField = np.zeros((1000,1000))

    for line in input:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if (x1==x2) or (y1==y2):
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    ventField[x,y] += 1
        else:
            if x1 > x2:
                temp = x1
                x1 = x2
                x2 = temp
                temp = y1
                y1 = y2
                y2 = temp
            
            for i, x in enumerate(range(x1, x2+1)):
                if y2 > y1:
                    ventField[x,y1+i] += 1
                if y2 < y1:
                    ventField[x,y1-i] += 1


    return numVents(ventField)


def main():

    testInput = parseInput("./day05/test.txt")
    realInput = parseInput("./day05/input.txt")


    assert(part1(testInput)==5)

    result1 = part1(realInput)
    print(f"Part 1 solution: {result1}")

    assert(part2(testInput)==12)

    result2 = part2(realInput)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()