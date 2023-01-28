# text 

# text = 'Python'
# '''
# P(y(t()h)o)n
# '''
# def pak(text):
#     if len(text) == 1 or len(text) == 0:
#         return text
#     else:
#         return text[0] + '(' +  pak(text[1:-1])  + ')' + text[-1]
# print(pak(text))



# 173
# def suma(s = 0):
#     num = input('Enter a number: ')
#     if num == '':
#         return s
#     else:
#         s += int(num)
#         return suma(s)
# print(suma())

# 174
# def gcd(a , b):
#     if b == 0:
#         return a
#     else:
#         c = a % b
#         return gcd(b , c)
# print(gcd(144 , 15))

# 178
def polindrom(word):
    if len(word) == 0 or len(word) == 1:
        return True
    else:
        if word[0] == word[-1]:
            return polindrom(word[1:-1])
        else:
            return False
print(polindrom('level'))




























































