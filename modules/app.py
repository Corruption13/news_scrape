# Main App Module resides here.
# S Sandeep Pillai ©

from .listen import listener_controller
from .WebDriver.driver import init_web_driver

from .filter import filter
from .target import find_relevant_articles


def app():  # Skeleton Model for project defined as comments.
    while(True):
        app_loop()
        break   # For now.
    # Implement scheduling here if needed.

def app_loop():

    print("\nStarting Systems..\n")
    driver = init_web_driver()  # Global Web Driver for Selenium.   
    
    source_news = "The Hindu"
    topic = "Corona" # Not used rn. TODO
    customer_filter_words = ['Narendra Modi']

    target_domain = ""
    time_period = '7d'
    output_filter = ['BJP']

    new_articles = listener_controller(driver, source_news, topic)
    cleaned_articles = filter(new_articles, customer_filter_words, driver)
    print(cleaned_articles)
    
    link_map = find_relevant_articles(driver, cleaned_articles, target_domain, time_period, output_filter)
    print(link_map)
    #data_map = find_link_relevance(link_map)
    #writeToCSV(data_map)

    # Output -> Links.

    driver.quit()
    print("\n\nShutting Down\n")