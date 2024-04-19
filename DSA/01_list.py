# Find The Lowest Value in an Array / List
# Create a variable 'minVal' and set it equal to the first value of the array.
# Go through every element in the array.
# If the current element has a lower value than 'minVal', update 'minVal' to this value.
# After looking at all the elements in the array, the 'minVal' variable now contains the lowest value.

list_array = [7,8,4,9,11,23,12]
minVal = list_array[0] 

for i in list_array:
    if i < minVal:
        minVal = i
print("Lowest value :",minVal)


