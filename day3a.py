import re
with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]

line = "".join(lines)
pattern = r"(\w+)\((\d+),(\d+)\)"
matches = re.findall(pattern, line)
total = 0

for match in matches:
    instruction, num1, num2 = match

    if instruction == "mul" or instruction.endswith("mul"):
        total += int(num1) * int(num2)

print(total)
