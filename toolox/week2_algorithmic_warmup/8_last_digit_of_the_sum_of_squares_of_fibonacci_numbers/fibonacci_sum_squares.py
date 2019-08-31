# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fib_fast(n):
    if n==0:
        return 0
    if n==1:
        return 1
    f = [None] * n
    f[0] = 1
    f[1] = 1
    sum = 2
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
        sum += f[i]**2

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fib_fast(n))
