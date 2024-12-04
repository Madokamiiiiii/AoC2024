
res = 0
res2 = 0

def checkLine(numLine):
    safe = False
    if sorted(numLine) == numLine or sorted(numLine, reverse=True) == numLine:
        i, safe = 1, True
        while i < len(numLine) and safe:
            if abs(numLine[i] - numLine[i-1]) > 3 or numLine[i] == numLine[i - 1]:
                safe = False
            i += 1

    return safe

def part2(numLine):
    i = 0
    while i < len(numLine):
        fixedLine = numLine[:i] + numLine[i+1:]
        if checkLine(fixedLine):
            return True
        i += 1
    return False

with open("input.txt", "r") as f:
    data = f.readlines()
    for line in data:
        line = [int(x) for x in line.strip().split(" ")]
        if checkLine(line):
            res += 1
            res2 += 1
        else:
            if(part2(line)):
                res2 += 1

print(res)
print(res2)
