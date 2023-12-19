input = "abcone2threexyz"
inputReversed = input[::-1]

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


def findLetter(dictionary : dict, input : str):
    firstIndex = 0
    firstKey = ""
    for letter in dictionary.keys():
        position = input.find(letter)
        if (position == -1): continue

        if (firstIndex == 0 or position <= firstIndex):
            firstIndex = position
            firstKey = letter
    return firstKey, firstIndex

dictNumLetterReversed = createReverseDict(dictNumLetter)

keyInc, indexInc = findLetter(dictNumLetter, input)
keyDec, indexDec = findLetter(dictNumLetterReversed, inputReversed)

print(keyInc, dictNumLetter[keyInc], indexInc)
print(keyDec, dictNumLetterReversed[keyDec], indexDec)
