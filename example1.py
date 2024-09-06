a = 'abcdefghijklmnopqrstuvwxyz'
b = int(input())
c = input()
d = ''

for i in range(len(c)):
    for j in range(len(a)):
        if c[i] == a[j]:
            x = ord(a[j]) - b
            if x <= ord('a'):
                x +=26
            d += chr(x)
            break
print(d)



# In the hole in the ground there lived a hobbit

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

