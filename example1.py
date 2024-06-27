for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                for e in range(d, 151):

                    if a ** 5 + b **5 + c ** 5 + d ** 5 == e ** 5:
                        # print(a, b, c, d, e)
                        print(a + b + c + d + e)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

