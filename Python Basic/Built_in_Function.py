# 코딩 테스트를 준비하면서 반드시 알아야 하는 라이브러리 6가지
# 내장 함수: print(), input()과 같은 기본 입출력 기능부터 sorted()과 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리 이다.
# 파이썬 프로그래밍을 작성하는데 없어서는 안 되는 필수적인 기능을 포함하고 있다.
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리이다.
# 순열과 조합 라이브러리를 제공한다.
# heapq : 힙(Heap) 기능을 제공하는 라이브러리이다. 우선순위 큐 기능을 구현하기 위해 사용한다.
# bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리이다.
# collections : 덱(deque), 카운터(Counter)등의 유용한 자료구조를 포함하고 있는 라이브러리이다.

# sum 함수는 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환한다.
result = sum([1, 2, 3, 4, 5])
print(result)

result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

# eval 함수는 수학 수식이 문자열로 들어오면 해당 수식을 계산한다.
result = eval("(3+5) * 7")
print(result)

# sorted() 함수는 iterable 객체가 들어왔을 때, 정렬된 결과를 반환한다.
# key 속성으로 정렬 기준을 명시할 수 있다.

result = sorted([9,1,8,5,4])
print(result)

result = sorted([9,1,8,5,4], reverse=True)
print(result)

# 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있어서, 굳이 위에처럼 사용하지않아도 된다.

data = [9,1,8,5,4]
data.sort()
print(data)



