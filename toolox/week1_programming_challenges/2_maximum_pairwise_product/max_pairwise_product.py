# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    if n > 1:
        max_product = 1
        max_n = max(numbers)
        index = numbers.index(max_n)
        numbers.pop(index)
        max_product *= max_n
        max_n = max(numbers)
        # index = numbers.index(max_n)
        max_product *= max_n
    else:
        max_product = numbers[0]

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
