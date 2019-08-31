# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fib_last_fast(n):
    a, b = 0, 1
    for _ in range(n - 1):
        c = a + b
        c = c % 10
        b, a = c, b

    return c


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    # print(n)
    print(get_fib_last_fast(n))
