# Multiplication table printer

number = 3

for i in range (1, 11):
    if i == 5:
        continue
    print(number, "X", i,"=", number*i)