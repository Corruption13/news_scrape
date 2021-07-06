# Common News Finder Service.
# Made by S Sandeep Pillai ©
# www.github.com/Corruption13\n

import chromedriver_autoinstaller
from modules.app import app
import parameters
import os

def dependency_check():
    chromedriver_autoinstaller.install()
    try:
        os.makedirs('Output')
    except:
        print("Output will be stored in the directory ./Output. Make the folder if it doesnt exist.")
 

if __name__ == "__main__":    
    dependency_check()
    app(parameters.input_parameters)
 
