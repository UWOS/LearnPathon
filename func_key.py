

#!/usr/bin/python
#func_key.py
#2.7.6

def func(a, b = 5, c = 10):
	print 'a is', a, 'and b is', b, 'and c is', c
	pass

func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)
