# Common News Finder Service.
# Made by S Sandeep Pillai ©
# www.github.com/Corruption13\n

import chromedriver_autoinstaller
from modules.app import app
import os, sys

def dependency_check():
    chromedriver_autoinstaller.install()
    import sys, os
    sys.path.append(os.path.abspath("./news_scrape/modules"))
 



if __name__ == "__main__":    
    dependency_check()
    app()
 
