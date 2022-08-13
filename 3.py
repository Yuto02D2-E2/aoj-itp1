""" 3_A """
# print(*["Hello World\n" for _ in range(1000)])


""" 3_B """
# for i in range(1, 100000):
#     x = int(input())
#     if x == 0:
#         break
#     print(f"Case {i}: {x}")


""" 3_C """
# while True:
#     x, y = map(int, input().split())
#     if x == y == 0:
#         break
#     print(min(x, y), max(x, y))


""" 3_D """
a, b, c = map(int, input().split())
ans = 0
for x in range(a, b + 1):
    if c % x == 0:
        ans += 1
print(ans)
