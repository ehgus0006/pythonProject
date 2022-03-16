# 집합 자료형
# 파이썬에서는 집합을 처리하기 위한 집합 자료형을 제공하고 있다.
# 집합은 기본적으로 리스트 혹은 문자열을 이용해서 만들 수 있는데, 다음과 같은 특징이 있다.

# 중복을 허용하지 않는다.
# 순서가 없다.

# 집합 자료형 초기화 방법
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형의 연산

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) #합집합
print(a & b) #교집합
print(a - b) #차집합

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

