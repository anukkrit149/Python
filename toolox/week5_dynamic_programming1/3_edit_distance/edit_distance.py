# Uses python3
def edit_distance(s, t):
    Slen = len(s) + 1
    Tlen = len(t) + 1

    dist = [[x] + [0] * (Tlen - 1) for x in range(Slen)]
    dist[0] = [x for x in range(Tlen)]

    for i in range(1, Slen):
        for j in range(1, Tlen):
            if s[i - 1] == t[j - 1]:
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min(dist[i][j - 1], dist[i - 1][j], dist[i - 1][j - 1]) + 1

    return dist[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
