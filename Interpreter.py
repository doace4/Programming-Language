with open("program.txt", "r") as file:
    read = file.readlines()

for x, y in enumerate(read):
    read[x] = y.replace("\n", "")

memory = [0] * int(read[0].replace("memory ", ""))
lines = []
count = 0

for x in read:
    instruction = []
    inputs = x.split(": ")

    if inputs[0] == "set":
        instruction.append("set")
        instruction.append(inputs[1])
        instruction.append(inputs[2])

    elif inputs[0] == "send":
        instruction.append("send")
        instruction.append(inputs[1])

    elif inputs[0] == "inc":
        instruction.append("inc")
        instruction.append(inputs[1])

    elif inputs[0] == "dec":
        instruction.append("dec")
        instruction.append(inputs[1])

    elif inputs[0] == "condition":
        instruction.append("condition")
        instruction.append(inputs[1])
        instruction.append(inputs[2])

    else:
        instruction = 0

    if instruction:
        lines.append(instruction)

while count < len(lines):
    typeofinstruction = lines[count][0]
    value = int(lines[count][1], 16)

    if typeofinstruction == "set":
        memory[value] = lines[count][2]

    elif typeofinstruction == "send":
        print(memory[value])

    elif typeofinstruction == "inc":
        memory[value] += 1

    elif typeofinstruction == "dec":
        memory[value] -= 1

    elif typeofinstruction == "condition":
        if eval(lines[count][1]):
            count = int(lines[count][2])
    
    count += 1
