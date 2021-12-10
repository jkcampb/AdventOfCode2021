import numpy as np

def parseInput(file):
    with open(file, "r") as inputFile: 
        floor = []
        for _, line in enumerate(inputFile):
            # add a buffer edge to avoid boundary issues
            floorLine = [9]
            floorLine.extend([int(x) for x in line.strip()])
            floorLine.extend([9])

            floor.append(floorLine)

    topBottom = [9] * len(floorLine)

    floor.insert(0, topBottom)
    floor.append(topBottom)
    
    return np.array(floor)

def part1(floor):

    riskLevel = 0
    for x in range(1, floor.shape[0]-1):
        for y in range(1, floor.shape[1] -1):
            if floor[x, y] < min(floor[x-1, y], floor[x+1, y], floor[x, y-1], floor[x, y+1]):
                riskLevel += (floor[x,y] +1)

    return riskLevel


def main():

    testFloor = parseInput("./day09/test.txt")
    inputFloor = parseInput("./day09/input.txt")

    assert(part1(testFloor)==15)

    result1 = part1(inputFloor)
    print(f"Part 1 solution: {result1}")

    # assert(part2(testFloor)==1134)

    # result2 = part2(inputFloor)
    # print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()