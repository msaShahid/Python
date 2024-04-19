def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5,6,7,8,9,))
# print(sum_all(1,2,3,23,4,5))