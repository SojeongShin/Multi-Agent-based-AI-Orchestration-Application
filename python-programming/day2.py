# # 논리 연산자
# def expensive_check():
#     print("시간이 오래 걸리는 함수를 실행합니다.")
#     return True

# is_active = False
# # is_active의 상태에 따라 expensive_check() 함수를 호출할지 결정
# if is_active and expensive_check():
#     print("활성화 상태입니다.")
# else:
#     print("비활성화 상태입니다.")


# #  class와 객체
# class SafeProfile:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get(self, key):
#         if key == "name":
#             return self.name
#         elif key == "age":
#             return self.age
#         else:
#             return None
        
#     def set(self, key, value):
#         if key == "name":
#             self.name = value
#         elif key == "age":
#             self.age = value

#     def show_profile(self):
#         print(f"이름: {self.name}, 나이: {self.age}")

# # user_profile = None  # user_profile 객체를 None으로 설정
# user_profile = SafeProfile("홍길동", 30)
# print(user_profile.name)  # 홍길동
# print(user_profile.age)   # 30
# user_profile.show_profile()  # 이름: 홍길동, 나이: 30

# if user_profile and user_profile.get("name"):
#     print(user_profile.name)  # 홍길동

# if user_profile:
#     user_profile.set("name", "김철수")
#     user_profile.show_profile()  # 이름: 김철수, 나이: 30


# 삼항 연산자
# user_age = 20

# if user_age >= 18:
#     access = "성인"
# else:
#     access = "미성년자"
# print(access)

# print("성인" if user_age >= 18 else "미성년자")


# 포함관계 in, not in
# allowd_roles = ["admin", "user", "manager"]
# user_role = input("Plz select your role in admin, user, manager, staff, guest): ")

# if user_role in allowd_roles:
#     print("Allowed")
# else:
#     print("Denied")


# # 리스트 vs 딕셔너리
# list_1 = [1, 2, 3, 4, 5]
# dict_1 = {"one": 1, "two": 2, "three": 3, "ten": 10}

# one = list_1[0]
# print(one)

# dict_one = dict_1["one"]
# print(dict_1.get("one"))  # 1
# print(dict_1.get("four", "default"))  # default, 해당 값이 없으면 2번째 값으로 반환

# values = dict_1.values() # dict_values([1, 2, 3])
# print(values)  # dict_values([1, 2, 3])
# values_list = list(values)  # [1, 2, 3]
# print(values_list)  # [1, 2, 3]

# dict_1.keys()   # dict_keys(['one', 'two', 'three'])
# dict_1.items()  # dict_items([('one', 1), ('two', 2), ('three', 3)])
# print(dict_1.items())

# dict_1.pop("one")  # 1
# print(dict_1.items())  # dict_items([('two', 2), ('three', 3)])

# dict_1["ten"] = 10 # 값이 없으면 추가, 있으면 수정
# dict_1.update({"ten": 10, "twenty": 20}) # 여러개 추가
# dict_1.update({"ten": 100}) # 값이 있으면 수정
# print(dict_1.items())

# dict_1[0] = 10
# print(dict_1["ten"])  # 10

# for i in dict_1:
#     print(i)  # 키 값만 반환

# key1, val1 = list(dict_1.items())[0]
# print(key1, val1)  # two 2

# # key_l, val_l = [], []
# key_l, val_l = list(dict_1.keys()), list(dict_1.values())
# print(key_l, val_l)

# 리스트 comprehension
list_1 = [1, 2, 3, 4, 5]
for i in list_1:
    if i % 2 == 0:
        print(i, end=" ")  # 2, 4

result = [i for i in list_1 if i % 2 == 0]
print(result)  # [2, 4]

menu = ["Americano", "Latte", "Cappuccino", "Mocha"]
ice = ["ice " + i for i in menu]
print(ice)


# 20세 이상인 데이터 추출
ages = [25, 17, 30, 15, 22]
adults = ["adult" if age >= 20 else "adolescent" for age in ages ]
print(adults)  # ['adult', 'adolescent', 'adult', 'adolescent', 'adult']

cnt_adults = adults.count("adult")
print(cnt_adults)  # 3

# print(sorted(adults))  # [22, 25, 30]


# 규칙에 맞는 데이터 추출(빈 데이터, 중복 제외, 오름차순 정렬)
# import re
# bad_words = ["bad", "", "evil", "nasty", "", "mean", "bad"]
# # filtered_words = []

# # for word in bad_words:
# #     if word and word not in filtered_words:
# #         filtered_words.append(word)

# # print(sorted(filtered_words))  # ['bad', 'evil', 'nasty', 'mean']

# filtered_word2 = list(set(word for word in bad_words if word))
# print(sorted(filtered_word2))


import random
ages = random.sample(range(15, 100), 25)
results = []
cnt_adults = 0
cnt_adolescents = 0

for i in ages:
    if i >= 20:
        results.append("adult")
        cnt_adults += 1
    else:
        results.append("adolescent")
        cnt_adolescents += 1
print(results)  # ['adult', 'adolescent', 'adult', 'adolescent', 'adult']
print(f"성인: {cnt_adults}, 청소년: {cnt_adolescents}")