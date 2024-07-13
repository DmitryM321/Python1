n = int(input())
total = 1
for i in range(1, n + 1):
    for j in range(1, i + i):
            print(total, end='')
            if j < i:
                total += 1
            else:
                total -= 1
    total = 1

    print()

# 1
# 121
# 12321
# 1234321
# 123454321

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

