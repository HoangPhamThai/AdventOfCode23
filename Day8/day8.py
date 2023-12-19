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

    index = 0
    standingPoint = "AAA"
    expectEndPoint = "ZZZ"
    step = 0
    while (standingPoint != expectEndPoint):
        standingPoint = map[standingPoint][instruction[index]]
        index = (index + 1) % instructionLen
        step += 1

    print(step)


if __name__ == '__main__':
    data = readData()
    process(data)
    
