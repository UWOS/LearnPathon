

#!/usr/bin/python
#class_init.py
#2.7.6

class Person(object):
    """docstring for Person"""
    def __init__(self, name):
        #super(Person, self).__init__()
        self.name = name
    def sayHi(self):
        print 'Hello,my name is', self.name


p = Person('Swaroop')
p.sayHi()

# This short example can also be written as Person('Swaroop').sayHi()