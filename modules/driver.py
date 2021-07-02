    
# Web driver stuff here.
from selenium import webdriver
DISABLE_IMAGE_LOADING = True

def init_web_driver():  

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

 
    if DISABLE_IMAGE_LOADING:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)

    print('\n\n\nIgnore any warnings above.\n')

    return driver