# 문자열 초기화

data = 'Hello World'
print(data)

data = "Don't you Know \"Python\"?"
print(data)

# 문자열 연산

a = "Hello"
b = "World"

print(a + " " + b)

a = "String"
print(a*3)

a = "ABCDEF"
print(a[2:4])

# 튜플 자료형

# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용한다.
# 리스트는 가변형, 튜플은 불변

a = (1, 2, 3, 4)
print(a)
# 대입 연산자를 이용한 값변경은 튜플은은적용되지 않는다.
# a[2] = 7
# print(a)