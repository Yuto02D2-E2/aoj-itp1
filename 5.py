""" 5_A """
# while True:
#     h, w = map(int, input().split())
#     if h == w == 0:
#         break
#     for _ in range(h):
#         print("#" * w)
#     print()


""" 5_B """
# while True:
#     h, w = map(int, input().split())
#     if h == w == 0:
#         break
#     print("#" * w)
#     for _ in range(h - 2):
#         print("#" + "." * (w - 2) + "#")
#     print("#" * w)
#     print()


""" 5_C """
# while True:
#     h, w = map(int, input().split())
#     if h == w == 0:
#         break
#     for r in range(h):
#         for c in range(w):
#             if r % 2 == c % 2:
#                 print("#", end="")
#             else:
#                 print(".", end="")
#         print()
#     print()


""" 5_D """
# 一番難しかった
# GOTOとか滅びてしまえ


def call(n: int) -> None:
    for i in range(1, n + 1):
        x = i
        if x % 3 == 0:
            print(f" {i}", end="")
            continue
        while True:
            if x:
                if x % 10 == 3:
                    print(f" {i}", end="")
                    break
                x //= 10
            else:
                break
    print()


if __name__ == '__main__':
    n = int(input())
    call(n)
