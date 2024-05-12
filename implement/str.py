# 3-2-1
# def solution(S, k):
#
#     while len(S) < k:
#         S += S[-1]
#     return S
#
#
# A = input()
# k = int(input())
# print(solution(A, k))
import itertools


# 3-2-2
# def solution(S):
#     T = ''
#     i = 0
#     while i < len(S):
#         # a, A가 아닌 값 T에 등록
#         if S[i] != 'a' and S[i] != 'A':
#             T += S[i]
#             i += 1
#             continue
#
#         # a or A의 다음 값 찾기
#         # 다음 값이 a, A면 j에 1을 더함
#         j = i + 1
#         while j < len(S):
#             if S[j] != 'a' and S[j] != 'A':
#                 break
#             j += 1
#
#         # j - i가 a의 개수
#         # 1이면 그대로 작성
#         # 2이상 a로 변경
#         if j - i == 1:
#             T += S[i]
#         else:
#             T += S[i].lower()
#         i = j
#
#     return T
#
#
# S = input()
# print(solution(S))

# 3-2-3
# def solution(S):
#     T = sorted(S)
#
#     B = ''.join(T)
#
#     return B
#
#
# S = input()
# print(solution(S))

# 3-2-4
# def solution(n, A):
#     T = [0] * 3600
#     answer = []
#     for a in A:
#         if a[0] == '1':
#             do_add(T, translate_time(a[1]), translate_time(a[2]))
#         else:
#             answer.append(T[translate_time(a[1])])
#     return answer
# 
# 
# # 00:10 < 형식의 시간을 분 혹은 초로 변경
# def translate_time(t):
#     return int(t[:2]) * 60 + int(t[3:])
# 
# 
# def do_add(T, i, j):
#     for p in range(i, j):
#         T[p] += 1
# 
# 
# n = int(input())
# A = list(list(input().split()) for _ in range(n))
# B = solution(n, A)
# for b in B:
#     print(b)

# 3-2-5
# def solution(A):
#     S = itertools.permutations(A, len(A))
#
#     answer = []
#
#     for s in S:
#         answer.append(''.join(s))
#         answer.sort()
#
#     return answer
#
#
# A = input()
# B = solution(A)
# for b in B:
#     print(b)
