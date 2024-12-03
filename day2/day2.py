
def check_first_condition(report):
    diff_array = []
    isdecrease = False
    isincrease = False
    
    if report[0] - report[1] > 0:
        isdecrease = True
    elif report[0] - report[1] < 0:
        isincrease = True
    else:
        return None
    

    for i in range(0, len(report)-1):
        d =report[i] - report[i+1]
        if d > 0 and isdecrease:        
            diff_array.append(abs(d))
        elif d < 0 and isincrease:
            diff_array.append(abs(d))
        else:
            return None
    # print(diff_array)
    return diff_array

def check_second_condition(diff_array):

    for i in diff_array:
        if i >= 1 and i <=3 :
            pass
        else:
            return None
    return True

def part1(reports):
    sum = 0

    for report in reports:
        res1 = check_first_condition(report)
        if res1:
            res2 = check_second_condition(res1)
            if res2:
                sum += 1        
    print(sum)

def main():

    with open("./day2_example.txt") as f:
    # with open("./day2_input.txt") as f:
        lines = f.readlines()

    reports = []

    for line in lines:
        line_report = line.split(' ')
        line_report[-1] = line_report[-1].rstrip('\n')
        line_report = [int(i) for i in line_report]
        reports.append(line_report)

    print(reports)
    part1(reports)

if __name__ == "__main__":
    main()
