
def getCubeData(game : str) -> list:
    listGameData = []
    gameData = game.split(":")[-1]
    listGameTurns = gameData.split(";")
    for turn in listGameTurns:
        listCubeDataTurn = turn.strip().split(",")
        for cubeDataTurn in listCubeDataTurn:
            cubeData = cubeDataTurn.strip().split(" ")
            listGameData.append({
                "color": cubeData[-1],
                "value": int(cubeData[0])
            })
    return listGameData

def isValidGameTurn(game : str):
    gameMetadata : dict = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    cubeData : list = getCubeData(game)
    for cube in cubeData:
        if (gameMetadata[cube["color"]] < cube["value"]):
            return False
    return True


if __name__ == "__main__":
    with open('./data_day2.txt', 'r') as f:
        data = f.readlines()

    totalValidGameTurn = 0
    for index in range(len(data)):
        if (isValidGameTurn(data[index])):
            totalValidGameTurn += index + 1

    print(totalValidGameTurn)
