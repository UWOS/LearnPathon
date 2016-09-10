

#!/usr/bin/python
# if.py
#2.7.6

number = 23
guess = int(raw_input('Enter an integer: '))

if  guess == number:
	print 'Congratulations,you guessed it.'   # New block start here
	print "(but you do not win any prizes!)"   # New block ends here
elif guess < number:
	print 'No,it is alittle lower than that'
	# you must have guess > number to reach here

print 'Done'
