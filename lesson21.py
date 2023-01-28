# 145
# points = { 
#     1  :'AEILNORSTU',
#     2  :'DG',
#     3  :'BCMP',
#     4  :'FHVWY',
#     5  :'K',
#     8  :'JX',
#     10 :'QZ',
# }

# word = 'Python'.upper()
# chars = list(word)

# points = {v : k for k , v in points.items()}
# s = 0
# for i in chars:
#     for j in points:
#         if i in j:
#             s+= points[j]
# print(s)

# 139
# morze = {
#     "A": ".-", 
#     "B": "-...", 
#     "C": "-.-.", 
#     "D": "-..",
#     "E": "." ,
#     "F": "..-.",
#     "G": "--.",
#     "H": "….",
#     "I": "..  ", 
#     "J": ".---",  
#     "K": "-.-",
#     "L": ".-..",  
#     "M": "--", 
#     "N": "-.",  
#     "O": "---",  
#     "P": ".--.",  
#     "Q": "--.-",  
#     "R": ".-.",
#     "S": "...",
#     "T": "-",
#     "U": "..-",
#     "V": "...-",
#     "W": ".--",
#     "X": "-..-",
#     "Y": "-.--",
#     "Z": "--..",
#     "0": "-----",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "….-",
#     "5": "…..",
#     "6": "–….",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
#     }
# word = 'Python'.upper()

# str1 = ''
# for i in word:
#     str1 += morze[i]
# print(str1)

# 143
# word1 = 'live'
# word_dict = {}

# for i in word1:
#     word_dict[i] = word1.count(i)
# print(word_dict)

# word2 = 'evil'

# for i in word2:
#     if i in word_dict:
#         if word2.count(i) == word_dict[i]:
#             pass
#         else:
#             print('No anagram')
#             break
#     else:
#         print('No anagram')
#         break
# else:
#     print('Aanagram')

# word1 = 'live'
# word2 = 'evil'
# word1 = sorted(word1)
# word2 = sorted(word2)

# if word1 == word2:
#     print('Anagram')
# else:
#     print('Not anagram')

# 144
# text1 = input('Enter first text: ').lower()
# text2 = input('Enter second text: ').lower()

# text1 = text1.replace(' ','')
# text1 = text1.replace(',','')
# text1 = text1.replace('.','')
# text1 = text1.replace('!','')
# text2 = text2.replace(' ','')
# text2 = text2.replace(',','')
# text2 = text2.replace('.','')
# text2 = text2.replace('!','')

# sortedtx1 = sorted(text1)
# sortedtx2 = sorted(text2)

# if sortedtx1 == sortedtx2:
#     print('The texts are anagrams:')
# else:
#     print('The texts are not anagrams: ')

# 146
# from random import randint
# LOTO = {
#     'B':[randint(1 , 15)  for _ in range(5)],
#     'I':[randint(16 , 30) for _ in range(5)],
#     'N':[randint(31 , 45) for _ in range(5)],
#     'G':[randint(46 , 60) for _ in range(5)],
#     'O':[randint(61 , 75) for _ in range(5)],
# }

# __import__('pprint').pprint(LOTO)

# _____________________SET__________________________

# set1 = {'a' , 'b' , 'a'}
# print(type(set1)) 
# st = set()
# print(st)


# A = {1 , 2 , 3 , 4}
# B = {3 , 4 , 5 , 6}

# print(A.union(B))
# print(A | B)
#________________
# print(A.intersection(B))
# print(A & B)
# __________________
# print(A.difference(B))
# print(B.difference(A))
# print(A - B)
# print(B - A)
# ____________________
# print(A.symmetric_difference(B))
# print(A ^ B)


#_________________________________________________

# set1 = {1 , 2 , 3 , 4}
# set2 = {4 , 5 , 6 , 7}
# set3 = {2 , 3}
# set1.add(5)
# set1.update(set2)
# set1.remove(5)
# set1.discard(5)
# set1.pop() # jnjum a skzbic 1 hat
# del set1 # jnjum e sax sety
# set1.clear() 

# set1 = {1 , 2 , 3 , 4}
# set2 = {4 , 5 , 6 , 7}
# set3 = {2 , 3}

# print(set1.isdisjoint(set2))
# print(set3.issubset(set1))
# print(set1.issuperset(set3))


# mylist = [1 , 2 ,4 , 5 ,2 , 2 ,2 ,1, 5, 1 , 4 , 5 ]
# print(list(set(mylist)))























