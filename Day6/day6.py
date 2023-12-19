import math


def readData() -> list:
    with open('./data.txt', 'r') as f:
        data = [row.split(":")[-1].split() for row in f.readlines()]
    return data


def getRangePressingTime(time: int, distance: int):
    delta = time * time - 4 * distance
    if (delta >= 0):
        return (time - math.sqrt(delta))/2, (time + math.sqrt(delta))/2
    return None, None


def process(data: list):
    listTime = list(map(int, data[0]))
    listDistance = list(map(int, data[-1]))
    totalWays = 1

    for i in range(len(listTime)):
        minTime, maxTime = getRangePressingTime(listTime[i], listDistance[i])

        if (minTime is not None and maxTime is not None):
            if (minTime % 1 > 0):
                minTime = math.ceil(minTime)
            else:
                minTime += 1

            if (maxTime % 1 > 0):
                maxTime = math.floor(maxTime)
            else:
                maxTime -= 1
            totalWays *= (maxTime - minTime + 1)
    print(totalWays)


if __name__ == '__main__':
    data = readData()
    process(data)
