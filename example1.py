n = int(input())
if n < 9:
    print(n)
else:
    while n > 9:
        sum = 0
        while (n) > 0:
            sum += n % 10
            n = n // 10
        n = sum
    print(sum)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

