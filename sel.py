# ЦИКЛ FOR

# for i in range(1, 11):
#     print(i)

# for i in range(1, 16, 2):
#     print(i)

# n = int(input())
# for i in range(1, n + 1, 2):
#     print(i)

# for i in range(1, n + 1):
#     print(i, "->", i**2)

# aboba = 0
# for i in range(1, n + 1, 2):
#     aboba += i
# print(aboba)

# aboba = 0
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         aboba += i
# print(aboba)

# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}")

# aboba = 1
# for i in range(1, n + 1):
#     aboba *= i
# print(aboba)

# aboba = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         aboba += 1
# print(aboba)

# for i in range(1, n + 1):
#     if i % 10 == 5:
#         print(i)

# aboba = n > 1
# for i in range(2, int(n**0.5) + 1):
#     if n % i == 0:
#         aboba = False
#         break
# print(aboba)

# a, b = map(int, input().split())
# aboba = 1
# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         aboba = i
#         break
# print(aboba)

# for i in range(2, n + 1):
#     aboba = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             aboba = False
#             break
#     if aboba:
#         print(i)

# aboba = 0
# for d in str(n):
#     aboba += int(d)
# print(aboba)

# aboba = 0
# for d in str(n):
#     if int(d) > aboba:
#         aboba = int(d)
# print(aboba)


#ЦИКЛЪ WHILE


# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# i = 1
# while i < n:
#     print(i)
#     i += 3


# aboba = 0
# i = 1
# while i <= n:
#     aboba += i
#     i += 1
# print(aboba)


# aboba = 1
# i = 1
# while i <= n:
#     aboba *= i
#     i += 1
# print(aboba)


# aboba = 0
# while True:
#     x = int(input())
#     if x == 0:
#         break
#     aboba += x
# print(aboba)


# aboba = n
# aboba1 = 0
# while aboba > 0:
#     aboba1 += aboba % 10
#     aboba //= 10
# print(aboba1)


# aboba = n
# aboba12 = 0
# while aboba > 0:
#     aboba12 += 1
#     aboba //= 10
# print(aboba12)


# aboba = n
# aboba123 = 0
# while aboba > 0:
#     aboba123 = aboba123 * 10 + aboba % 10
#     aboba //= 10
# print(aboba123)
 

# aboba = n
# aboba213 = 0
# while aboba > 0:
#     if aboba % 10 > aboba213:
#         aboba213 = aboba % 10
#     aboba //= 10
# print(aboba213)


# aboba = n
# 1aboba = 0
# while aboba > 0:
#     1aboba = 1aboba * 10 + aboba % 10
#     aboba //= 10
# print(n == 1aboba)


# aboba = 2
# aboba33 = n > 1
# while aboba * aboba <= n:
#     if n % aboba == 0:
#         aboba33 = False
#         break
#     aboba += 1
# print(aboba33)


# v1, v2 = a, b
# while v1 > 0 and v2 > 0:
#     if v1 > v2:
#         v1 %= v2
#     else:
#         v2 %= v1
# print(v1 + v2)


# aboba = n
# while aboba >= 10:
#     aboba //= 10
# print(aboba)


# f1, f2 = 0, 1
# while f1 <= n:
#     print(f1)
#     f1, f2 = f2, f1 + f2


# aboba = -float('inf')
# while True:
#     x = int(input())
#     if x < 0:
#         break
#     if x > aboba:
#         aboba = x  
# print(aboba)