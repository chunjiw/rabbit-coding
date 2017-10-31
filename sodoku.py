# You’re given a 9x9 grid of numbers. Verify that each number from 1 to 9 appears exactly once in each row, column, and each of the 9 3x3 sub-blocks.

# These are the sub-blocks, labeled A-I:

# AAABBBCCC
# AAABBBCCC
# AAABBBCCC
# DDDEEEFFF
# DDDEEEFFF
# DDDEEEFFF
# GGGHHHIII
# GGGHHHIII
# GGGHHHIII

import collections


def is_valid(solution):
    if not solution:
        return False
    s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    dcol = set()
    drow = set()
    d = set()

    for i in range(9):
        for j in range(9):
            dcol.add(solution[i][j])
            drow.add(solution[j][i])
        if s != dcol or s != drow:
            return False
        dcol = {}
        drow = {}

    for j in range(3):
        for k in range(3):
            for ji in range(3):
                for ki in range(3):
                    d.add(solution[j * 3 + ji][k * 3 + ki])
                    if d != s:
                        return False

    return True
