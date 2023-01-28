# 176
# def Encode(word):
#     word = word.upper()

#     nato = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta',
#             'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H': 'Hotel' , 'I':'India', 'J':'Juliet',
#             'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar',
#             'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango',
#             'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'
#             }

#     if len(word) == 1:
#         return nato[word]
#     else:
#         return nato[word[0]] + ' ' + Encode(word[1:])

# word = input('Enter any word: ')
# print(Encode(word))

# 179 
# def Sqrt(n , guess = 1.0):
#     if abs(n - guess**2) < 10**(-15):
#         return guess
#     else:
#         guess = (guess + n / guess) / 2
#         return Sqrt(n , guess)
# print(Sqrt(5))


# 180
# def Change(s , t):
#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[-1] != t[-1]:
#             cost = 1
#         d1 = Change(s[:-1] , t) + 1
#         d2 = Change(s , t[:-1]) + 1
#         d3 = Change(s[:-1] , t[:-1])  + cost
#     return min(d1  , d2 , d3)
# print(Change('kitten' , 'sitting'))


# power of number
# def power(n , p):
#     if p == 1:
#         return n
#     else:
#         return n * power(n , p - 1)
# print(power(2 , 10))

# 184 
list1 = [1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]]
# ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def unpack(data):
    if len(data) == 0:
        return []
    elif type(data[0]) is list:
        l1 = unpack(data[0])
        l2 = unpack(data[1:])
        return l1 + l2
    elif type(data[0]) is not list:
        l1 = unpack([data[0]])
        l2 = unpack(data[1:])
        return l1 + l2

lst = [3 , [1 , 2] ]
l1 = [lst[0]]
l2 = lst[1]
print(l1 + l2)


    
    