s = input()
if 5 <= len(s) <= 15 and s[0] == '@' and (s[1:].isdigit() or (s[1:].isalnum() and s[1:].islower())):

    print('Correct')
else:
    print('Incorrect')

# s = input()
#
# if  s[1:].isalnum() or s[1:].isalpha()  :
#
#     print('Correct')
# else:
#     print('Incorrect')



# print(s[:s.find('h') - 1], s[s.rfind('h'):])

# In the hole in the ground there lived a hobbit


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# a, b, c, d = float(input()), float(input()), float(input()), float(input())
# m, n = int(input()), int(input())
# num1, num2, num3 = int(input()), int(input()), int(input())

