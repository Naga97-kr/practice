# 5-2-1
from bisect import *
#
#
# def solution(n, m, A, B):
#     answer = []
#
#     A.sort()
#     for k in B:
#         i = bisect_left(A, k)
#         answer.append(n - i)
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

# 5-2-2
# def solution(n, m, A, B):
#     answer = []
#
#     A.sort()
#     for k in B:
#         i = bisect_right(A, k)
#         answer.append(n - i)
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

# 5-2-3
def solution(n, m, A, B):
    answer = []

    A.sort()
    for i, j in B:
        i = bisect_left(A, i)
        j = bisect_right(A, j)
        a = n - i
        b = n - j
        answer.append(a - b)

    return answer


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(list(map(int, input().split())) for _ in range(m))
C = solution(n, m, A, B)
for c in C:
    print(c)
