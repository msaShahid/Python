# Find the first Non-Repeated character

str_list = "teeteracdacd"

for char in str_list:
   # print(char)
    if str_list.count(char) == 1:
        print("First Character :",char)
        break