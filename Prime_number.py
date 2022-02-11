from itertools import permutations

def solution(numbers):
    cnt = 0
    number_list = list(map(int,numbers))
    numbers_case = []

    for nl in range(len(number_list)):
        cases = list(permutations(number_list,nl+1))

        for i in range(len(cases)):
            case = list(map(str,cases[i]))
            if nl== 0:
                numbers_case.append(int(case[0]))
            else:
                num_test = int("".join(case))
                numbers_case.append(num_test)

        numbers_case = list(set(numbers_case))

    if 0 in numbers_case:
        numbers_case.remove(0)
    if 1 in numbers_case:
        numbers_case.remove(1)

    for i in numbers_case:
        bool_p = 1
        for den in range(2,i):
            if i%den==0:
                bool_p -= 1
                break

        if bool_p ==1:
            cnt += 1
    return cnt
