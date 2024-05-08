# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solution(n, A, i1, j1, i2, j2, k):
    for i in range(i1, i2+1):
        for j in range(j1, j2+1):
                A[i][j] *= k

    answer = 0
    for i in range(n):
        answer += sum(A[i])
    return answer


n = int(input())
A = list(list(map(int, input().split())) for _ in range(n))
i1, j1, i2, j2, k = map(int, input().split())
print(solution(n, A, i1, j1, i2, j2, k))
