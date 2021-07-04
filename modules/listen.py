import time
from bs4 import BeautifulSoup

from Listeners.the_hindu import the_hindu_listener
# Define Custom Listener Functions in "Listener" module folder. Instuctions given there.


SUPPORTED_NEWS_SOURCES = {  # Map the listener function to the News Source Name.
    "The Hindu": the_hindu_listener
}

### End 

def listener_controller(driver, news_source, topic=None, IGNORE_INITIAL_ARTICLES = True):    # Listens for new article from source and returns list of new articles found.
    latest_article_list = []
    previous_articles = []
    new_article_found = False
    poll_count = 0  # How many times website has been polled since last new article.

    while(not new_article_found):
        if news_source in SUPPORTED_NEWS_SOURCES: # Check if given news source is supported by our software.

            latest_article_list = SUPPORTED_NEWS_SOURCES[news_source](driver, topic)  \
                                or latest_article_list  # If return None, some error occoured with request. So Ignore this iteration.
            
            if not previous_articles and IGNORE_INITIAL_ARTICLES:   # First time setup.
                previous_articles = latest_article_list
                print("\nInitialised Articles.")

            else:
                if previous_articles[:3] != latest_article_list[:3]:    # only checking first 3 articles to reduce computation.
                    print("New Articles Published!!")
                    new_article_found = True
                else:
                    poll_count = poll_count + 1
                    print(str(poll_count) + " -> No New Articles found. Sleeping for 60s")
                    time.sleep(60)

        else:
            print("Invalid News Source.")
        
    new_article_list = [d for d in latest_article_list if d not in previous_articles]
    
    return new_article_list








