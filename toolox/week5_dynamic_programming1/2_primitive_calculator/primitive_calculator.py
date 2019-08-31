# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def new_sequence(n):
    Ocount = [0] * (n + 1)

    Ocount[1] = 1
    for i in range(2, n + 1):
        countI = [i - 1]
        if i % 2 == 0:
            countI.append(i // 2)
        if i % 3 == 0:
            countI.append(i // 3)

        min_count = min([Ocount[x] for x in countI])
        Ocount[i] = min_count + 1

    current_value = n
    value_trail = [current_value]
    while current_value != 1:
        option_list = [current_value - 1]
        if current_value % 2 == 0:
            option_list.append(current_value // 2)
        if current_value % 3 == 0:
            option_list.append(current_value // 3)

        current_value = min(
            [(c, Ocount[c]) for c in option_list],
            key=lambda x: x[1]
        )[0]
        value_trail.append(current_value)
    return reversed(value_trail)


input = sys.stdin.read()
n = int(input)
sequence = list(new_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
