animal = "Cat"
age = 2

if animal == "Dog":
    if age < 2:
        status = "Puppy Food"
    else:
        status = "Senior Food"
elif animal == "Cat":
    if age < 2:
        status = "Cat Food"
    else:
        status = "Senior Cat Food"
print(status)