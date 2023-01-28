
# class Vardges():

#     def info(self):
#         return 'Hello, I am class Vardges'

    
# x = Vardges()
# print(x.info())
# print(type(x))



# class Informations():

#     def __init__(self , **kwargs):
#         self.kwargs = kwargs

#     def info(self):
#         return self.kwargs

# inf = Informations(name = 'Vardges' , surname = 'Hambaryan' , age = 19 )

# print(inf.info())
# print(type(inf))

# class Mathematics():

#     def __init__(self , a , b) -> None:
#         self.a = a
#         self.b = b

#     def suma(self):
#         return self.a + self.b
    
#     def product(self):
#         return self.a * self.b

# operations = Mathematics(4 , 5)

# print(operations.suma())
# print(operations.product())


# class Mathematics():
  
#     def suma(self , a , b):
#         return a + b
    
#     def product(self , a , b):
#         return a * b
# #_____________________________________

# operation = Mathematics()
# a = int(input('Enter first number: ')) 
# b = int(input('Enter second number: ')) 


# print(operation.product(a , b))


class Person():

    def __init__(self , name, surname, age , SerialNumber , **kwargs) -> None:
        self.name= name
        self.surname = surname
        self.age = age
        self.SerialNumber = SerialNumber
        self.kwargs = kwargs

    def main_info(self):
        text = f''' 
        name --------> {self.name}
        sumname -----> {self.surname}
        age ---------> {self.age}
        SerialNumber-> {self.SerialNumber}
        '''
        return text
    
    def more_info(self):
        text = ''
        for k , v in self.kwargs.items():
            text += f'{k} ----> {v}\n'
        return text



# Hrayr = Person(name='Hrayr' , surname='Antonyan' , age=20 , SerialNumber='AA00000')
# Karen = Person(name='Karen' , surname='Aleqsanyan' , age=35 , SerialNumber='AA00001')

# print(Hrayr.main_info())
# print(Karen.main_info())





