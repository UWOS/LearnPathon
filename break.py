

#!usr/bin/python
#break.py
#2.7.6

while  True:
	s = raw_input('Enter something:')
	if  s == 'quit':
		break
	print 'Length of the string is', len(s)
print 'Done'