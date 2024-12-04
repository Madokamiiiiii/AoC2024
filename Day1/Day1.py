
list1 = []
list2 = []
total = 0
with open("input.txt", "r") as f:
    data = f.readlines()
    for line in data:
        line = line.split("   ")
        list1.append(int(line[0]))
        list2.append(int(line[1]))

def part1(total):
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        total += abs(list2[i] - list1[i])

    print(total)

part1(total)

def part2(total):
    numOccurences = {}
    for num in list1:
        if num in numOccurences:
            total += numOccurences[num]
        else:
            numOccurences[num] = num * list2.count(num)
            total += numOccurences[num]
    print(total)

part2(total)




