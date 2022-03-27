# 코드업 6046~6062
# 기초-비트시프트연산~기초-비교연산~기초-비트논리연산

# 6046
# 정수 1개를 입력받아 2배 곱해 출력해보자.

# n = int(input())
# print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
# print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
# print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
# print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

# 6047
# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# a, b = map(int, input().split())
# print(a<<b) # 2 10 2048 반대부호 /2

# 6048
# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

# a, b= map(int, input().split())
# if a<b:
#     print(True)
# else:
#     print(False)

# 6049
# 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.
# a, b= map(int, input().split())
# if (a==b):
#     print(True)
# else:
#     print(False)

# 6050
# 두 정수(a, b)를 입력받아
# b의 값이 a의 값 보다 크거나 같으면 True 를,
# 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

# a, b= map(int, input().split())
# if (a<=b):
#     print(True)
# else:
#     print(False)

# 6051
# 두 정수(a, b)를 입력받아
# a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.

# a, b= map(int, input().split())
# if (a!=b):
#     print(True)
# else:
#     print(False)

# 6052
# 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
# python 언어에서 정수값 0은 False(거짓)로 평가되고, 그 외의 값들은 모두 True(참)로 평가된다.
# n = int(input())
# print(bool(n))

# 6053
# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.

# a = bool(int(input()))
# print(not a)

# 6054
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

# a,b = map(int, input().split())
# if (bool(a)and bool(b) == True):
#     print(True)
# else:
#     print(False)

# 6055
# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# a,b = map(int, input().split())
# if(bool(a) or bool(b) == True):
#     print(True)
# else:
#     print(False)

# 6056
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.
# a와 b를 정수형으로 입력받은 뒤에 xor 논리연산 (^)이 True라면 True를, 이외에는 False를 출력하도록 하였습니다.

# a,b = map(int, input().split())
# if(bool(a) ^ bool(b) == True):
#     print(True)
# else:
#     print(False)

# 6057
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

# a,b = map(int, input().split())
# if(bool(a) == bool(b)):
#     print(True)
# else:
#     print(False)
#

# 6058
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# a,b = map(int, input().split())
# a,b = bool(a), bool(b)
# if(a == False and b == False):
#     print(True)
# else:
#     print(False)

# 6059
# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.

# a = int(input())
# print(~a)


# 6060
# 두 정수를 비트단위(bitwise)로 and 계산을 수행한 결과를 10진수로 출력한다.
# a,b = map(int, input().split())
# print(a&b)

# 6061
# 두 정수를 비트단위(bitwise)로 or 계산을 수행한 결과를 10진수로 출력한다.
# a,b = map(int, input().split())
# print(a|b)

# 6062
# 두 정수를 비트단위(bitwise)로 xor 계산을 수행한 결과를 10진수로 출력한다.
# a,b = map(int, input().split())
# print(a^b)

