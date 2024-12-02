with open('day1.txt') as f:
    lines = [line.rstrip() for line in f]

left_list = []
right_list = []

for line in lines:
    left, right = line.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))


sim_score = 0
for i in range(len(left_list)):
    sim_score += right_list.count(left_list[i]) * left_list[i]

print(sim_score)





