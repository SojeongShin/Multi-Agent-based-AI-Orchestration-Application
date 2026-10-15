# number = 1
# print(number)

# 사용자로 부터 점수를 입력받아서 70점 이상이면 합격, 70점 미만이면 불합격을 출력.
# score = int(input("점수를 입력하세요: "))
# if score >= 70:
#     print("합격")
# else:
#     print("불합격")



# 반복문
# num_list = []
# for i in range(5):
#     number = int(input(f"{i+1}번째 숫자를 입력하세요: "))
#     num_list.append(number)
# print("입력한 숫자:", num_list)
# for num in num_list:
#     print(num, end=" ")
# print()  # 줄바꿈


# for dan in range(2, 10):
#     for i in range(1, 10):
#         print(f"{dan} x {i} = {dan * i}")
#     print("")
# print("구구단 출력")
# for i in range(1, 10):
#     for dan in range(2, 10):
#         print(f" {dan} x {i} = {dan * i}", end="\t")
    

import random
num = random.randint(1, 100)
user_num = int(input("1~100 사이의 숫자를 입력하세요: "))
while user_num != num: 
    if user_num > num:
        print("입력한 숫자가 큽니다.")
    else:
        print("입력한 숫자가 작습니다.")
    user_num = int(input("다시 입력하세요: "))

print("정답입니다!")