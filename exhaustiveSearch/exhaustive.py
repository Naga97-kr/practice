from itertools import *


# 4-1-1
# def solution(S, n):
#     answer = []
#
#     for s in combinations(S, n):
#         answer.append(''.join(s))
#         answer.sort()
#
#     return answer
#
#
# S = input()
# n = int(input())
# A = solution(S, n)
# for a in A:
#     print(a)

# 4-1-2
# def solution(n):
#     answer = 0
#
#     for A in range(10 ** (n - 1), 10 ** n):
#         if is_ok(A):
#             answer += 1
#
#     return answer
#
#
# def is_ok(A):
#     p = A % 10
#
#     if p == 0:
#         return False
#
#     while A > 0:
#         c = A % 10
#         A //= 10
#
#         if c == 0 or abs(p - c) > 2:
#             return False
#
#     return True
#
#
# n = int(input())
# print(solution(n))

# 4-1-3

def get_apple(board, aloc, iloc, jloc, kloc):
    cnt = 0

    if in_boundary(iloc) == False or in_boundary(jloc) == False:
        return 0

    if board[iloc[0]][iloc[1]] == -1 or board[jloc[0]][jloc[1]] == -1:
        return 0

    if aloc == jloc:
        return 0

    cnt = board[iloc[0]][iloc[1]] + board[jloc[0]][jloc[1]]

    if in_boundary(kloc) and board[kloc[0]][kloc[1]] == 1 and iloc != kloc:
        cnt += 1

    return cnt


def solution(board, aloc):
    dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for i in range(4):
        for j in range(4):
            for k in range(4):

                iloc = [aloc[0] + dd[i][0], aloc[1] + dd[i][1]]
                jloc = [iloc[0] + dd[j][0], iloc[1] + dd[j][1]]
                kloc = [jloc[0] + dd[k][0], jloc[1] + dd[k][1]]

                if get_apple(board, aloc, iloc, jloc, kloc) >= 2:
                    return 1
    return 0


def in_boundary(loc):
    return 0 <= loc[0] <= 4 and 0 <= loc[1] <= 4


board = list(list(map(int, input().split())) for _ in range(5))
aloc = list(map(int, input().split()))
print(solution(board, aloc))
