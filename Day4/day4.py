def extractCard(card):
    cartNumbers = card.split(":")[-1].strip()
    winningNumbers, owningNumbers = cartNumbers.split("|")
    winningNumbers = winningNumbers.strip().split(" ")
    owningNumbers = owningNumbers.strip().split(" ")
    winningNumbers = list(filter(lambda x: x != '', winningNumbers))
    owningNumbers = list(filter(lambda x: x != '', owningNumbers))
    return winningNumbers, owningNumbers


def readData() -> list:
    with open('./data.txt', 'r') as f:
        data = f.readlines()
    return data

def getCardScrore(card):
    winningNumbers, owningNumbers = extractCard(card)
    # create a dictionary of winning numbers
    dictWinningNumber = {}
    for number in winningNumbers:
        dictWinningNumber[number] = 0
    # Calculate the number of appearance of each winning number
    for number in owningNumbers:
        if (number in dictWinningNumber):
            dictWinningNumber[number] += 1
    totalCorrectNumber = sum(list(dictWinningNumber.values()))
    
    totalScore = 0
    if (totalCorrectNumber == 0): totalScore = 0
    else: totalScore = 2**(totalCorrectNumber - 1)
    
    return totalScore



if __name__ == '__main__':
    data = readData()
    totalScore = 0
    for card in data:
        totalScore += getCardScrore(card)
    print(totalScore)