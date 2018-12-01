#%%
"""
Create a function that reads through a file and prints all the 
lines in uppercase. Be sure to control exceptions that may occur 
here, such as the file not existing
"""

#%%

class EmptyFileError(Exception):
    pass

file = open("quijote.txt")

def convert_to_uppercase(file):
    
    content = file.read()
    
    print(len(fcontent))
    
    if len(file.read()) > 0:
        for line in file:
            print(line.upper())

        
#    if len(file.read()) is 0:
#        
#        raise EmptyFileError()

convert_to_uppercase(file)

#%%