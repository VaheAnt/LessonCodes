#_________________________________RECURSION_______________________________
# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x + 1)
#     print(x)
# rec(1)

# # factorial
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))

#  5! = 5 * 4! = 5 * (4 * 3!) = 5 * 4 * (3 * 2!) = 5 * 4 * 3 * (2 * 1!) = 120


# fibonacci
# 0 , 1 , 1, 2, 3 , 5 ,8 , 13 , 21 , 34 , 55 , 89 , 144

# def fibonacci(n):
#     if n == 1 or n == 2:
#         return n - 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(55))

# a = 0
# b = 1
# for i in range(10000):
#     a , b = b , a + b
#     print(b)

# 
# text = 'Hello'
# text = 'H*e*l*l*o'

# def myfunc(text):
#     if len(text) == 1:
#         return text
#     else:
#         return text[0] + '*' + myfunc(text[1:])
# print(myfunc(text))


# text = 'Hello'
# text = 'H(e(l)l)o'

# text = 'Python'
# text = 'P(y(th)o)n'



























