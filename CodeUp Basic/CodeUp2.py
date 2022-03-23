# 코드업 6009~6024

# 6009

# c = input()
# print(c)

# 6010

# n = int(input())
# print(n)

# 6011
#
# n = float(input())
# print(n)

# 6012
# a = input()
# b = input()
#
# print(a)
# print(b)

# 6013
# a = input()
# b = input()
#
# print(a)
# print(b)

# 6014
# a = float(input())
# print(a)
# print(a)
# print(a)

# 6015
# a ,b = input().split()
# print(a)
# print(b)

# 6016
# c1,c2 = input().split()
# print(c2, c1)


# 6017
# s = input()
# print(s, s, s)

# 6018
# a, b = input().split(':')
# print(a, b, sep=':')

# 6019
# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
# y,m,d = input().split('.')
# print(d,m,y, sep="-")

# 6020
# 주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다.
# (입력값은 가상의 주민번호이다.)
# ex)110011-0000000
# f, r = input().split("-")
# print(f,r,sep='')


# 6021
# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

# 문자열을 변수 a에 input() 함수로 입력받고, 문자열 인덱싱을 사용해줍니다.
# 문자열의 첫 번째 글자(인덱싱 넘버는 0)는 a[0], 문자열의 두 번째 글자(인덱싱 넘버는 1)는 a[1]
# s = input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

# 6022
# s[a:b] 라고 하면, s라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분을 의미한다.
# s = input()
# print(s[0:2], s[2:4], s[4:])

# 6023
# 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
# 입력예시 17:23:57 출력 23
# h, m, s = input().split(":")
# print(m)

# 6024
# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
# 순서대로 붙여 출력하는 프로그램을 작성해보자.

w1, w2 = input().split()
print(w1 + w2)







