# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(n, A, k):
    answer = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == k:
                answer += 1
    return answer


n, k = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))
print(solution(n, A, k))
