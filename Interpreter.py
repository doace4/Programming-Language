with open("program.txt", "r") as file:
    read = file.readlines()

for x, y in enumerate(read):
    read[x] = y.replace("\n", "")

memory = [0] * int(read[0].replace("memory ", ""))
lines = dict()
count = 1

while count < len(read):
    instruction = []
    inputs = read[count].split(": ")

    if "set" in read[count]:
        instruction.append("set")
        instruction.append(inputs[1])
        instruction.append(inputs[2])

    elif "send" in read[count]:
        instruction.append("send")
        instruction.append(inputs[1])

    elif "inc" in read[count]:
        instruction.append("inc")
        instruction.append(inputs[1])

    elif "dec" in read[count]:
        instruction.append("dec")
        instruction.append(inputs[1])

    elif "condition" in read[count]:
        instruction.append("condition")
        instruction.append(inputs[1])
        instruction.append(inputs[2])

    lines[count] = instruction
    count += 1

count = 1

while count <= len(lines):
    typeofinstruction = lines[count][0]
    value = int(lines[count][1], 16)

    if typeofinstruction == "set":
        memory[value] = lines[count][2]

    elif typeofinstruction == "send":
        print(value)

    elif typeofinstruction == "inc":
        memory[value] += 1

    elif typeofinstruction == "dec":
        memory[value] -= 1

    elif typeofinstruction == "condition":
        if eval(lines[count][1]):
            count = int(lines[count][2])
    
    count += 1
