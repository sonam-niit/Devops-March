import shutil

shutil.move('./myfolder','./test_folder')
#moves the file or directory to new location
#if the destination location is on the same file system its like renaming.
#if its diffrent the it copies and deletes the original content.

# Remove Directories
shutil.rmtree('./test_folder')
#its deletes a folder and all its content recoursively

#Creating zip archive
shutil.make_archive('archived','zip','./files')

#Extract an Archive
shutil.unpack_archive('archived.zip','extracted_folder')