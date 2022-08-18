""" 1_A """
# print("Hello World")


""" 1_B """
# print(int(input())**3)


""" 1_C """
# a, b = map(int, input().split())
# print(a * b, 2 * a + 2 * b)


""" 1_D """
S = int(input())
h = S // 60 // 60 % 60
m = S // 60 % 60
s = S % 60
print(f"{h}:{m}:{s}")
