

#!/usr/bin/python
#using_dict.py
#2.7.6

ab = {'Swaroop' : 'swaroopch@byteofpython.info',
'Larry' : 'larry@wall.org',
'Matsumoto' : 'matz@ruby-lang.org',
'Spammer' : 'spammer@hotmail.com'
}

print "Swaroop's address is %s" %ab['Swaroop']

ab['Guido'] = 'guido@python.org'

del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s' %(name, address)
    pass

if  'Guido' in ab:   # OR ab.has_key('Guido')
    print "\n Guido's address is %s" %ab['Guido']
    pass