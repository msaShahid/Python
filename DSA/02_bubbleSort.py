# Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

# How it works:

# Go through the array, one value at a time.
# For each value, compare the value with the next value.
# If the value is higher than the next one, swap the values so that the highest value comes last.
# Go through the array as many times as there are values in the array.

#my_array = [64, 34, 25, 12, 22, 11, 90, 5]
#my_array = [7, 3, 9, 12, 11]
my_array = [1, 2, 3, 4, 11]

n = len(my_array)

for a in range(n-1):
    swapped = False
    for b in range(n-a-1):
        if my_array[b] > my_array[b+1]:
            my_array[b], my_array[b+1] = my_array[b+1], my_array[b]
            swapped = True
        if not swapped:
            break

print("Bubble Sort :",my_array)
