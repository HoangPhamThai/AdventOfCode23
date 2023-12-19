
class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.type = self.__getHighestType()
        self.encodeCards = self.__encode()
        self.rank = 0

    def __encode(self):
        encodeDict = {
            "J": "a",
            "2": "b",
            "3": "c",
            "4": "d",
            "5": "e",
            "6": "f",
            "7": "g",
            "8": "h",
            "9": "i",
            "T": "j",
            "Q": "l",
            "K": "m",
            "A": "n",
        }
        return ''.join(encodeDict[card] for card in self.cards)

    def __getHighestType(self):
        if ("J" in self.cards):
            uniqueCardSet = set(self.cards)
            listType = []
            for char in uniqueCardSet:
                if (char != "J"):
                    listType.append(self.__getType(
                        cards=self.cards.replace("J", char)))
            if (len(listType) > 0):
                return max(listType)
            else:
                return self.__getType(cards=self.cards)
        else:
            return self.__getType(cards=self.cards)

    def __getType(self, cards):
        freq = {}
        # 0: high card
        # 1: one pair
        # 2: two pairs
        # 3: three of a kind
        # 4: full house
        # 5: four of a kind
        # 6: five of a kind
        type = 0
        for card in cards:
            if (card in freq):
                freq[card] += 1
            else:
                freq[card] = 1
        freqLen = len(freq)
        if (freqLen == 5):
            type = 0
        elif (freqLen == 4):
            type = 1
        elif (freqLen == 3):
            # 2 pairs or 3 of a kind
            if (3 in list(freq.values())):
                type = 3
            else:
                type = 2
        elif (freqLen == 2):
            # full house or four of a kind
            if (4 in list(freq.values())):
                type = 5
            else:
                type = 4
        else:
            type = 6
        return type

    def getTotalWinnings(self):
        return self.bid * self.rank

    def __repr__(self) -> str:
        return f"{self.cards} - {self.encodeCards} - {self.type} - {self.rank}"


class ListHand:
    def __init__(self, listHand: list[Hand], type: int):
        self.listHand = [hand for hand in data if hand.type == type]
        self.type = type
        self.__sort()

    def __sortKey(self, obj: Hand):
        return obj.encodeCards

    def __sort(self):
        self.listHand = sorted(self.listHand, key=self.__sortKey)

    def __repr__(self) -> str:
        result = ''
        for hand in self.listHand:
            result = result + "\n" + f"{hand}"
        return result

    def setRank(self, initRank: int = 1):
        rank = initRank
        for hand in self.listHand:
            hand.rank = rank
            rank += 1

    def getLastRank(self):
        if (len(self.listHand) == 0):
            return 0
        return self.listHand[-1].rank

    def getTotalWinnings(self):
        total = 0
        for hand in self.listHand:
            total += hand.getTotalWinnings()
        return total


def readData() -> list:
    with open('./data.txt', 'r') as f:
        rawData = [[item.strip() for item in row.split(" ")]
                   for row in f.readlines()]
    data = [Hand(cards=hand[0], bid=int(hand[1])) for hand in rawData]
    return data


def process(data: list[Hand]):
    list5Kind = ListHand(data, 6)
    list4Kind = ListHand(data, 5)
    listFullHouse = ListHand(data, 4)
    list3Kind = ListHand(data, 3)
    list2Pair = ListHand(data, 2)
    list1Pair = ListHand(data, 1)
    listHighCard = ListHand(data, 0)

    initRank: int = 1
    listHighCard.setRank(initRank=initRank)
    if (len(listHighCard.listHand) > 0):
        initRank = listHighCard.getLastRank() + 1

    list1Pair.setRank(initRank=initRank)
    if (len(list1Pair.listHand) > 0):
        initRank = list1Pair.getLastRank() + 1

    list2Pair.setRank(initRank=initRank)
    if (len(list2Pair.listHand) > 0):
        initRank = list2Pair.getLastRank() + 1

    list3Kind.setRank(initRank=initRank)
    if (len(list3Kind.listHand) > 0):
        initRank = list3Kind.getLastRank() + 1

    listFullHouse.setRank(initRank=initRank)
    if (len(listFullHouse.listHand) > 0):
        initRank = listFullHouse.getLastRank() + 1

    list4Kind.setRank(initRank=initRank)
    if (len(list4Kind.listHand) > 0):
        initRank = list4Kind.getLastRank() + 1

    list5Kind.setRank(initRank=initRank)

    total = list5Kind.getTotalWinnings() + list4Kind.getTotalWinnings() + listFullHouse.getTotalWinnings() + \
        list3Kind.getTotalWinnings() + list2Pair.getTotalWinnings() + \
        list1Pair.getTotalWinnings() + listHighCard.getTotalWinnings()
    print(total)


if __name__ == '__main__':
    data = readData()
    process(data)
