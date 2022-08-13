""" 7_A """
# while True:
#     m, f, r = map(int, input().split())
#     if m == f == r == -1:
#         break
#     if m == -1 or f == -1 or m + f < 30:
#         print("F")
#     elif 80 <= m + f:
#         print("A")
#     elif 65 <= m + f:
#         print("B")
#     elif 50 <= m + f:
#         print("C")
#     else:
#         if 50 <= r:
#             print("C")
#         else:
#             print("D")


""" 7_B """
# import itertools
# while True:
#     n, x = map(int, input().split())
#     if n == x == 0:
#         break
#     comb = list(itertools.combinations(range(1, n + 1), 3))
#     ans = 0
#     for a, b, c in comb:
#         if a + b + c == x:
#             ans += 1
#     print(ans)


""" 7_C """
# r, c = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(r)]
# for y in range(r):
#     A[y] = A[y] + [sum(A[y])]
#     print(*A[y])
# for x in range(c):
#     cur = 0
#     for y in range(r):
#         cur += A[y][x]
#     print(cur, end=" ")
# cur = 0
# for y in range(r):
#     cur += A[y][c]
# print(cur)


""" 7_D """
n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
C = [[0 for _ in range(l)] for _ in range(n)]
for y in range(n):
    for x in range(l):
        for k in range(m):
            C[y][x] += A[y][k] * B[k][x]
for c in C:
    print(*c)
