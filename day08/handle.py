import numpy as np


SEVENSEGMAP = {0:"abcefg", 1:"cf", 2:"acdeg", 3:"acdfg", 4:"bcdf", 5:"abdfg", 6:"abdefg", 7:"acf", 8:"abcdefg", 9:"abcdfg"}

def parseInput(file):
    with open(file, "r") as inputFile: 
        lines = []
        for _, line in enumerate(inputFile):
            codes = line.strip().split(' | ')

            signal = codes[0].split(' ')
            output = codes[1].split(' ')

            lines.append({"signals":signal, "output":output})

    return lines


def part1(codes):
    numUniqueSegments = 0
    for line in codes:
        for code in line["output"]:
            if len(code) in [2, 3, 4, 7]:
                numUniqueSegments += 1

    return numUniqueSegments


def codesByLen(codes):
    lenDict = {}
    for code in codes:
        if len(code) in lenDict:
            lenDict[len(code)].append(code)
        else:
            lenDict[len(code)] = [code]

    return lenDict


def decryptCodes(lenCodes):
    decrypted = {}

    # Unique lengths we know
    decrypted[1] = ''.join(sorted(lenCodes[2][0]))
    decrypted[4] = ''.join(sorted(lenCodes[4][0]))
    decrypted[7] = ''.join(sorted(lenCodes[3][0]))
    decrypted[8] = ''.join(sorted(lenCodes[7][0]))


    # Lets start with 0, 6, 9 (segment length of 6)
    for code in lenCodes[6]:
        # 0, 9 have both segments in the 1, but 6 does not
        if all(x in code for x in decrypted[1]):
            # 9 has all the segments that are in 4, but 0 does not
            if all(x in code for x in decrypted[4]):
                decrypted[9] = ''.join(sorted(code))
            else:
                decrypted[0] =  ''.join(sorted(code))
        else:
            decrypted[6] = ''.join(sorted(code))

    #  Now lets find 2, 3, 5 (segment length of 5)
    for code in lenCodes[5]:
        # Only 3 has both segments in the 1
        if all(x in code for x in decrypted[1]):
            decrypted[3] = ''.join(sorted(code))
        else:
            # 5 has 3 of the same segments as 4, but 2 only shares 2 segments with 4
            if sum(x in code for x in decrypted[4]) == 3:
                decrypted[5] = ''.join(sorted(code))
            else: 
                decrypted[2] = ''.join(sorted(code))

    # reverse the map to make lookup easy
    return {v: k for k, v in decrypted.items()}


def part2(codes):

    sum = 0

    for code in codes:
        lenCodes = codesByLen(code['signals'])
        decryption = decryptCodes(lenCodes)
        
        outputNum = ''
        for outputCode in code['output']:
            outputNum += str(decryption[''.join(sorted(outputCode))])

        sum += int(outputNum)

    return sum


def main():

    testCodes = parseInput("./day08/test.txt")
    inputCodes = parseInput("./day08/input.txt")

    assert(part1(testCodes)==26)

    result1 = part1(inputCodes)
    print(f"Part 1 solution: {result1}")

    assert(part2(testCodes)==61229)

    result2 = part2(inputCodes)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()