# 4 from slide 
# with open('text.txt' , 'r') as file:
#     res = file.read()

# res = res.replace('\n' , ' ')
# res = res.split()
# res = sorted(res , key = len)
# max_len = len(res[-1])

# for i in res:
#     if len(i) == max_len:
#         print(i)


# 5
# with open('text.txt' , 'r') as file:
#     res = file.read()

# number_list = []
# for i in res:
#     if i.isdigit():
#         number_list.append(i)
# print(number_list)

# 6
# with open('text.txt' , 'r') as file:
#     res = file.readlines()
# password_list = []

# for i in res:
#     if 'login' in i:
#         password_list.append(i)
#     elif 'password' in i:
#         password_list.append(i)
# print(password_list)
# print(''.join(password_list))


# 149
# def head(file_name: str , lines : int) -> str:
#     with open(file_name , 'r') as file:
#         res = file.readlines()
#     return ''.join(res[:lines])

# print(head('text.txt' , 4))

# 150
# def tail(file_name : str, lines : int) -> str:
#     with open(file_name , 'r') as file:
#         result = file.readlines()
#     return ''.join(result[-lines: ])

# print(tail('text.txt' , 4))


# 152
# def to_number(file):
#     with open(file , 'r') as file:
#         result = file.readlines()
#     ans = []
#     for i in range(len(result)):
#         ans.append(f'{i + 1} {result[i]}')
#     return ans

# new = to_number('text.txt')

# with open('text.txt' , 'w') as file:
#     file.write(''.join(new))



#________________________________________JSON__________________________________________
# import json

# info = {
#     'name':'Vardges',
#     'surname':'Hambaryan',
#     'Datavatsutyun':False
# }

# with open('info.json' , 'w') as file:
    # json.dump(info , file , indent=4)

# with open('info.json' , 'r' , encoding='UTF-8') as file:
    # res = json.load(file)

# print(res)


# import os

# os.mkdir('Allah')
# print(os.getcwd())


# with open('text.txt','r') as file:
#     res = file.read().split()
#     count = {'chr':0}
#     alp = 'qwertyuiopasdfghjklzxcvbnm'
#     for i in res:
#         if i == alp:
#             count['chr'] =+ 1
#     print(count)

class Singlton:
    __instance = None

    def __new__(cls , *args , **kwargs):
        if cls.__instance is not None:
            cls.args = args
            return cls.__instance
        else:
            cls.args = args
            cls.__instance = super(Singlton , cls).__new__(cls)
            return cls.__instance

    def info(cls):
        return cls.args

# a = Singlton(10)
b = Singlton()
print(b.info())




