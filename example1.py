n = int(input())
sum = ''
for i in range(1, n + 1):
    total = 0
    sum = ''
    for j in range(1, i + 1):
        if i % j == 0:
            sum += '+'
    print(i, sum, sep='')


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

