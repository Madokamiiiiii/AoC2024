import re

input = open("input.txt", "r").read()

matches = re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)", input)

res = 0

for match in matches:
    nums = re.findall(r"\d{1,3}", match)
    res += int(nums[0]) * int(nums[1])

print(res)

res2 = 0
enabled = True
matches = re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)|do\(\)|don't\(\)", input)

for match in matches:
    if "don't" in match:
        enabled = False
    elif "do" in match:
        enabled = True
    elif enabled:
        nums = re.findall(r"\d{1,3}", match)
        res2 += int(nums[0]) * int(nums[1])

print(res2)