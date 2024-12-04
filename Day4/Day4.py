import re

input = open("input.txt", "r").readlines()

input = [x.strip() for x in input]

lineLength = len(input[0].strip())
numRows = len(input)

res = 0

# Forward / backward
for i in range(numRows):
    findings = re.findall(r"(?=(XMAS|SAMX))", input[i])
    res += len(findings)

    # vertical
    if i < numRows - 3:
        for j in range(lineLength):
            word = input[i][j] + input[i+1][j] + input[i+2][j] + input[i+3][j]
            find = re.search(r"XMAS|SAMX", word)
            if find is not None:
                res += 1
        # horizontal
        for j in range(lineLength - 3):
            word = input[i][j] + input[i+1][j+1] + input[i+2][j+2] + input[i+3][j+3]
            find = re.search(r"XMAS|SAMX", word)
            if find is not None:
                res += 1

    # horizontal backwards
        for j in range(3, lineLength):
            word = input[i][j] + input[i+1][j-1] + input[i+2][j-2] + input[i+3][j-3]
            find = re.search(r"XMAS|SAMX", word)
            if find is not None:
                res += 1

print(res)

res2 = 0

for i in range(1, numRows-1):
    for j in range(1, lineLength-1):
        if input[i][j] == "A":
            word = input[i-1][j-1] + input[i-1][j+1] + input[i+1][j-1] + input[i+1][j+1]
            if word == "MMSS" or word == "SSMM" or word == "MSMS" or word == "SMSM":
                res2 += 1

print(res2)