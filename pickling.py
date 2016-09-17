

#!/usr/bin/python
#pickling.py
#2.7.6

import cPickle as p
#import Pickle as p

shoplistfile = 'shoplist.data'
# the name of the file where we will store the object

shoplist = ['apple', 'mango', 'carrot']

#White to the file
f = file(shoplistfile, 'w')
p.dump(shoplist, f)   #dump the object to a file
f.close()

del shoplist   # remove the shoplist

# Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist