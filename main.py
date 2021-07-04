# Common News Finder Service.
# Made by S Sandeep Pillai ©
# www.github.com/Corruption13\n

import chromedriver_autoinstaller
from modules.app import app

def dependency_check():
    chromedriver_autoinstaller.install()
    



if __name__ == "__main__":    
    dependency_check()
    app()
 
