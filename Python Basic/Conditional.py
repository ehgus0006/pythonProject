x = 15

if x >= 10:
    print(x)

# 성적이 90점 미만일 때:A
# 성적이 90점 미만, 80점 이상일 때:B
# 성적이 80점 미만, 70점 이상일 때:C
# 성적이 70점 미만일 때:F

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
    
score = 85

if score >= 70:
    print("성적이 70점 이상입니다")
    if score >= 90:
        print("우수한 성적입니다")
else:
    print("성적이 70점 미만입니다")
    print("조금더 분발하세요")

print("프로그램을 종료합니다")

