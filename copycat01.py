#!/usr/bin/env python3

import shutil
import os

os.chdir('/home/student/mycode/')

# Copy a file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

# Copy a directory tree
shutil.copytree('5g_research/', '5g_research_backup/')
