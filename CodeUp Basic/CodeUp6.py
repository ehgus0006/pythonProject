# 코드업 6063~
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

a, b, c = map(int, input().split())
if (a%2==0):
    print("even")
else:
    print("odd")

if (b%2==0):
    print("even")
else:
    print("odd")

if (c%2==0):
    print("even")
else:
    print("odd")