""" 4_A """
# a, b = map(int, input().split())
# print(f"{a // b} {a % b} {a / b:.8f}")


""" 4_B """
# import math
# r = float(input())
# print(math.pi * r * r, 2 * math.pi * r)


""" 4_C """
# while True:
#     a, op, b = input().split()
#     if op == "?":
#         break
#     a, b = int(a), int(b)
#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     else:
#         print(a // b)


""" 4_D """
n = int(input())
A = list(map(int, input().split()))
print(min(A), max(A), sum(A))
