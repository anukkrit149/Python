# Uses python3
import sys


def get_change(m):
    ctr = 0
    while m > 0:
        if m >= 10:
            ctr += m // 10
            m %= 10
        elif m >= 5:
            ctr += m // 5
            m %= 5
        else:
            ctr += m
            break
    return ctr


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
