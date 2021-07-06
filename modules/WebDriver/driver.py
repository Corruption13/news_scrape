# Web driver stuff here.
from selenium import webdriver
from time import sleep

def init_web_driver(DISABLE_IMAGE_LOADING=True):  

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

 
    if DISABLE_IMAGE_LOADING:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)

    print('\nIgnore any warnings above.\n')
    driver.minimize_window()
    return driver


def scroll_down(driver, scroll_limit=5, sleep_time = 2):
    """A method for scrolling the page."""
    # scroll index 
    scroll = 0
    redundancy_time = 0
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        sleep(sleep_time)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height or scroll > scroll_limit:
            if redundancy_time > 3*sleep_time:
                break
            else:
                redundancy_time = redundancy_time + 1
        else:
            redundancy_time = 0
            scroll = scroll + 1
            last_height = new_height