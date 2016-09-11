

#!/usr/bin/python
#using_sys.py
#2.7.6

import sys

print ('The command line arguments are:')
for i in sys.argv:
    print (i)
    pass

print ('\n\nThe PYTHONPATH is', sys.path, '\n')