# count the positive numbers in given list
numbers = [1,-2,3,-4,5,-6,7,-8,9,-10]
positive_num_count = 0

for num in numbers:
    if num > 0:
        positive_num_count +=1
print("Final count of Positive number in list ", positive_num_count)
