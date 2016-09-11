

#!/usr/bin/python
#str_methods.py
#2.7.6

name = 'Swaroop' # This is a string object

if name.startswith('Swa'):
    print 'Yes,the string starts with "Swa"'
    pass

if 'a' in name:
    print 'Yes,it contains the string "a"'
    pass

if name.find('war') != -1:
    print 'Yes,it contains the string "war"'
    pass

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)