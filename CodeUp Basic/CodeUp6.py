# 코드업 6063~6070
# 기초-3항연산~기초-조건/선택실행구조

# 6063
# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.
# a, b = map(int, input().split())
#
# if(a<b):
#     print(b)
# else:
#     print(a)

# 6064
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

# 5 10 15
# a, b, c = map(int, input().split())
# # print(min(a,b,c))
#
# d = a if a<b else b
# e = d if d<c else c
# print(e)

# 6065
# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
# a, b, c = map(int, input().split())
# if(a%2==0):
#     print(a)
# if(b%2==0):
#     print(b)
# if(c%2==0):
#     print(c)


# 6066
# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

# a, b, c = map(int, input().split())
# if (a%2==0):
#     print("even")
# else:
#     print("odd")
#
# if (b%2==0):
#     print("even")
# else:
#     print("odd")
#
# if (c%2==0):
#     print("even")
# else:
#     print("odd")

# 6067
# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.

# a = int(input())
# if (a<0):
#     if(a%2==0):
#         print("A")
#     else:
#         print("B")
# else:
#     if (a % 2 == 0):
#         print("C")
#     else:
#         print("D")

# 6068
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

# n = int(input())
# if(n>=90):
#     print("A")
# elif(n>=70):
#     print("B")
# elif(n>=40):
#     print("C")
# else:
#     print("D")

# 6069
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
#
# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

# c = input()
#
# if(c =="A"):
#     print("best!!!")
# elif(c=="B"):
#     print("good!!")
# elif(c=="C"):
#     print("run!")
# elif(c=="D"):
#     print("slowly~")
# else:print("what?")

# 6070
# 월이 입력될 때 계절 이름이 출력되도록 해보자.
# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall
# // 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
a = int(input())
if (a == 12 or a == 1 or a == 2):
    print("winter")
elif (a == 3 or a == 4 or a == 5):
    print("spring")
elif ( a == 6 or a == 7 or a == 8):
    print("summer")
else: print("fall")



