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

def updateCardDict(card : str, cardDict : dict, cardIndex : int):
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

    
    
    if (totalCorrectNumber != 0):
        for time in range(totalCorrectNumber):
            cardDict[cardIndex + time + 1] += cardDict[cardIndex]
    # print(f'card {cardIndex} - totalCorrectNumber = {totalCorrectNumber} - cardDict = {cardDict}')

    return cardDict

def createCardDict(data) -> dict:
    card = {}
    for i in range(len(data)):
        card[i+1] = 1
    return card

if __name__ == '__main__':
    data = readData()
    cardDict = createCardDict(data)
    for i in range(len(data)):
        card = data[i]
        cardDict = updateCardDict(card, cardDict, i + 1)

    print(sum(list(cardDict.values())))
    
    # for card in data:
    #     totalScore += getCardScrore(card)
    # print(totalScore)