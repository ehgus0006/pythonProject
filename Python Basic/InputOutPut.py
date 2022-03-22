# 입력을 위한 전형적인 소스코드

# 데이터 개수 입력
# n = int(input())

# 각 데이터를 공백으로 구분하여 입력 정수형을 여러개 받을려면 map을 이용하여 해당 리스트의 모든 원소에 int()를 적용해야한다.
# data = list(map(int, input().split()))
# data = list(input().split())

# data.sort(reverse=True)
# print(data)

# n,m,k를 공백으로 구분하여 입력
n,m,k = input().split()

print(n, m , k)

answer = 7
print(f"정답은 {answer} 입니다.")

