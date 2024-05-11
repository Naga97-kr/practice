# 3-1-1
# def solution(n, m ,A, B):
#     answer = []
#     for b in B:
#         cnt = 0
#         for a in A:
#             if b <= a:
#                 cnt += 1
#         answer.append(cnt)
#
#     return answer
#
#
# n, m = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(int(input()) for _ in range(m))
# C = solution(n, m, A, B)
# for c in C:
#     print(c)

# 3-1-2
# def solution(n, m, A, B):
#     answer = []
#
#     for b in B:
#         if b == '-':
#             answer.append(n)
#         else:
#             cnt = 0
#             for a in A:
#                 if b == a:
#                     cnt += 1
#             answer.append(cnt)
#
#     return answer
#
#
# n, m = map(int, input().split())
# A = list(input().split())
# B = list(input() for _ in range(m))
# C = solution(n, m, A, B)
# for c in C:
#     print(c)

# 3-1-3
# def solution(board, n, m):
#     dd = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
#     for dr, dc in dd:
#         r, c = n + dr, m + dc
#         if in_range(r, c) and board[r][c] == 1:
#             print(r, c)
#             return 1
#     return 0
#
#
# def in_range(r, c):
#     return 0 <= r <= 4 and 0 <= c <= 4
#
#
# board = list(list(map(int, input().split())) for _ in range(5))
# n, m = map(int, input().split())
# print(solution(board, n, m))

# 3-1-4
# def solution(A, B):
#     answer = []
#
#     for b in B:
#         if b[0] == 1:
#             for i in range(b[1], b[2]+1):
#                 A[i] += b[3]
#         else:
#             temp = 0
#             for i in range(b[1], b[2]+1):
#                 temp += A[i]
#             answer.append(temp)
#
#     return answer
#
#
# n, m = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(list(map(int, input().split())) for _ in range(m))
# C = solution(A, B)
# for c in C:
#     print(c)

# 3-1-5
def solution(n, m, A, B):
    answer = []

    for b in B:
        if b[0] == 1:
            do_sum(A, b[1], b[2], b[3], b[4], b[5])
        else:
            temp = 0
            for i in range(b[1], b[3] + 1):
                for j in range(b[2], b[4] + 1):
                    temp += A[i][j]
            answer.append(temp)
    return answer

def do_sum(board, i1, j1, i2, j2, k):
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            board[i][j] += k


n, m = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
B = list(list(map(int, input().split())) for _ in range(m))
C = solution(n, m, A, B)
for c in C:
    print(c)
