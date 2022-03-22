from itertools import permutations, product, combinations_with_replacement
from itertools import combinations
# itertools
# 가장 유용한 클래스는 permutations, combinations이다.

# permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.
# permutations는 클래스이므로 객체 초기화 이후에 이후에는 리스트 자료형으로 변환하여 사용한다.

# 리스트['A', 'B', 'C']에서 3개(r=3)를 뽑아 나열하는 경우

data = ['A', 'B', 'C'] #데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산해준다.
data = ['A', 'B', 'C'] #데이터 준비
result = list(combinations(data, 2))
print(result)

# product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산한다.
# 뽑고자 하는 데이터의 수는 repeat 속성값으로 넣어준다.
data = ['A', 'B', 'C'] #데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

# combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아
# 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산한다. 다만 원소를 중복해서 뽑는다.

data = ['A', 'B', 'C'] #데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)

