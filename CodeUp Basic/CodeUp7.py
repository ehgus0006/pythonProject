# 6071~
# 기초-반복실행구조~

# 6071
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

# while True:
#     a = int(input())
#
#     if(a==0):
#         break
#     else:
#         print(a)

# 6072
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
# n = int(input())
# while (n!=0):
#         print(n)
#         n -= 1
#         if(n==0): # 이밑ㅇ ㅔ 두개는 없어도 실행됨
#             break

# 6073
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

# n = int(input())
# while (n!=0):
#         n -= 1
#         print(n)
#         if(n==0): # 이밑ㅇ ㅔ 두개는 없어도 실행됨
#             break

# 6074
# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
# 알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
# chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.
# c = ord(input())
# t = ord("a")
#
# while (t<=c):
#     print(chr(t), end=' ')
#     t += 1

# 6075
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

# a = int(input())
# n = 0
# while(n<=a):
#     print(n)
#     n += 1

# 6076
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
# range(끝)
# range(시작, 끝)
# range(시작, 끝, 증감)

# a = int(input())
#
# for i in range(a+1):
#     print(i)

# 6077
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# n = int(input())
# s = 0
# for i in range(1, n+1):
#     if(i % 2 == 0):
#         s += i
#
# print(s)

# 6078
# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
#
# while (True):
#     n = input()
#     if(n== 'q'):
#         break
#     else:
#         print(n)

# 6079
# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

# 즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
# 어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

# n = int(input())
# i = 0
# s = 0
# while(i <= n):
#     s += i   # 그값을 s에 저장
#     if(s>=n):
#         print(i)
#         break
#     i += 1

# 6080
# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
# 나올 수 있는 모든 경우를 출력해보자.
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)


