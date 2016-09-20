

#!/usr/bin/python
#lambda.py
#2.7.6

def make_repeater(n):
    return lambda s: s * n

twice = make_repeater(2)

print twice('word')
print twice(5)