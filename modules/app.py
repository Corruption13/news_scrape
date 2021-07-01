# Main App Module resides here.
# Made by S Sandeep Pillai ©

from .listen import listener
from .driver import init_web_driver


def app():

    driver = init_web_driver()
    
    #news_source = int(input(
    #    "Enter news source:\n[1] The Hindu\n[2] ANI\n"))
    # user_filter = [str]

    #news_target = input("Enter news website to target: ")

    articles = listener(driver, 1, "boo")
    print(articles)
    #news = listen(news_source)
    #keywords = filter(news, user_filter)
    driver.quit()


