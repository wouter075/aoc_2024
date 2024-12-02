with open('day1.txt') as f:
    lines = [line.rstrip() for line in f]

left_list = []
right_list = []

for line in lines:
    left, right = line.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))

left_list = sorted(left_list)
right_list = sorted(right_list)

distance = 0
for i in range(len(left_list)):
    distance += abs(right_list[i] - left_list[i])

# 800528 - to low
print(distance)



