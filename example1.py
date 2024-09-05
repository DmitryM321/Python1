a = input()
b = ''
count1 = 0
count2 = 0
x = 'eyopaxcETOPAHXCBM'
y = 'еуорахсЕТОРАНХСВМ'

for i in range(len(a)):
    count1 += ord(a[i])

for k in range(len(a)):
    for i in range(len(x)):
        if a[k] == x[i]:
            b += y[i]
            break
    else:
        b += a[k]

for k in range(len(b)):
    count2 += ord(b[k])
print("Старая стоимость: ", count1*3, '🐝', sep='')
print('Новая стоимость: ', count2*3, '🐝', sep='')


# In the hole in the ground there lived a hobbit

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

