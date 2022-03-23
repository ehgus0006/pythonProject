# 코드업 6025~6031
# 기초 값변환 ~ 출력변환


# 6025

# 파이썬에서 input().split()으로 입력받은 변수들을 정수값으로 변환하기 위해서는 map() 함수로 묶어주어야 합니다.
# map() 함수에서 int형을 선언해주고 input().split() 문을 사용하면 됩니다.
# a, b = input().split()
# print(int(a)+int(b))

# a, b = map(int, input().split())
# print(a+b)

# 6026

# 실수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

# a = float(input())
# b = float(input())
# print(a+b)

# 6027

# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
# 소문자 x는 소문자 형태로 출력된다
# 8진수는 o

# a = int(input())
# print("%x"% a)

# 6028
# 대문자 X를 사용하면 대문자 형태로 출력된다

# a = int(input())
# print("%X"% a)

# 6029

# 밑 내가작성한 코드
# a = int(input(), 16)
# print("%o"%a)

# 타인이 작성한 코드
# print("%o" %int(input(),16))

# 6030
# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.

# n = ord(input())
# print(n)

# 6031
# 10진 정수 1개를 입력받아
# 유니코드 문자로 출력해보자.

# chr( )는 정수값->문자,
# ord( )는 문자->정수값 형태로 바꿔주는 서로 반대 방향으로 바꾸어 주는 기능을 한다.

# c = int(input())
# print(chr(c))

