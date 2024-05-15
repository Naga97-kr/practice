# 5-1-1
# def get_sum(T, start, end):
#     for t in range(1, 24 * 3600):
#         T[t] += T[t - 1]
#
#     ret = 0
#     for t in range(start, end):
#         ret += T[t]
#     return ret
#
#
# def add_query(T, start, end):
#     T[start] += 1
#     T[end] -= 1
#
#
# def solution(n, A):
#     T = 24 * 3600 * [0]
#     answer = 0
#     for a in A:
#         if a[0] == '1':
#             add_query(T, is_time(a[1]), is_time(a[2]))
#         else:
#             answer = get_sum(T, is_time(a[1]), is_time(a[2]))
#
#     return answer
#
#
# def is_time(S):
#     return int(S[:2]) * 3600 + int(S[3:5]) * 60 + int(S[6:])
#
#
# n = int(input())
# A = list(list(input().split()) for _ in range(n))
# print(solution(n, A))

# 5-1-2
def add_query(psum, i, j, k):
    psum[i] += k
    if j + 1 < n:
        psum[j + 1] -= k


def solution(n, m, A, B):

    psum = [0] * n

    for b in B:
        if b[0] == 1:
            add_query(psum, b[1], b[2], b[3])
        else:
            for i in range(1, n):
                psum[i] += psum[i - 1]

            return sum(psum[b[1]:b[2] + 1]) + sum(A[b[1]:b[2]+ 1])


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(list(map(int, input().split())) for _ in range(m))
print(solution(n, m, A, B))
