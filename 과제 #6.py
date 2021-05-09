def std_weight(height, gender) :
    if height > 100 :
        height /= 100
    if gender == "남자" :
        weight = height ** 2 * 22
        return weight
    elif gender == "여자" : 
        weight = height ** 2 * 21
        return weight

height = float(input("키: "))
gender = input("남자 or 여자: ")
weight = std_weight(height, gender)
if height < 100:
    height *= 100
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))