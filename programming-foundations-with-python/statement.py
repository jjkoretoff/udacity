# the objective of this function is to take a set of files in a folder and
# rename them without numbers attached to their names

# access os files in py
import os

# define an empty function that has the same name as this file
def statement ():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/johnkoretoff/code/udacity/programming-foundations-with-python/alphabet")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir("/Users/johnkoretoff/code/udacity/programming-foundations-with-python/alphabet")
    #(2) for each file, rename file
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    
statement()
