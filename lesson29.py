# name = 'index.docs'

# f = open(name , 'w')

# file = open(name , 'a') #_______
# file.write('Hello Python Team 2\n')

# file.close() #___________________


# file = open(name , 'r')

# res = file.read()
# print(res)


# f = open('text.txt' , 'a')

# f.write('Hello Python Team 3')

# f.close()


# f = open('text.txt' , 'r')
# res = f.read()

# res = f.readline()
# res = f.readlines()

# f.close()
# res = ['Hello Python Team 1234\n', 'Hello Python Team 1\n', 'Hello Python Team 1\n', 'Hello Python Team 1\n', 'Hello Python Team 2\n']

# print(''.join(res))


# mylist = [1 ,2 ,3 , 4]


# with open('text.txt' , 'w') as file:
#     # result = file.readline()
#     file.write('Hello')


# for i in range(1 , 6):
#     with open(f'text{i}.txt' , 'w') as file:
#         file.write('Hello')

# with open('text.txt' , 'w') as file:
#     file.write('Hello 1')

with open('text.txt' , 'a') as file:
    file.write('\nNew Line')

with open('text.txt' , 'r') as file:
    res = file.read()
print(res)












