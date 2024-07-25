a, b = int(input()), int(input())
total = 0
for i in range (a, b + 1):
        total = 0

        for j in range (1, i + 1):
                if i % (j) == 0:
                        total += 1
        if total == 2 and i > 1:
                print(i)






# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

