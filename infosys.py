

#!/usr/bin/python
#infosys.py
#2.7.6

import sys
import os
import cPickle as p

class Person(object):
    """information for Person."""
    def __init__(self, name, sex, age, phone, address):
        self.name = name
        self.sex = sex
        self.age = age
        self.phone = phone
        self.address = address

    def __str__(self):
        #print 'Name:', self.name
        #print 'Sex:', self.sex
        #print 'Age:', self.age
        #print 'Phone:', self.phone
        #print 'Address:', self.address
        return 'Name: %s\nSex: %s\nAge: %s\nPhone: %s\nAddress: %s' \
        %(self.name, self.sex, self.age, self.phone, self.address)

index = {}

recordfile = 'infoRecord.dat'

def addRecord():
    global index

    n = raw_input('Name: ')
    s = raw_input('Sex: ')
    a = raw_input('Age: ')
    ph = raw_input('Phone: ')
    ad = raw_input('Address: ')

    op = Person(n, s, a, ph, ad)

    index[n] = op

    f = file(recordfile, 'a')

    p.dump(index, f)
    f.close()


if os.path.exists(recordfile):
    f = file(recordfile)
    index = p.load(f)
    f.close()

if len(sys.argv) < 2:
    print 'a name expected.'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print 'Version: V1.00'
    elif option == 'add':
        addRecord()
    sys.exit()
else:
    checkname = sys.argv[1]
    if checkname in index:
        print index[checkname]
    else:
        print 'there is no record of', checkname, "'s"

