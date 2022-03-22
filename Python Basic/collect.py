# collections
# collections 라이브러리의 기능 중에서 코딩 테스트에서 유용하게 사용되는 클래스는 deque와 Counter 이다.

# 보통 파이썬에서는 deque를 사용해 큐를 구현한다. 별도로 제공하는 Queue 라이브러리가 있는데
# 일반적인 큐 자료구조를 구현하는 라이브러리는 아니다. 따라서 deque를 사용해야 한다.

# 기본 리스트
# 가장 앞쪽에 원소 추가 O(N), 가장 뒤쪽에 원소 추가O(1)
# 가장 앞쪽에 있는 원소 제거 O(N), 가장 뒤쪽에 있는 원소 제거O(1)

# deque 4개다 O(1)
# deque에서는 리스트 자료형과 다르게 인덱싱, 슬라이싱 기능은 사용할수 없지만
# 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적으로 사용될 수 있다.

# deque는 첫 번째 원소 제거할 때 popleft()를 사용하며, 마지막 원소를 제거할 때 pop()을 사용한다
# 또한 첫 번째 인덱스에 원소 x를 삽입할 때 appendleft(x)를 사용하며, 마지막 인덱스에 원소를 삽입할 때 append(x)를 사용한다.

# 스택과 큐의 기능을 모두 포함함

# 리스트 [2, 3, 4]의 가장 앞쪽과 뒤쪽에 원소를 삽입하는 예시는 다음과 같다
from collections import deque
from collections import Counter

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# Counter는 구체적으로 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전 자료형으로 변환



