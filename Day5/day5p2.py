

def readData() -> list:
    with open('./data.txt', 'r') as f:
        data = f.readlines()
    return data


def getDataByCategory(category: str, rawData: list) -> list:
    data = []
    i = 0
    while i < len(rawData):
        if rawData[i].strip() == category:
            j = i + 1
            while (rawData[j].strip() != ''):
                data.append(list(map(int, rawData[j].strip().split(" "))))
                j += 1
                if (j >= len(rawData)):
                    break
        i += 1
    return data


def getOutputTransfer(initValue: int, transformMatrixChain: list[list[int]]) -> int:
    result = initValue
    for transformMatrix in transformMatrixChain:
        for row in transformMatrix:
            if (result >= row[1] and result <= (row[-1] + row[1])):
                result -= row[1] - row[0]
                break
    return result


def process(rawData: list[str]):

    listSeed = list(map(int, rawData[0].split(':')[-1].strip().split(" ")))
    listSeed = list(range(listSeed[0], listSeed[0] + listSeed[1])) + list(range(listSeed[2], listSeed[2] + listSeed[3]))

    seed2SoilMap = getDataByCategory(
        category="seed-to-soil map:", rawData=rawData)
    soil2Fertilizer = getDataByCategory(
        category="soil-to-fertilizer map:", rawData=rawData)
    fertilizer2Water = getDataByCategory(
        category="fertilizer-to-water map:", rawData=rawData)
    water2Light = getDataByCategory(
        category="water-to-light map:", rawData=rawData)
    light2Temperature = getDataByCategory(
        category="light-to-temperature map:", rawData=rawData)
    temperature2Humidity = getDataByCategory(
        category="temperature-to-humidity map:", rawData=rawData)
    humidity2Location = getDataByCategory(
        category="humidity-to-location map:", rawData=rawData)

    transformMatrixChain = [seed2SoilMap, soil2Fertilizer, fertilizer2Water,
                            water2Light, light2Temperature, temperature2Humidity, humidity2Location]

    listLocation = []
    for seed in listSeed:
        listLocation.append(getOutputTransfer(
            initValue=seed, transformMatrixChain=transformMatrixChain))
    print(min(listLocation))



if __name__ == '__main__':
    data = readData()
    process(data)
