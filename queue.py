# 2-4-1

from collections import deque
# def solution(n, A):
#     answer = [0, 0]
#
#     q = deque()
#
#     for info in A:
#         if info[0] == 1:
#             q.append(info[1])
#             if answer[0] < len(q) or (answer[0] == len(q) and answer[1] > info[1]):
#                 answer = [len(q), info[1]]
#         else:
#             q.popleft()
#
#     return answer
#
#
# n = int(input())
# A = list(list(map(int, input().split())) for _ in range(n))
# B = solution(n, A)
# print(B[0], B[1])

# 2-4-2
# def solution(n, S):
#     answer = [[] for _ in range(3)]
#
#     q = deque()
#     menu = deque()
#
#     for info in S:
#         if info[0] == 1:
#             q.append((info[1],info[2]))
#         else:
#             menu.append(info[1])
#
#     for a in range(len(q)):
#         i, j = q.popleft()
#         k = 0
#         if menu:
#             k = menu.popleft()
#
#         print(i, j, k)
#         if j == k:
#             answer[0].append(i)
#         else:
#             answer[1].append(i)
#
#     while len(q) > 0:
#         i, j = q.popleft()
#         answer[2].append(i)
#
#     for i in range(3):
#         answer[i].sort()
#     return answer
#
#
# n = int(input())
# S = list(list(map(int, input().split())) for _ in range(n))
# T = solution(n, S)
# for t in T:
#     if len(t) == 0:
#         print("None")
#     else:
#         for x in t:
#             print(x, end=' ')
#         print()
