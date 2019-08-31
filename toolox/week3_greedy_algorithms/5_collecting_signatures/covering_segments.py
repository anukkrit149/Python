# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(seg):
    points = []
    seg = sorted(seg, key=attrgetter('end'))
    max = seg[0].end
    points.append(max)
    i = 1
    while i < len(seg):
        if max < seg[i].start:

            max = seg[i].end

            points.append(max)
        i += 1

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
