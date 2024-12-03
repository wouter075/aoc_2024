with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]

line = "".join(lines).rstrip()
offset = 0
enabled = True
total = 0

while offset < len(line):
    if line[offset:].startswith("do()"):
        enabled = True
        offset += 4

    if line[offset:].startswith("don't()"):
        enabled = False
        offset += 7

    if line[offset:].startswith("mul("):
        if len(line[offset + 4:].split(",")) > 1:
            num1 = line[offset + 4:].split(",")[0]
            num2 = line[offset + 4:].split(",")[1].split(')')[0]

            if num1.isdigit() and num2.isdigit() and enabled:
                total += int(num1) * int(num2)
                offset += len(num1) + len(num2) + 2

    offset += 1

print(total)


