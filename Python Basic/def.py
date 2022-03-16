# 함수

def add(a,b):
    return a + b

print(add(3,5))

def add(a,b):
    print("함수의 결과 : ", a+b)

add(3,5)

def add(a,b):
    print('함수의 결과 : ', a+b)

add(a = 3, b = 5)

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

def add(a,b):
    return a + b

# 일반적인 add() 메소드 사용
print(add(3,5))

# 람다 표현식으로 구현한 add() 메소드
print((lambda a,b: a+b)(3,5))