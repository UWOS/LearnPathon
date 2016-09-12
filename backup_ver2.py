

#!/usr/bin/python
#backup_ver2.py
#2.7.6

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/home/uwos/python', '/home/uwos/Git-Local']

# 2. The backup must be stored in a main backup directory
target_dir = '/home/uwos/exbackup/'

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if  not os.path.exists(today):
    os.mkdir(today)   # make diretory
    print 'Successfully created directory', today
    pass

# The name of the zip file
target = today + os.sep + now + '.zip'   # os.sep,seprator sign fit current os automatically.

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" %(target, ' '.join(source))

# Run the backup
if  os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'