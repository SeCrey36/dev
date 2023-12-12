"""MIX IN"""

class Entity:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class SquareMixin:
    def add_size(self, size_x):
        self.size_x = size_x
        self.size_y = size_x

    def perimeter(self):
        return self.size_x * 4

    def square(self):
        return self.size_x * self.size_x


class SquareEntity(SquareMixin, Entity):
    pass

# запускаем
# $ python3 -i test.py
>>> square = SquareEntity(5, 4)
>>> square.add_size(500)
>>> square.size_x
# 500
>>> square.size_y
# 500
>>> square.square()
# 250000
>>> square.perimeter()
# 2000







"""ДИНАМИЧЕСКОЕ СОЗДАНИЕ КЛАССА"""

def choose_class(name):
  ...     if name == 'foo':
  ...         class Foo(object):
  ...             pass
  ...         return Foo # возвращает класс, а не экземпляр
  ...     else:
  ...         class Bar(object):
  ...             pass
  ...         return Bar
  ...
  >>> MyClass = choose_class('foo')
  >>> print MyClass # функция возвращает класс, а не экземпляр
  <class '__main__.Foo'>
  >>> print MyClass() # можно создать экземпляр этого класса
  <__main__.Foo object at 0x89c6d4c>





type(<имя класса>, 
       <кортеж родительских классов>, # для наследования, может быть пустым
       <словарь, содержащий атрибуты и их значения>)

>>> MyShinyClass = type('MyShinyClass', (), {}) # возвращает объект-класс
>>> print MyShinyClass
<class '__main__.MyShinyClass'>
>>> print MyShinyClass() # создаёт экземпляр класса
<__main__.MyShinyClass object at 0x8997cec>




class Javatpoint:  
     def __init__(self):  
          self._age = 0 
        
     # using the getter function  
     @property 
     def age(self):  
         print("getter method")  
         return self._age  
        
     #now, using the setter function  
     @age.setter  
     def age(self, x):  
         if(x < 20):  
            raise ValueError("the age is below eligibility criteria")  
         print("setter method")  
         self._age = x  
   
John = Javatpoint()  
   
John.age = 25 
   
print(John.age)  
Источник: https://pythonpip.ru/osnovy/gettery-settery-python


class F:
    b = 2
    def __init__(self) -> None:
        self.a = 1
        
    @staticmethod
    def ghb():
        pass
