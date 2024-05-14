# 4-2-1
# def solution(A):
#     solve(A, 0)
#
#
# def solve(A, B):
#     if A != 0:
#
#         if A % 10 != 0 or B == 1:
#             print(A % 10, end='')
#             B = 1
#
#         solve(A // 10, B)
#
#
# A = int(input())
# solution(A)

# 4-2-2
# def solve(n):
#     if n == 1:
#         return 1
#
#     return n + solve(n - 1)
#
#
# def solution(n):
#     return solve(n)
#
#
# n = int(input())
# print(solution(n))

# 4-2-3
# def solve(n):
#     if n < 3:
#         return 1
#
#     return solve(n - 1) + solve(n - 2)
#
#
# def solution(n):
#     return solve(n)
#
#
# n = int(input())
# print(solution(n))

# 4-2-4
# def solve(A, n):
#     m = len(A)
#
#     if m == n:
#         return 1
#
#     if m == 0:
#         s, e = 1, 9
#     else:
#         s = max(A[m - 1] - 2, 1)
#         e = min(A[m - 1] + 2, 9)
#
#     ret = 0
#     for a in range(s, e + 1):
#         A.append(a)
#         ret += solve(A, n)
#         A.pop()
#
#     return ret
#
#
# def solution(n):
#     return solve([], n)
#
#
# n = int(input())
# print(solution(n))

# 4-2-5
def in_range(loc):
    return 0 <= loc[0] <= 4 and 0 <= loc[1] <= 4


def solve(board, aloc, apple_num):
    if apple_num == 0:
        return 0

    ret = -1

    dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for dr, dc in dd:
        r, c = dr + aloc[0], dc + aloc[1]
        if in_range([r, c]) and board[r][c] != -1:
            prev = board[aloc[0]][aloc[1]]
            board[aloc[0]][aloc[1]] = -1

            cur_ret = solve(board, [r, c], apple_num - board[r][c])

            if cur_ret != -1:
                cur_ret += 1

            if cur_ret != -1:
                if ret == -1 or cur_ret < ret:
                    ret = cur_ret

            board[aloc[0]][aloc[1]] = prev

    return ret


def solution(board, aloc):
    return solve(board, aloc, 3)


board = list(list(map(int, input().split())) for _ in range(5))
aloc = list(map(int, input().split()))
print(solution(board, aloc))
