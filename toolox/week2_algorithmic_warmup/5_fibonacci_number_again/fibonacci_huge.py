# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fib(n):
    if n <= 1:
        return n
    p = 0
    c = 1
    for i in range(n - 1):
        p, c = c, p + c
    return c


def get_fib_len(m):
    p = 0
    c = 1
    for i in range(m * m + 1):
        p, c = c, (p + c) % m
        if p == 0 and c == 1:
            return i + 1


def get_fib_huge_fast(n, m):
    rem = n % get_fib_len(m)
    return get_fib(rem) % m


if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fib_huge_fast(n, m))
