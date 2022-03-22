# bisect
# 파이썬에서 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다.
# bisect 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다. bisect 라이브러리에서는
# bisect_left() 함수와 bisect_right() 함수가 가장 중요하게 사용되며, 이 두 함수의 시간 복잡도는 O(NlogN)에 동작한다.

# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print("오른쪽 인덱스", right_index)
    print("왼쪽 인덱스", left_index)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))