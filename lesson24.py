# 97
# def precedence(operation):
#     if operation == '+' or operation == '-':
#         return 1
#     elif operation == '*' or operation == '/':
#         return 2
#     elif operation == '^':
#         return 3
#     else:
#         return -1

# oper = input('Enter operation: ')
# print(precedence(oper))

# 98
# def isPrime(num):
#     for i in range(2 , num):
#         if num % i == 0:
#             return False
#     return True

# 99
# def NextPrimeNumber(num):
#     while True:
#         if isPrime(num + 1):
#             return num + 1
#         else:
#             num += 1

# print(NextPrimeNumber(6657))


# 100
# def PasswordGenerator():
#     import random
#     password = ''
#     for _ in range(random.randint(7 , 10)):
#         password += chr(random.randint(33 , 126))
#     return password
# password =  PasswordGenerator()

# 102
# def isValid(password):
#     number = False
#     lower = False
#     upper = False
#     symbol = False

#     sym = '~!@#$%^&*()_+=[]/.'
#     low = 'qwertyuiopasdfghjklzxcvbnm'
#     up = low.upper()
#     for i in password:
#         if i in sym:
#             symbol = True
#         elif i in low:
#             lower = True
#         elif i in up:
#             upper = True
#         elif i.isdigit():
#             number = True
#     return number and lower and upper and symbol
# print(password)
# print(isValid(password))


# def hex2int(hexNumber):
#     hexn = {
#         '1':1,  '2':2,  '3':3,
#         '4':4,  '5':5,  '6':6,
#         '7':7,  '8':8,  '9':9,
#         'A':10, 'B':11, 'C':12,
#         'D':13, 'E':14, 'F':15,
#     }
#     hexNumber = hexNumber[::-1] # 8F
#     num = 0
#     for i in range(len(hexNumber)):
#         num += hexn[hexNumber[i]] * pow(16 , i)
#     return num
# print(hex2int('F8'))

# def int2hex(intnum):
    
# num = 'F8'
# n = '1011011'
# print(int(n , base=2))

# print(hex(248))



# 107
# def mygcd(a , b):
#     from math import gcd
#     return f'{a//gcd(a , b)} / {b//gcd(a , b)}'
# print(mygcd(10 , 25))


# a = 10
# b = 25
# m = 1
# for i in range(2 , min(a , b) + 1):
#     if a % i == 0 and b % i == 0:
#         if i > m:
#             m = i
# print(m)

