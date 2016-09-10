

#!/usr/bin/python
#func_global.py
#2.7.6

def func():
	global x

	print 'x is', x
	x = 2
	print 'Changed local x to', x
	pass

x = 50
func()
print 'Value of x is', x