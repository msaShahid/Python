# compute the factorial of a number using awhile loop

number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1
print(f"factorial of the 5 is {factorial}")