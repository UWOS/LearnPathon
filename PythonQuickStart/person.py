#! python3

# person.py

class Person:
    """ Class to  represent a person
    """

    #def __init__(self):
    def __init__(self, name = '', age = 0):
        self.__name = name
        self.__age = age

    def display(self):
        #print("Person('%s', %d)" %(self.__name, self.__age))
        #print(str(self))   # 在有了__str__以后。
        print(self)   # 在有了__repr__以后。

    def __str__(self):
        return "Person('%s', %d)" %(self.__name, self.__age)

    def __repr__(self):
        return str(self)   # 大部分情况下，__repr__与__str__相同。

    @property
    def age(self):
        """ Returns this person's age.
        """
        return self.__age
    
    # def set_age(self, age):
    #     if 0 < age <= 150:
    #         self._age = age
    # 使用装饰器重写set_age。

    @age.setter
    def age(self, age):
        if 0 < age <= 150:
            self.__age = age
    
            
    
