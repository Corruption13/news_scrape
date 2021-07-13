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
        print("\nOutput will be stored in the directory ./Output.\nMake the folder if script can't create it.")
 

if __name__ == "__main__":    
    dependency_check()
    app(parameters)
 
