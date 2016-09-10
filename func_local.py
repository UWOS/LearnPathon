

#!/usr/bin/python
#func_local.py
#2.7.6

def func(x):
	print 'x is', x
	x = 2
	print 'Changed local x to', x
	pass

x = 50
func(x)
print 'x is still', x