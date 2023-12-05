

listNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8","9","10"]
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
        print(letter, position, firstIndex)
        if (position == -1): continue

        if (firstIndex == -1 or position <= firstIndex):
            firstIndex = position
            firstKey = letter
    return firstKey, firstIndex

def findNumber(inputStr : str):
    for i in range(0, len(inputStr)):
        if (inputStr[i] in listNum):
            return inputStr[i], i
    return None, None


def getFirstNum(line: str, dictionary: dict):
    numberValue, numberIndex = findNumber(line)
    # print(numberValue, numberIndex)
    letterKey, letterIndex = findLetter(dictionary, line)
    # print(letterKey, letterIndex)
    if (numberIndex != None):
        if (letterKey != ""):
            if (numberIndex > letterIndex):
                return dictionary[letterKey]
            return numberValue
        return numberValue
    if (letterKey != ""):
        return dictionary[letterKey]
    return None
    
    

sum = 0
dictNumLetterReversed = createReverseDict(dictNumLetter)

data = "abcone2threexyz"
firstNum = getFirstNum(data, dictNumLetter)
lastNum = getFirstNum(data[::-1], dictNumLetterReversed)
if (firstNum != None and lastNum != None):
    sum += int(firstNum) * 10 + int(lastNum)

print(sum)