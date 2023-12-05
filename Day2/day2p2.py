
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

def getPowerOfGameTurn(game : str) -> int:
    minCubeRequired : dict = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    cubeData : list = getCubeData(game)
    for cube in cubeData:
        if (minCubeRequired[cube["color"]] < cube["value"]):
            minCubeRequired[cube["color"]] = cube["value"]
    
    gamePower = 1
    for value in minCubeRequired.values():
        gamePower *= value
    return gamePower


if __name__ == "__main__":
    with open('./data_day2.txt', 'r') as f:
        data = f.readlines()

    total = 0
    for game in data:
        total += getPowerOfGameTurn(game)

    print(total)
