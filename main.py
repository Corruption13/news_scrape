# Common News Finder Service.
# Made by S Sandeep Pillai ©
# www.github.com/Corruption13\n

import chromedriver_autoinstaller
import nltk
from modules.app import app

def dependency_check():
    chromedriver_autoinstaller.install()
    nltk.download('punkt')


if __name__ == "__main__":    
    dependency_check()
    app()
 
