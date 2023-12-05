


def findNumber(inputStr : str, listNum : list[int]):
    for i in range(0, len(inputStr)):
        if (inputStr[i] in listNum):
            return inputStr[i], i
    return None, None


def getFirstNum(line: str, listNum : list[int]):
    numberValue, _ = findNumber(line, listNum)
    return numberValue
    

if __name__ == '__main__':

    with open('./data.txt', 'r') as f:
        data = f.readlines()

    listNum = ["1", "2", "3", "4", "5", "6", "7", "8","9","10"]
    sum = 0

    for line in data:
        firstNum = getFirstNum(line, listNum)
        lastNum = getFirstNum(line[::-1], listNum)
        if (firstNum != None and lastNum != None):
            sum += int(firstNum) * 10 + int(lastNum)

    print(sum)