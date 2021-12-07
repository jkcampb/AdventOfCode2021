import numpy as np


def parseInput(file):
    with open(file, "r") as inputFile:
        inputData = [int(fish) for fish in inputFile.read().split(',')]
    return np.array(inputData)


def part1(crabs):

    minFuel = crabs.max() * len(crabs)
    for position in range(crabs.min(),crabs.max()):
        fuel = np.absolute(crabs - position).sum()
        if fuel < minFuel:
            minFuel = fuel

    return minFuel


def part2(crabs):

    minFuel = sumOfWholeNums(crabs.max()) * len(crabs)
    for position in range(crabs.min(),crabs.max()):
        distances = np.absolute(crabs - position)
        fuel = np.array(list(map(sumOfWholeNums, distances))).sum()
        if fuel < minFuel:
            minFuel = fuel

    return minFuel


def sumOfWholeNums(x):
    return int(x*(x+1)/2)


def main():

    testCrabs = parseInput("./day07/test.txt")
    inputCrabs = parseInput("./day07/input.txt")

    assert(part1(testCrabs)==37)

    result1 = part1(inputCrabs)
    print(f"Part 1 solution: {result1}")


    assert(part2(testCrabs)==168)

    result2 = part2(inputCrabs)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()