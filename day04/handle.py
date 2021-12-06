import numpy as np
import numpy.ma as ma


def parseInput(file):
    bingoNumbers = []
    bingoBoards = []
    with open(file, "r") as inputFile: 
        bingoBoard = []
        for count, line in enumerate(inputFile):
            if count == 0:
                bingoNumbers.extend([int(x) for x in line.strip().split(',')])
            elif (line in ['\n', '']) and (len(bingoBoard) > 0):
                bingoBoards.append(bingoBoard)
                bingoBoard = []
            elif line != '\n':
                bingoBoard.append(parseBingoBoardLine(line))

        bingoBoards.append(bingoBoard)

    return bingoNumbers, np.array(bingoBoards)


def parseBingoBoardLine(line):
    return [int(line[i:i+3].strip()) for i in range(0, len(line), 3)]


def createMarkingBoards(boards):
    markingBoards = []
    for i in range(len(boards)):
        markingBoard = []
        for j in range(len(boards[i])):
            markingBoard.append([False] * len(boards[i][j]))
        markingBoards.append(markingBoard)

    return np.array(markingBoards)


def checkForBingo(markingBoards):
    winningBoards = []
    for boardNum, board in enumerate(markingBoards):
        for i in range(len(board)):
            if (all(board[i,:])) or (all(board[:,i])):
                winningBoards.append(boardNum)

    return winningBoards


def calculateScore(board, markingBoard):
    score = ma.masked_array(board, markingBoard).sum()

    return score


def part1(nums, boards):
    markingBoards = createMarkingBoards(boards)

    for bingoNum in nums:
        markingBoards = (np.array(boards) == bingoNum) | markingBoards
        winningBoards = checkForBingo(markingBoards)
        for winningBoard in winningBoards:
            return bingoNum*calculateScore(boards[winningBoard], markingBoards[winningBoard])


def part2(nums, boards):
    markingBoards = createMarkingBoards(boards)

    prevScore = None

    for bingoNum in nums:
        markingBoards = (np.array(boards) == bingoNum) | markingBoards
        winningBoards = checkForBingo(markingBoards)
        if len(winningBoards) > 0:
            if len(boards) == 1:
                return bingoNum*calculateScore(boards[winningBoards[0]], markingBoards[winningBoards[0]])
            else:
                for winningBoard in winningBoards:
                    prevScore = bingoNum*calculateScore(boards[winningBoard], markingBoards[winningBoard])
                boards = np.delete(boards, winningBoards, 0)
                markingBoards = np.delete(markingBoards, winningBoards, 0)
            
    return prevScore


def main():

    testNums, testBoards = parseInput("./day04/test.txt")
    bingoNums, bingoBoards = parseInput("./day04/input.txt")

    assert(part1(testNums, testBoards)==4512)

    result1 = part1(bingoNums, bingoBoards)
    print(f"Part 1 solution: {result1}")

    assert(part2(testNums, testBoards)==1924)

    result2 = part2(bingoNums, bingoBoards)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()