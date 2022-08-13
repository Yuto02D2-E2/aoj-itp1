""" 9_A """
# word = input()
# document = list()
# while True:
#     buffer = input()
#     if buffer == "END_OF_TEXT":
#         break
#     for b in buffer.split():
#         document.append(b.lower())
# print(document.count(word))


""" 9_B """
# while True:
#     text = input()
#     if text == "-":
#         break
#     m = int(input())
#     H = [int(input()) for _ in range(m)]
#     for h in H:
#         text = text[h:] + text[:h]
#     print(text)


""" 9_C """
# taro_score = hanako_score = 0
# n = int(input())
# for _ in range(n):
#     taro, hanako = input().split()
#     if taro < hanako:
#         hanako_score += 3
#     elif hanako < taro:
#         taro_score += 3
#     else:
#         taro_score += 1
#         hanako_score += 1
# print(taro_score, hanako_score)


""" 9_D """
text = list(input())
q = int(input())
for _ in range(q):
    buffer = input().split()
    order = buffer[0]
    a = int(buffer[1])
    b = int(buffer[2]) + 1
    if order == "print":
        print("".join(text[a:b]))
    elif order == "reverse":
        text[a:b] = reversed(text[a:b])
    else:
        text[a:b] = buffer[-1]
