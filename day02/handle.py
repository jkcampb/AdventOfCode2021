def parseInput(file):
    with open(file, "r") as inputFile:
        inputData = inputFile.read().split('\n')
    return inputData


def part1(course):
    x, y = 0, 0

    for step in course:
        direction, distance = step.split(' ')
        if direction == 'forward':
            y+=int(distance)
        elif direction == 'down':
            x+=int(distance)
        elif direction == 'up':
            x-=int(distance)

    return x*y


def part2(course):
    x, y, aim = 0, 0, 0

    for step in course:
        direction, value = step.split(' ')
        if direction == 'forward':
            y+=int(value)
            x+=aim*int(value)
        elif direction == 'down':
            aim+=int(value)
        elif direction == 'up':
            aim-=int(value)

    return x*y


def main():

    testInput = parseInput("./day02/test.txt")
    realInput = parseInput("./day02/input.txt")

    assert(part1(testInput)==150)

    result1 = part1(realInput)
    print(f"Part 1 solution: {result1}")

    assert(part2(testInput)==900)

    result2 = part2(realInput)
    print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()