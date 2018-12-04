#!/user/bin/env python3

import shutil
import os

# Make sure to start the script with the mycode dir
os.chdir('/home/student/mycode')

# Move a file to a new directory
shutil.move('raynor.obj', 'ceph_storage/')

# Prompt the user for some input
xname = input('What is the new name for kerrigan.obj? ')

# Use the input as the new name of the file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
