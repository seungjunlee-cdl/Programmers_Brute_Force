Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def solution(answers):
    cor = [0,0,0]
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    ans_p1 = p1*(len(answers)//len(p1)) + p1[0:len(answers)%len(p1)]
    ans_p2 = p2*(len(answers)//len(p2)) + p2[0:len(answers)%len(p2)]
    ans_p3 = p3*(len(answers)//len(p3)) + p3[0:len(answers)%len(p3)]

    for i in range(len(answers)):
        ans_p1[i] = answers[i] - ans_p1[i]
        ans_p2[i] = answers[i] - ans_p2[i]
        ans_p3[i] = answers[i] - ans_p3[i]

    for i in range(3):
        exec('cor[i] = ans_p%d.count(0)'%(i+1))

    high_sc = []
    for i in range(3):
        if cor[i] == max(cor):
            high_sc.append(i+1)
    return high_sc