# 2-3-1
# def solution(n, m, A, B):
#     D = {}
#     for name, cost in A:
#         D[name] = int(cost)
#
#     answer = 0
#     for name in B:
#         answer += D[name]
#
#     return answer
#
#
# n, m = map(int, input().split())
# A = list(list(input().split()) for _ in range(n))
# B = list(input().split())
# print(solution(n, m, A, B))

# 2-3-2
# def solution(S):
#     D = {}
#     for s in S.split():
#         if s in D:
#             D[s] += 1
#         else:
#             D[s] = 1
#
#     answer = list(D.items())
#     answer.sort()
#     return answer
#
#
# S = input()
# A = solution(S)
# for name, cnt in A:
#     print(name, cnt)

# 2-3-3
# def solution(A, B):
#     D = {}
#     for b in B.split():
#         if b in D:
#             D[b] += 1
#         else:
#             D[b] = 1
#
#     answer = []
#     for a in A.split():
#         if a not in D:
#             answer.append(a)
#     answer.sort()
#     return answer
#
#
# A = input()
# B = input()
# S = solution(A, B)
# for name in S:
#     print(name)

# 2-3-4
# def solution(A, B):
#     D = {}
#     for a in A.split():
#         for i in range(len(a) - 1):
#             x = a[:i + 1]
#             if x in D:
#                 D[x] += 1
#             else:
#                 D[x] = 1
#
#     if B in D:
#         return D[B]
#     else:
#         return 0
#
#
# A = input()
# B = input()
# print(solution(A, B))

# 2-3-5
# def solution(n, A):
#     D = {}
#     mx = 0
#     for a in A:
#         if a in D:
#             D[a] += 1
#         else:
#             D[a] = 1
#         mx = max(mx, D[a])
#
#     answer = []
#     for key, value in D.items():
#         if value == mx:
#             answer.append(key)
#     answer.sort()
#     return answer
#
#
# n = int(input())
# A = map(int, input().split())
# B = solution(n, A)
# for i in B:
#     print(i, end=' ')
