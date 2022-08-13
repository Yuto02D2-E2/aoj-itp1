""" 2_A """
# a, b = map(int, input().split())
# if a < b:
#     print("a < b")
# elif a > b:
#     print("a > b")
# else:
#     print("a == b")


""" 2_B """
# a, b, c = map(int, input().split())
# print(["No", "Yes"][a < b < c])


""" 2_C """
# print(*sorted(map(int, input().split())))


""" 2_D """
w, h, x, y, r = map(int, input().split())
if r <= x and r <= y and x <= w - r and y <= h - r:
    print("Yes")
else:
    print("No")
