with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]


def check_report(report):
    report_count = len(report)

    up = 1
    down = 1

    for n in range(len(report) - 1):
        if report[n] < report[n + 1]:
            up += 1

        if report[n] > report[n + 1]:
            down += 1

    if up == report_count or down == report_count:
        for n in range(len(report) - 1):
            diff = abs(report[n] - report[n + 1])
            if diff > 3 or diff < 0:
                return False
        return True
    else:
        return False

safe_reports = 0
for line in lines:
    r = [int(item) for item in line.split(' ')]

    if check_report(r):
        safe_reports += 1
    else:
        # print(r)
        for x in range(0, len(r)):
            r2 = r.copy()
            del r2[x]

            if check_report(r2):
                safe_reports += 1
                break

# 289, to low
# 306, to low

print(safe_reports)
