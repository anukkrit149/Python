# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fib_fast(n):
    if n <= 1:
        return n
    p = 0
    c = 1
    for i in range(n - 1):
        p, c = c % 10, (p + c) % 10

    return c


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fib_fast(n))
