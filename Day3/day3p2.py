def getSizes(schematic):
    numRow = len(schematic)
    numCol = len(schematic[0])
    return numRow, numCol


def getSchematic() -> list:
    with open('./data.txt', 'r') as f:
        schematic = f.readlines()
    return makeBorder(schematic)


def makeBorder(schematic):
    _, col = getSizes(schematic)
    horzBorder = "."*(col + 1)
    newSchematic = [horzBorder]
    for line in schematic:
        line = "." + line.strip() + "."
        newSchematic.append(line)

    newSchematic.append(horzBorder)
    return newSchematic


def isSymbol(char):
    listNotSymbol = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "0"]
    return char not in listNotSymbol


def isNearSymbol(schematic, i, j):
    return (isSymbol(schematic[i-1][j-1])
            or isSymbol(schematic[i-1][j])
            or isSymbol(schematic[i-1][j+1])
            or isSymbol(schematic[i][j-1])
            or isSymbol(schematic[i][j+1])
            or isSymbol(schematic[i+1][j-1])
            or isSymbol(schematic[i+1][j])
            or isSymbol(schematic[i+1][j+1]))


def getNextIndices(i, j, col):
    if (j == col - 1):
        j = 1
        i += 1
    else:
        j += 1

    return i, j


def getListPartNumber(schematic) -> list:
    listNumber = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    numRow = len(schematic)
    numCol = len(schematic[0])

    listPartNumber = []
    i = 1
    j = 1
    start = 0

    nearSymbol = False
    print(numRow, numCol)
    while i < numRow:
        while j < numCol:
            if ((i == (numRow)) or (j == numCol)):
                break
            if (schematic[i][j] not in listNumber):
                # check if it's the end of a number
                if (start == 0):
                    i, j = getNextIndices(i, j, numCol)
                    continue

                # Found a part number
                if (nearSymbol):
                    listPartNumber.append(schematic[i][start: j])
                    start = 0
                    nearSymbol = False
                else:
                    start = 0


                i, j = getNextIndices(i, j, numCol)
                continue

            # get the starting point of a number in a row
            if (start == 0):
                start = j

            if (not nearSymbol):
                nearSymbol = isNearSymbol(schematic, i, j)

            i, j = getNextIndices(i, j, numCol)

    return listPartNumber

def findNumber(schematic, i, j, markedMap : dict):
    listNumber = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    num : str = schematic[i][j]
    if (num not in listNumber):
        return markedMap, None
    # search from the left
    start : int = j
    while (schematic[i][start] in listNumber):
        num = schematic[i][start] + num


def findListGear(schematic) -> list:
    numRow = len(schematic)
    numCol = len(schematic[0])

    i = 1
    j = 1

    while i < numRow:
        while j < numCol:
            if (isSymbol(schematic[i][j])):
                pass


def calSum(listNum):
    result = 0
    for item in listNum:
        result += int(item)
    return result

if __name__ == "__main__":
    schematic: list = getSchematic()

    


