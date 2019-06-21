#BMI标准
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.75
weight = 72

BMI = weight / (height * height)

def result(bmi):
    if bmi <= 18.5:
        return "过轻"
    elif bmi <= 25:
        return "正常"
    elif bmi <= 28:
        return "过重"
    elif bmi <= 32:
        return "肥胖"
    else:
        return "严重肥胖"

print(result(BMI))
