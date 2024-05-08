# 2-2-1
# def solution(A):
#     # 두 번째 문자 A[1]부터 인덱스를 2씩 증가하면서 문자열 B를 만든다
#     B = A[1::2]
#     return B
#
#
# A = input()
# print(solution(A))

# 2-2-2
# def solution(A):
#     B = ''
#     for a in A:
#         if a.islower():
#             B += a
#     return B
#
#
# A = input()
# print(solution(A))

# 2-2-3
# def solution(A):
#     B = A.upper()
#     return B
#
#
# A = input()
# print(solution(A))

# 2-2-4
# def solution(A, B):
#     for b in B:
#         A = A.replace(b, b.lower())
#     return A
#
#
# A = input()
# B = list(map(str, input().split()))
# print(solution(A, B))

# 2-2-5
def parse_log(s):
    return int(s[0:2]) * 60 + int(s[3:5])


def solution(A):
    total_time = 0

    for t in map(parse_log, A):
        total_time += t

    hour = total_time / 60
    minute = total_time % 60

    ret = ''
    if hour < 100:
        ret = '%02d:%02d' % (hour, minute)
    else:
        ret = '%d:%02d' % (hour, minute)

    return ret


A = list(input().split())
print(solution(A))
