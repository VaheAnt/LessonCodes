# pi = 3
# for i in range(1 , 10000):
#     pi += (-1)**(i + 1) *  4 / (2*i * (2*i + 1) * (2*i + 2))
# print(round(pi , 15))

# def isPrime(number : int) -> bool:
#     for i in range(2 , number):
#         if number % i == 0: 
#             return False
#     return True    
    

# def nextPrime(num: int):
#     while True:
#         if isPrime(num):
#             return num
#         else:
#             num +=  1
# print(nextPrime(17))


# def password():
#     import random

#     rand_lenght = random.randint(7,10)
#     password = ''
#     for _ in range(rand_lenght):
#         rand_num = random.randint(33,126)
#         password += chr(rand_num)
#     return password

# print(password())


# mydict = {'A' : 55 , 'B': 45 , 'C': 27 , 'D': 36 , 'F': 10}
# print(dict(sorted(mydict.items(), key = lambda x : x[1])))


# s = "25525511135"

# def restoreIpAddresses(s: str , points: int = 4) -> list[int]:
#     if len(s) == points:
#         return ['.'.join(points)]
#     else:
#         if int(s[0]) > 2 & int(s[1])




