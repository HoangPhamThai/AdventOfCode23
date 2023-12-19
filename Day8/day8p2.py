import math

def readData() -> list:
    with open('./data.txt', 'r') as f:
        data = f.readlines()
    return data


def extractInfo(data: list):
    instruction = [0 if step == "L" else 1 for step in data[0].strip() ]
    map = {}
    for i in range(2, len(data)):
        line = data[i].strip().split("=")
        map[line[0].strip()] = [item.strip() for item in line[-1].strip()[1:-1].split(",")]
    
    return instruction, map
        

def process(data: list):
    instruction, map = extractInfo(data)
    instructionLen = len(instruction)

    result = 1
    for point in map:
        if (point[-1] == "A"):
            index = 0
            step = 0
            standingPoint = point
            while (standingPoint[-1] != "Z"):
                standingPoint = map[standingPoint][instruction[index]]
                index = (index + 1) % instructionLen
                step += 1

            result = math.lcm(result, step)

    print(result)


if __name__ == '__main__':
    data = readData()
    process(data)
    
