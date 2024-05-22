# 6-1-1
from collections import deque


# def in_range(nr, nc):
#     return 0 <= nr <= 4 and 0 <= nc <= 4
#
#
# def bfs(board, sr, sc, tr, tc):
#     dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#     visited = [[0] * 5 for _ in range(5)]
#     dist = [[0] * 5 for _ in range(5)]
#
#     q = deque()
#     q.append([sr, sc])
#
#     visited[sr][sc] = 1
#     dist[sr][sc] = 0
#
#     while len(q) != 0:
#         r, c = q.popleft()
#
#         if r == tr and c == tc:
#             return dist[r][c]
#
#         for dr, dc in dd:
#             nr = r + dr
#             nc = c + dc
#
#             if in_range(nr, nc) and visited[nr][nc] == 0 and board[nr][nc] != -1:
#                 q.append([nr, nc])
#                 dist[nr][nc] = dist[r][c] + 1
#                 visited[nr][nc] = 1
#
#     return -1
#
#
# def solution(board, sr, sc):
#     tr, tc = 0, 0
#     for r in range(5):
#         for c in range(5):
#             if board[r][c] == 1:
#                 tr, tc = r, c
#
#     return bfs(board, sr, sc, tr, tc)
#
#
# board = list(list(map(int, input().split())) for _ in range(5))
# sr, sc = map(int, input().split())
# print(solution(board, sr, sc))

# 6-1-2
# def in_range(nr, nc):
#     return 0 <= nr <= 4 and 0 <= nc <= 4
#
#
# def bfs(board, sr, sc, tr, tc):
#     dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#     visited = [[0] * 5 for _ in range(5)]
#     dist = [[0] * 5 for _ in range(5)]
#
#     visited[sr][sc] = 1
#     dist[sr][sc] = 0
#
#     q = deque()
#     q.append([sr, sc])
#
#     while len(q) != 0:
#         r, c = q.popleft()
#
#         if r == tr and c == tc:
#             return dist[r][c]
#
#         for dr, dc in dd:
#             nr = r + dr
#             nc = c + dc
#
#             if in_range(nr, nc) and visited[nr][nc] == 0 and board[nr][nc] != -1:
#                 q.append([nr, nc])
#                 dist[nr][nc] = dist[r][c] + 1
#                 visited[nr][nc] = 1
#
#     return -1
#
#
# def solution(board, sr, sc):
#     target = list([] for _ in range(6))
#     for r in range(5):
#         for c in range(5):
#             if board[r][c] > 0:
#                 target[board[r][c] - 1] = [r, c]
#
#     answer = 0
#     r, c = sr, sc
#     for nr, nc in target:
#
#         ret = bfs(board, r, c, nr, nc)
#
#         if ret == -1:
#             return -1
#
#         answer += ret
#         r, c = nr, nc
#
#     return answer
#
#
# board = list(list(map(int, input().split())) for _ in range(5))
# sr, sc = map(int, input().split())
# print(solution(board, sr, sc))

# 6-1-3
# def in_range(nr, nc):
#     return 0 <= nr <= 4 and 0 <= nc <= 4
#
#
# def bfs(board, sr, sc, tr, tc):
#     dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#     visited = [[0] * 5 for _ in range(5)]
#     dist = [[0] * 5 for _ in range(5)]
#
#     q = deque()
#     q.append([sr, sc])
#
#     visited[sr][sc] = 1
#     dist[sr][sc] = 0
#
#     while len(q) != 0:
#         r, c = q.popleft()
#
#         if r == tr and c == tc:
#             return dist[r][c]
#
#         for dr, dc in dd:
#             nr = r + dr
#             nc = c + dc
#             if in_range(nr, nc) and board[nr][nc] != -1 and visited[nr][nc] == 0:
#                 visited[nr][nc] = 1
#                 q.append([nr, nc])
#                 dist[nr][nc] = dist[r][c] + 1
#
#         for dr, dc in dd:
#             nr, nc = r, c
#             while True:
#                 if not in_range(nr + dr, nc + dc):
#                     break
#
#                 if board[nr + dr][nc + dc] == -1:
#                     break
#
#                 nr += dr
#                 nc += dc
#                 if board[nr][nc] == 7:
#                     break
#
#             if visited[nr][nc] == 0:
#                 q.append([nr, nc])
#                 visited[nr][nc] = 1
#                 dist[nr][nc] = dist[r][c] + 1
#
#     return -1
#
#
# def solution(board, sr, sc):
#     tr, tc = 0, 0
#     for r in range(5):
#         for c in range(5):
#             if board[r][c] == 1:
#                 tr, tc = r, c
#
#     return bfs(board, sr, sc, tr, tc)
#
#
# board = list(list(map(int, input().split())) for _ in range(5))
# sr, sc = map(int, input().split())
# print(solution(board, sr, sc))

# 6-1-4
def in_range(nr, nc):
    return 0 <= nr <= 4 and 0 <= nc <= 4


def bfs(board, sr, sc, tr, tc):
    dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[0] * 5 for _ in range(5)]
    dist = [[0] * 5 for _ in range(5)]

    q = deque()
    q.append([sr, sc])

    visited[sr][sc] = 1
    dist[sr][sc] = 0

    while len(q) != 0:
        r, c = q.popleft()

        if r == tr and c == tc:
            return dist[r][c]

        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            if in_range(nr, nc) and board[nr][nc] != -1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dist[nr][nc] = dist[r][c] + 1
                q.append([nr, nc])

        for dr, dc in dd:
            nr, nc = r, c
            while True:
                if not in_range(nr + dr, nc + dc):
                    break

                if board[nr + dr][nc + dc] == -1:
                    break

                nr += dr
                nc += dc
                if board[nr][nc] == 7:
                    break

            if visited[nr][nc] == 0:
                q.append([nr, nc])
                visited[nr][nc] = 1
                dist[nr][nc] = dist[r][c] + 1

    return -1


def solution(board, sr, sc):
    target = list([] for _ in range(6))
    for r in range(5):
        for c in range(5):
            if 0 < board[r][c] < 7:
                target[board[r][c] - 1] = r, c

    answer = 0
    r, c = sr, sc
    for nr, nc in target:

        ret = bfs(board, r, c, nr, nc)

        if ret == -1:
            return -1

        r = nr
        c = nc

        answer += ret

    return answer


board = list(list(map(int, input().split())) for _ in range(5))
sr, sc = map(int, input().split())
print(solution(board, sr, sc))
