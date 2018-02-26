
import os

def get_uploaded_images():
    list = []
    rootdir = os.getcwd()
    print rootdir 
    for subdir, dirs, files in os.walk(rootdir + '/static/uploads'):
     for file in files:
        list.append(file)
        print list
    
