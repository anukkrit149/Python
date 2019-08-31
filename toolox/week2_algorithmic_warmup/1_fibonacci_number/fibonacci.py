# Uses python3
# import array

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def fib_fast(n):
    if n==0:
        return 0
    if n==1:
        return 1
    f = [None] * n
    f[0] = 1
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]

    return f[n-1]




n = int(input())
print(fib_fast(n))
