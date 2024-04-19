# take number from user between 1 to 10 else retake number 

while True:
    number = int(input("Enter value w/e 1 to 10 : "))
    if 1 <= number <= 10:
        print("Thank you!")
        break
    else:
        print("Invilid number, try again")