import numpy as np

def parseInput(file):
    with open(file, "r") as inputFile:
        inputData = [int(x) for x in inputFile.read().split('\n')]
    return inputData

def part1(input):
    depths = parseInput(input)

    prevDepth = depths[0]
    increaseCount = 0

    for depth in depths[1:]:
        if depth > prevDepth:
            increaseCount+=1
        prevDepth = depth
    
    return increaseCount



def part2(input):
    depths = parseInput(input)

    # Truncate first two and last two as they are partial windows
    slidingDepts = np.convolve(depths, np.ones(3, dtype=int))[2:-2]

    prevDepth = slidingDepts[0]
    increaseCount = 0

    for depth in slidingDepts[1:]:
        if depth > prevDepth:
            increaseCount+=1
        prevDepth = depth
    
    return increaseCount



def main():

    assert(part1("./day01/test.txt")==7)

    result1 = part1("./day01/input.txt")
    print(f"Part 1 solution: {result1}")

    assert(part2("./day01/test.txt")==5)

    result1 = part2("./day01/input.txt")
    print(f"Part 2 solution: {result1}")


if __name__ == "__main__":
    main()