# 5-3-1
# def solution(n, k):
#     answer = 0
#
#     while n > 0:
#         # d: n을 k진수로 나타낸 경우, 가장 낮은 자릿수를 나타낸다
#
#         d = n % k
#
#         # n에서 가장 낮은 자릿수 d를 제거한다
#         n = n // k
#
#         answer = answer * k + d
#
#     return answer
#
#
# n, k = map(int, input().split())
# print(solution(n, k))

# 5-3-2
# def solution(n, k):
#     s = 0
#     while n > 0:
#         d = n % k
#         n = n // k
#         s += d
#
#     answer = ''
#     while s > 0:
#         d = s % k
#         s = s // k
#         answer = str(d) + answer
#
#     return answer
#
#
# n, k = map(int, input().split())
# print(solution(n, k))

# 5-3-3
# def solution(A):
#     answer = 0
#
#     for a in A:
#         if check(a):
#             answer += a
#
#     return answer
#
#
# def check(a):
#     if a < 2:
#         return False
#
#     i = 2
#     while i * i <= a:
#         if a % i == 0:
#             return False
#         i += 1
#
#     return True
#
#
# A = list(map(int, input().split()))
# print(solution(A))

# 5-3-4
def parse_log(s):
    return int(s[:2]) * 60 + int(s[3:])


def get_fee(fees, t):

    money = fees[1]

    if fees[0] < t:
        money += (t - fees[0] + fees[2] - 1) // fees[2] * fees[3]

    return money


def solution(fees, A):

    answer = 0

    for t in map(parse_log, A):
        answer += get_fee(fees, t)

    return answer


A = list(input().split())
fees = [100, 10, 50, 3]
print(solution(fees, A))
