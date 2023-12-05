

def createReverseDict(dictInput : dict):
    result = {}
    
    for key in dictInput:
        result[key[::-1]] = dictInput[key]
    return result


def findLetter(dictionary : dict, inputStr : str):
    firstIndex = -1
    firstKey = ""
    for letter in dictionary.keys():
        position = inputStr.find(letter)
        if (position == -1): continue

        if (firstIndex == -1 or position <= firstIndex):
            firstIndex = position
            firstKey = letter
    return firstKey, firstIndex


def findNumber(inputStr : str, listNum : list[int]):
    for i in range(0, len(inputStr)):
        if (inputStr[i] in listNum):
            return inputStr[i], i
    return None, None


def getFirstNum(line: str, dictionary: dict, listNum : list[int]):
    numberValue, numberIndex = findNumber(line, listNum)
    letterKey, letterIndex = findLetter(dictionary, line)
    if (numberIndex != None):
        if (letterKey != ""):
            if (numberIndex > letterIndex):
                return dictionary[letterKey]
            return numberValue
        return numberValue
    if (letterKey != ""):
        return dictionary[letterKey]
    return None
    

if __name__ == '__main__':

    with open('./data.txt', 'r') as f:
        data = f.readlines()

    
    listNum = ["1", "2", "3", "4", "5", "6", "7", "8","9","10"]
    dictNumLetter = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    sum = 0
    dictNumLetterReversed = createReverseDict(dictNumLetter)

    for line in data:
        firstNum = getFirstNum(line, dictNumLetter, listNum)
        lastNum = getFirstNum(line[::-1], dictNumLetterReversed, listNum)
        if (firstNum != None and lastNum != None):
            sum += int(firstNum) * 10 + int(lastNum)

    print(sum)