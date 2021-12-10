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


def countPoints(floor, visited, i, j):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    # if we've been here, or it's a 9, leave and don't count
    if visited[i,j] or (floor[i,j] == 9):
        return 0, visited

    visited[i][j] = True
    count = 1

    # go in our 4 directions and check those points to see if they can be included
    for direction in directions:
        points, visited = countPoints(floor, visited,i+direction[0], j+direction[1])
        count += points

    return count, visited


def countBasins(floor):
    basinSizes = []
    basinCount = 0

    # we need to know where we've been
    visited = np.zeros(floor.shape, dtype=bool)

    # walk through our floor
    for i in range(1, floor.shape[0] - 1):
        for j in range(1, floor.shape[1] - 1 ):
            
            # if we haven't been here and it's not a 9, count it as a basin and 
            # start traversing the nearby points
            if floor[i,j] != 9 and not visited[i,j]:
                basinCount += 1
                basinSize, visited = countPoints(floor, visited, i, j)
                basinSizes.append(basinSize)

    return basinSizes


def part2(floor):
    sizes = countBasins(floor)

    return (np.prod(sorted(sizes, reverse=True)[:3]))


def main():

    testFloor = parseInput("./day09/test.txt")
    inputFloor = parseInput("./day09/input.txt")

    assert(part1(testFloor)==15)

    result1 = part1(inputFloor)
    print(f"Part 1 solution: {result1}")

    assert(part2(testFloor)==1134)

    result2 = part2(inputFloor)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()