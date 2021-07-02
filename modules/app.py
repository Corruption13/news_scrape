# Main App Module resides here.
# S Sandeep Pillai ©

from .listen import listener_controller
from .driver import init_web_driver

from .filter import filter

def app():  # Skeleton Model for project defined as comments.

    print("\nStarting Systems..\n")
    driver = init_web_driver()  # Global Web Driver for Selenium.   
    

    new_articles = listener_controller(driver, "The Hindu", "Corona")
    cleaned_articles = filter(new_articles, [], driver)
    print(cleaned_articles)
    #links = find_relevant_news(cleaned_articles['keywords])
    # Output -> Links.

    driver.quit()
    print("\n\nShutting Down\n")




# Input variables

#news_source = int(input(
#    "Enter news source:\n[1] The Hindu\n[2] ANI\n"))
# custom_user_filter = [str,]
#news_target = input("Enter news website to target: ")
