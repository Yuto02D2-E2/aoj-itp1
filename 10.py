""" 10_A """
# import math
# x1,y1,x2,y2 = map(float, input().split())
# print(
#     math.sqrt((x1-x2)**2 + (y1-y2)**2)
# )


""" 10_B """
# import math
# a, b, deg = map(int, input().split())
# # 余弦定理
# c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(deg)))
# # ヘロンの公式
# L = a + b + c
# s = L / 2
# S = math.sqrt(s * (s - a) * (s - b) * (s - c))
# # 三角形の面積=1/2*(底辺)*(高さ)
# h = 2 * S / a
# print(S)
# print(L)
# print(h)


""" 10_C """
# import statistics
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     S = list(map(int, input().split()))
#     print(statistics.pstdev(S))


""" 10_D """


def D(p, is_inf=False) -> float:
    if not is_inf:
        return pow(
            sum([pow(abs(X[i] - Y[i]), p) for i in range(n)]),
            1 / p
        )
    else:
        return max([abs(X[i] - Y[i]) for i in range(n)])


n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
print(D(1))
print(D(2))
print(D(3))
print(D(float("inf"), True))
