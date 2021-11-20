import os
import time

# Files and directories for archiving
source = ['N:\\Python', 'N:\\Github']

# Path to archive, if folder don't exist then make folder
arc_directory = 'D:\\Backup'
if os.path.exists(arc_directory) == False:
    os.mkdir(arc_directory)

# For Backup use zip
# Name of zip arc is the current date and time
arc_name = arc_directory + os.sep + time.strftime('%Y-%m-%d-%H-%M-%S') + 'zip'

# Make command for zip util
zip_command = "zip -qr {0} {1}".format(arc_name, ' '.join(source))


# Start backup process
if os.system(zip_command) == 0:
    print('Backup was sucсessfully created')
else:
    print("Can't create backup. ERROR")
