a, b = int(input()), int(input())
sum = 0
max = 0
for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
            if total > sum or (total == sum and i > max):
                sum = total
                max = i

print(max, sum)

# Sample Input 1:
# 1
# 10
# Sample Output 1:
# 10 18
# Sample Input

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

