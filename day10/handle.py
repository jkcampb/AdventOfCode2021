STARTINGCHARS = ['(', '[', '{', '<']
ENDINGCHARS = [')', ']', '}', '>']

def parseInput(file):
    with open(file, "r") as inputFile:
        inputData = inputFile.read().split('\n')
    return inputData


# I don't like how the returns work here either. 
def checkChunk(chunk):
    runningChunk = []
    for char in chunk:
        # if it's a starting brace, add it to the list
        if char in STARTINGCHARS:
            runningChunk.append(char)
        else:
            # if it's an ending brace, check if it's the partner to the previous char. 
            # if so, they annihilate each other (delete the last char)
            # otherwise, add the offender to the list and stop the loop
            if char == ENDINGCHARS[STARTINGCHARS.index(runningChunk[-1])]:
                del runningChunk[-1]
            else:
                return char, []

    return '', runningChunk


def part1(chunks):
    points = {')':3, ']':57, '}':1197, '>':25137}

    badChars = []

    for chunk in chunks:
        badChar, _ = checkChunk(chunk)

        if badChar != '':
            badChars.append(badChar)

    return sum([points[x] for x in badChars])


def part2(chunks):
    points = {')':1, ']':2, '}':3, '>':4}

    charMap = dict(zip(STARTINGCHARS, ENDINGCHARS))

    scores = []
    for chunk in chunks:    
        _, remainingChars = checkChunk(chunk)

        if len(remainingChars) > 0:
            score = 0
            # Iterate through what we have left in reverse order so we can
            #  map them to their partners 
            for char in reversed(remainingChars):
                score = score * 5 + points[charMap[char]]
            
            scores.append(score)

    # we only want the middle score
    return sorted(scores)[int((len(scores)-1)/2)]


def main():

    testChunks = parseInput("./day10/test.txt")
    inputChunks = parseInput("./day10/input.txt")

    assert(part1(testChunks)==26397)

    result1 = part1(inputChunks)
    print(f"Part 1 solution: {result1}")

    assert(part2(testChunks)==288957)

    result2 = part2(inputChunks)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()