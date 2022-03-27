# 코드업 6032~6045
# 기초-산술연산

# 6032
# 부호 바꾸기
# n = int(input())
# print(-n)

# 6033
# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

# chr( )는 정수값->문자,
# ord( )는 문자->정수값 형태로 바꿔주는 서로 반대 방향으로 바꾸어 주는 기능을 한다.
# 풀이
# 먼저 input() 함수로 입력값을 받은 다음 ord() 함수로 묶어 입력받은 문자를 아스키 코드값으로 변환해줍니다.
# 변환한 아스키 코드값에 1을 더해주어 다음 문자로 변환한 뒤에 변환한 값을 chr() 함수로 유니코드 문자 형태로 출력하면 됩니다.
# n = ord(input())
# print(type(n))
# print(chr(n+1))

# 6034
# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

# a, b = map(int, input().split())
# print(a-b)

# 6035
# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

# a, b = map(float, input().split())
# print(a*b)

# 6036
# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.
#
# w, n = input().split()
# print(w*int(n))

# 6037
# 반복 횟수와 문장을 입력받아 여러 번 출력해보자.
# n = input()
# s = input()
#
# print(s*int(n))

# 6038

# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.
# a, b = map(int, input().split())
# print(a**b)

# 6039
# 실수 2개(f1, f2)를 입력받아
# f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

# a, b = map(float, input().split())
# print(a**b)


# 6040
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
# a, b = map(int, input().split())
# print(a//b)

# 6041
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
# a, b = map(int, input().split())
# print(a%b)

# 6042
# 실수 1개를 입력받아
# 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.
# a = float(input())
# print(format(a, ".2f"))

# 6043
# 실수 2개(f1, f2)를 입력받아
# f1 을 f2 로 나눈 값을 출력해보자.
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

# a, b = map(float, input().split())
# print(format(a/b, ".3f"))

# 6044
# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단 0 <= a, b <= 2147483647, b는 0이 아니다.
# round() 함수를 사용해도된다
#
# a,b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(format(a/b, ".2f"))
# print(round(a/b,2))

# 6045
# 정수 3개를 입력받아 합과 평균을 출력해보자.

a, b, c = map(int, input().split())
sum = a+b+c
avg = sum/3
print(sum, format(avg, '.2f'))


