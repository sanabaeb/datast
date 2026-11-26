def count_down(n):
    if n <= 0:
        return
    print(n)
    count_down(n - 1)
    m = n-1
    count_down(m)

def gugu(dan, num=1):
    gugu(dan, num + 1)

for i  in range(2, 10):
    gugu(i)

def pow(base, exponent):
    if exponent == 0:
        return 1
    else:
        print("base:", base, "exponent:", exponent)
        return base * pow(base, exponent - 1)

print(pow(2, 4))


def arr_sum(arr, n):
    if n <= len(arr):
        return 0
    else:
        return arr[n - 1] + arr_sum(arr, n - 1)

foo = [1, 2, 3, 4, 5]
print(arr_sum(foo, len(foo)))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

    
