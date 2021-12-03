import numpy as np


def parseInput(file):
    with open(file, "r") as inputFile:
        inputData = np.array([[int(bit) for bit in bits] for bits in inputFile.read().split('\n')])
    return inputData


def mostCommon(input):
    return "".join([str(int(x>=0.5)) for x in np.mean(input, axis=0)])


def leastCommon(input):
    return "".join([str(int(x<0.5)) for x in np.mean(input, axis=0)])


def bitArrayToBinary(input):
    return int("".join([str(x) for x in input]), 2)


def part1(input):
    bitSize = len(input[0])

    gammaBinary = mostCommon(input)

    gamma = int(gammaBinary, 2)
    epsilon = (2**bitSize-1) - gamma

    return gamma * epsilon


def part2(input):
    bitSize = len(input[0])

    remainingCodes = input

    for bitPos in range(bitSize):
        mostCommonBit = mostCommon(remainingCodes)[bitPos]

        remainingCodes = [codes for codes in remainingCodes if mostCommonBit == str(codes[bitPos])]

        if len(remainingCodes) == 1:
            o2GenRating = bitArrayToBinary(remainingCodes[0])
            break


    remainingCodes = input

    for bitPos in range(bitSize):
        leastCommonBit = leastCommon(remainingCodes)[bitPos]

        remainingCodes = [codes for codes in remainingCodes if leastCommonBit == str(codes[bitPos])]

        if len(remainingCodes) == 1:
            co2Scubber = bitArrayToBinary(remainingCodes[0])
            break

    return o2GenRating*co2Scubber


def main():

    testInput = parseInput("./day03/test.txt")
    realInput = parseInput("./day03/input.txt")

    assert(part1(testInput)==198)

    result1 = part1(realInput)
    print(f"Part 1 solution: {result1}")

    assert(part2(testInput)==230)

    result2 = part2(realInput)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()