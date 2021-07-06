import time
from bs4 import BeautifulSoup

# Define Custom Listener Functions in "Listener" module folder. Instuctions given there.
from .Listener.the_hindu import the_hindu_listener

SUPPORTED_NEWS_SOURCES = {  # Map the listener function to the News Source Name.
    "The Hindu": the_hindu_listener
}

### End 

def listener_controller(driver, news_source, must_contain_title_keyword=[], previous_articles=None, sleep_duration=60):    # Listens for new article from source and returns list of new articles found.
    latest_article_list = []
    
    new_article_found = False
    poll_count = 1  # How many times website has been polled since last new article.

    while(not new_article_found):
        if news_source in SUPPORTED_NEWS_SOURCES: # Check if given news source is supported by our software.

            latest_article_list = SUPPORTED_NEWS_SOURCES[news_source](driver)  \
                                or latest_article_list  # If return None, some error occoured with request. So Ignore this iteration.
            
            if not previous_articles:   # First time setup, if no previous articles indexed.
                previous_articles = latest_article_list
                print(news_source, "Initialised Articles.")
                print("Listening for new articles. Sleep duration:", sleep_duration, 'seconds\nPoll Count -> 1', end="")

            else:
                if previous_articles[:3] != latest_article_list[:3]:    # only checking first 3 articles to reduce computation.

                    new_article_list = [d for d in latest_article_list if d not in previous_articles]
                    # Find Set A - Set B for new articles.

                    if must_contain_title_keyword:     # Check if these new articles contain req keyword.
                        for article in new_article_list:
                            for keyword in must_contain_title_keyword:
                                if keyword in article['title']:
                                    break   # Atleast one keyword hit will break loop.
                            new_article_list.remove(article)    # Hence, wont reach this line.
                    
                    if new_article_list:  # If any elements remain in new article list after above checks.
                        print("New Articles Published!!")
                        new_article_found = True
                    else:
                        print("New Articles, but does not contain keyword:", must_contain_title_keyword)
                        previous_articles = latest_article_list
                                          # If no elements remain, reset and continue checking.
                else:
                    poll_count = poll_count + 1
                    print("-> ", poll_count, end="")
                    time.sleep(sleep_duration)

        else:
            print("Invalid News Source.")
        
    


    return new_article_list, latest_article_list








