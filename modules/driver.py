    
from selenium import webdriver
DISABLE_IMAGE_LOADING = True

def init_web_driver():  
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    if DISABLE_IMAGE_LOADING:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)

    return driver