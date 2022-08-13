""" 6_A """
# n = int(input())
# print(*list(reversed(list(map(int, input().split())))))


""" 6_B """
# n = int(input())
# card = {
#     "S": [False for _ in range(13)],
#     "H": [False for _ in range(13)],
#     "C": [False for _ in range(13)],
#     "D": [False for _ in range(13)],
# }
# for _ in range(n):
#     char, num = input().split()
#     card[char][int(num) - 1] = True
# for char in ["S", "H", "C", "D"]:
#     for num in range(13):
#         if not card[char][num]:
#             print(char, num + 1)


""" 6_C """
# cnt = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
# n = int(input())
# for _ in range(n):
#     b, f, r, v = map(int, input().split())
#     cnt[b - 1][f - 1][r - 1] += v

# for b in range(4):
#     for f in range(3):
#         print(" ", end="")
#         print(*cnt[b][f])
#     if b < 3:
#         print("#" * 20)


""" 6_D """
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [int(input()) for _ in range(m)]
C = [0 for _ in range(n)]
for i in range(n):
    for j in range(m):
        C[i] += A[i][j] * B[j]
print(*C, sep="\n")
