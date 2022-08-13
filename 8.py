""" 8_A """
# S = input()
# ans = ""
# for s in S:
#     if s.isalpha():
#         if s.islower():
#             ans += s.upper()
#         else:
#             ans += s.lower()
#     else:
#         ans += s
# print(ans)


""" 8_B """
# while True:
#     x = input()
#     if x == "0":
#         break
#     print(sum([int(i) for i in x]))


""" 8_C """
# import collections
# alpha_cnt = collections.defaultdict(int)
# while True:
#     try:
#         buffer = input()
#     except EOFError:
#         break
#     for b in buffer:
#         if b.isalpha():
#             alpha_cnt[b.lower()] += 1
# for i in range(26):
#     alpha = chr(97 + i)
#     print(f"{alpha} : {alpha_cnt[alpha]}")


""" 8_D """
S = input()
P = input()
print(["No", "Yes"][P in (S + S)])
