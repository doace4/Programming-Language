from time import time as t
start = t()

with open("program.txt", "r") as file:
    read = file.readlines()

for x, y in enumerate(read):
    read[x] = y.replace("\n", "")

memory = [0] * int(read[0][6:])
lines = []
count = 0

for x in read:
    instruction = []
    inputs = x.split(": ")

    if inputs[0] == "set":
        instruction.append("set")
        instruction.append(inputs[1])

        try:
            instruction.append(int(inputs[2]))

        except ValueError:
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
        instruction.append(inputs[1].split(" ")[0])
        instruction.append(inputs[1].split(" ")[1])
        instruction.append(inputs[1].split(" ")[2])
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
        pass
        print(memory[value])

    elif typeofinstruction == "inc":
        memory[value] += 1

    elif typeofinstruction == "dec":
        memory[value] -= 1

    elif typeofinstruction == "condition":
        if lines[count][2] == "<":
            if memory[value] < int(lines[count][3]):
                count = int(lines[count][4])
        
        elif lines[count][2] == ">":
            if memory[value] > int(lines[count][3]):
                count = int(lines[count][4])

        elif lines[count][2] == "<=":
            if memory[value] <= int(lines[count][3]):
                count = int(lines[count][4])

        elif lines[count][2] == ">=":
            if memory[value] >= int(lines[count][3]):
                count = int(lines[count][4])

        elif lines[count][2] == "=":
            if memory[value] == int(lines[count][3]):
                count = int(lines[count][4])
    
    count += 1

stop = t()
print(f"The program finished in {stop - start} secs")
