# --------------------- 1
username = "Shahid"

def login():
    #username = "MD Shahid"
    print(username)

# print(username)
# login()

# --------------------- 2
val1 = 78

def digitSum(val2):
    sum = val1 + val2
    return sum

result = digitSum(22)
#print(result)

# ----------------- 3
x = 99
def f1():
    x =88
    def f2():
        print(x)
    return f2
result1 = f1()
result1()

# ------------------- 4
