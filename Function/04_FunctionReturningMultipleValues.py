import math

def circle_stats(radius):
    area = round(math.pi * radius ** 2,4)
    circumference = round(2 * math.pi  * radius,2)
    return area,circumference

a, c = circle_stats(3)
print("Area: ",a ,"Circumference: ", c)