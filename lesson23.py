# # 87
# # def purchase(count_of_products):
#     # return 10.95 + 2.95 * (count_of_products - 1)
# # print(purchase(10))

# # 88
# # 1 2 3 4 5 6
# # def median(*args):
# #     args = sorted(args)
# #     if len(args) % 2 == 1:
# #         return args[len(args) // 2]
# #     else:
# #         return (args[len(args) // 2] + args[len(args) // 2 - 1]) / 2
# # print(median(1, 2, 3, 4))


# # def median(a , b , c):
# #     return a + b + c - min(a , b , c) - max(a , b , c)
# # print(median(1, 4, 3))

# # 89
# # def tiv(a):
# #     if a == 1:
# #         return 'first'
# #     elif a == 2:
# #         return 'first'
# #     elif a == 3:
# #         return 'first'




# # 90
# # def ordinalDate(year , month , day):
# #     import datetime
# #     d1 = datetime.datetime(year, month , day)
# #     d0 = datetime.datetime(year , 1 , 1)
# #     return (d1 - d0).days

# # year = int(input('Enter Year: '))
# # month = int(input('Enter Month: '))
# # day = int(input('Enter day: '))

# # print(f'{ordinalDate(year , month , day)} days')

# # def roadToFuture(year , month , day):
# #     import datetime
# #     now = datetime.datetime.now()
# #     d = datetime.datetime(year , month , day)
# #     return (d - now).days
# # print(roadToFuture(2099 , 3 , 20))

# # 93
# # def tabs(s , w):
# #     if len(s) >= w:
# #         return w * '  ' + s
# #     else:
# #         return ((w - len(s)) // 2) * '   ' + s
# # print(tabs('Hello' , 35))


# #  94
# # def text_transformer(text):
# #     text = text.split('? ')
# #     for i in range(len(text)):
# #         text[i] = text[i].capitalize()
# #     print(text)
# #     text = '? '.join(text)
# #     text = text.replace(' i ', ' I ')
# #     text = text.replace(" i'", " I'")
# #     return text

# # text = "what time do i have to be there? what's the address? this time i'll try to be on time!"
# # print(text_transformer(text))


# # 96
# def isintager(operation):
#     operation = eval(operation)
#     if type(operation) == int:
#         return True
#     return False

# text = '-5.6'
# print(isintager(text))

