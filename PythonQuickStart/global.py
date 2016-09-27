#! python3

# global.py

name = 'Jack'

def say_hello():
    print('Hello ' + name + '!')
def change_name(new_name):
    global name            # added after error
    name = new_name
