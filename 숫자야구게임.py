import random

num_list = []
num = str(random.randint(0,9))
cnt_strike = 0
cnt_ball = 0
for i in range(3):
    while num in num_list:
        num = str(random.randint(0,9))
    num_list.append(num)

while cnt_strike < 3:
    cnt_strike = 0
    cnt_ball = 0
    number = str(input("숫자 3자리 입력>> "))

    if len(number) == 3:
        for i in range(3):
            for j in range(3):
                if number[i] == num_list[j] and i == j:
                    cnt_strike += 1
                elif number[i] == num_list[j] and i != j:
                    cnt_ball += 1
        if cnt_strike == 0 and cnt_ball == 0:
            print("3아웃!")
        else:
            s = ""
            if cnt_strike > 0:
                s += "{} 스트라이크 ".format(cnt_strike)
            if cnt_ball > 0:
                s += "{} 볼".format(cnt_ball)
            print(s)

print("게임 클리어!")
