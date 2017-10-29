# hacker rank

# !/bin/python3

import heapq


def main():
    n = 3
    a = [94455, 20555, 20535]
    left, right = [], []
    for a_i in range(n):
        a_t = a[a_i]

        if a_i == 0:
            left.append(-a_t)
            print(a_t)
            continue

        if a_i == 1:
            if a_t >= -left[0]:
                right.append(a_t)
            else:
                right.append(-left.pop())
                left.append(-a_t)
            print((-left[0] + right[0]) / 2)
            continue

        if a_t <= -left[0]:
            heapq.heappush(left, -a_t)
        else:
            heapq.heappush(right, a_t)

        if len(left) < len(right):
            while len(left) + 1 < len(right):
                heapq.heappush(left, -heapq.heappop(right))

        if len(left) > len(right):
            while len(left) > len(right) + 1:
                heapq.heappush(right, -heapq.heappop(left))

        if len(left) == len(right):
            print(float(-left[0] + right[0]) / 2)
        elif len(left) + 1 == len(right):
            print(right[0])
        elif len(left) == len(right) + 1:
            print(-left[0])


if __name__ == "__main__":
    main()

