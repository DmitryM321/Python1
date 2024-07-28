n = int(input())
count3 = 0
count_last_dig = 0
even = 0
sum_more5 = 0
deterioration_more7 = 1
count_0_and_5 = 0
a1 = n % 10
while n > 0:
    a = n % 10
    n = n // 10
    if a == 3:
        count3 += 1
    if a1 == a:
        count_last_dig += 1
    if a % 2 == 0:
        even += 1
    if a > 5:
        sum_more5 += a
    if a == 0 or a == 5:
        count_0_and_5 += 1
    if a > 7:
        deterioration_more7 *= a
    if deterioration_more7 == 7:
        deterioration_more7 = 7
        if a != 7:
            deterioration_more7 = 1

print(count3)
print(count_last_dig)
print(even)
print(sum_more5)
print(deterioration_more7)
print(count_0_and_5)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

