with open("program.txt", "r") as file:
    read = file.readlines()

for x, y in enumerate(read):
    read[x] = y.replace("\n", "")

memory = [0] * int(read[0].replace("memory ", ""))
lines = dict()
count = 1

while count < len(read):
    instruction = []

    if "set" in read[count]:
        instruction.append("set")
        instruction.append(read[count].split(": ")[1])
        instruction.append(read[count].split(": ")[2])

    if "send" in read[count]:
        instruction.append("send")
        instruction.append(read[count].split(": ")[1])

    lines[count] = instruction
    count += 1

count = 1

while count <= len(lines):
    typeinstruction = lines[count][0]

    if typeinstruction == "set":
        memory[int(lines[count][1], 16)] = lines[count][2]

    elif typeinstruction == "send":
        print(memory[int(lines[count][1], 16)])
    
    count += 1