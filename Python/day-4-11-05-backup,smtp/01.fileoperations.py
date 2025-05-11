import shutil
#Copy file from source to destination
shutil.copy('./files/source.txt',
            './files/dest.txt')

#copy2 is similar to copy function
#It also preseves file metadata (modification time, access time)
shutil.copy2('./files/source.txt',
             './files/dest1.txt')

#Copy Entire Directory
shutil.copytree('./files',
                './myfolder')