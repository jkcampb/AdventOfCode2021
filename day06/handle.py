import copy

def parseInput(file):
    with open(file, "r") as inputFile:
        inputData = [int(fish) for fish in inputFile.read().split(',')]
    return inputData


def part1(fish, days):

    lanternFish = copy.deepcopy(fish)

    for day in range(days):
        newFish = 0
        for i, fishState in enumerate(lanternFish):
            if fishState == 0:
                lanternFish[i] = 6
                newFish += 1
            else:
                lanternFish[i]-=1
        lanternFish.extend([8] * newFish)

    return len(lanternFish)
    

def part2(fish, days):
    fishCounts = dict()

    # Initialize fish counter (key is fish timer, value is num of fish)
    for fishTimer in range(9):
        fishCounts[fishTimer] = 0
    for i in fish:
        fishCounts[i] = fishCounts.get(i, 0) + 1

    for _ in range(days):
        tempFish = copy.deepcopy(fishCounts)
        for fishTimer in range(1, 9):
            fishCounts[fishTimer-1] = tempFish[fishTimer]

        #Fish at 0 reset to 6 and make a new fish at 8
        fishCounts[6] += tempFish[0]
        fishCounts[8] = tempFish[0]

    totalFish = 0
    for _, v in fishCounts.items():
        totalFish += v

    return totalFish


def main():

    testFish = parseInput("./day06/test.txt")
    inputFish = parseInput("./day06/input.txt")

    assert(part1(testFish,18)==26)

    assert(part1(testFish,80)==5934)

    result1 = part1(inputFish, 80)
    print(f"Part 1 solution: {result1}")


    assert(part2(testFish,18)==26)
    assert(part2(testFish, 256)==26984457539)

    result2 = part2(inputFish, 256)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()