# 154
# with open('text.txt' , 'r') as file:
#     res = file.read()
# res = res.replace('\n' , '')
# res = res.replace(' ' , '')

# unique = set(res)

# for i in unique:
#     print(f'{i}-ը Կրկնվում է {res.count(i)}')

# 155
# with open('text.txt' , 'r') as file:
#     res = file.read()
# unique = set(res.replace('\n' , ' ').split())

# for i in unique:
#     print(f'{i}-ը Կրկնվում է {res.count(i)}')




#____freestyle By Vardges_______
# import random
# __import__('pprint').pprint(({random.randint(0 , 100):random.randint(0 , 100)  for k , v in zip(range(20) ,range(20))}))
# __________________________________________


#_________________________________Try ---- Except______________________________________________

'''
SyntaxError
TypeError
AsertionError
ValueError
KeyError
NameError
IndexError
IndentationError
ModuleNotFoundError
'''
# try - else

# try:
#     num = int(input('Enter a number: '))
# except ValueError:
#     print('Losseer')
# else:
#     print(num)

# finally:
#     print('End')


# s = 0
# while True:
#     try:
#         n = int(input('Enter a number: '))
#     except ValueError:
#         print(f'Sum is {s}')
#         break
#     else:
#         s += n


# 155 try
# file = input('Enter file name(without format): ')

# try:
#     with open(file  + '.txt', 'r') as file:
#         res = file.read()
# except FileNotFoundError:
#     print('Error 302')
# else:
#     unique = set(res.replace('\n' , ' ').split())

#     for i in unique:
#         print(f'{i}-ը Կրկնվում է {res.count(i)}')

# vat orinak

# try:
#     num = int(input('Enter a number: '))
# except ValueError:
#     raise ValueError('Edqan el aseci qich xmi')


# 67
# import math

# perimeter = 0
# first_X = x0 = int(input('Enter X: '))
# first_Y = y0 = int(input('Enter Y: '))

# while True:
#     try:
#         x = int(input('Enter X: '))
#     except ValueError:
#         perimeter += math.sqrt((first_X - x0)**2 + (first_Y - y0)**2)
#         print(perimeter)
#         break
#     else:
#         y = int(input('Enter Y: '))
#         perimeter += math.sqrt((x - x0)**2 + (y - y0)**2)
#         x0 = x
#         y0 = y



# numbers = []
# while True:
#     try:
#         num = int(input("Write a number: "))
#     except ValueError:
#         mijin = sum(numbers)/len(numbers)
#         print(mijin)
#         break
#     else:
#         numbers.append(num)



















