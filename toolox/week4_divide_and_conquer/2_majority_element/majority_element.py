# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    lElem = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    rElem = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    lCtr = 0
    for i in range(left, right):
        if a[i] == lElem:
            lCtr += 1
    if lCtr > ((right - left) // 2):
        return lElem

    rCtr = 0
    for i in range(left, right):
        if a[i] == rElem:
            rCtr += 1
    if rCtr > ((right - left) // 2):
        return rElem
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
