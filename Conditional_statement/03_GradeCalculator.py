# Grade calcultor

scroe = 67

if scroe >= 101:
    print("Scroe can not be more than 100")
    exit()

if scroe >= 90:
    grade="A"
elif scroe >=80:
    grade="B"
elif scroe >= 70: 
    grade="C"
elif scroe >= 60:
    grade="D"
else:
    grade="F"

print("Grade : ", grade)