# sum = 0
# for n in range(100000000, 0, -1):
#     sum += n
# print(sum)

def sum_numbers(n, m):
    if n > m:
        max = n
        min = m

    else:
        max = m
        min = n

    foo = ((min+max)*max)/2
    print(foo)
