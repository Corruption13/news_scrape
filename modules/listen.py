import time
from bs4 import BeautifulSoup


# News Sources defined in dictionary at bottom of this file.
# News Source Functions should follow the following structure for IO:
# Take in a Link
# Output a list of article structures. If Empty list, return a None (IMPORTANT!)
# Article structure must contain keys: 
# url, title ..


def listener_controller(driver, news_source, link, IGNORE_INITIAL_ARTICLES = True):    # Listens for new article from source and returns list of new articles found.
    latest_article_list = []
    previous_articles = []
    new_article_found = False
    poll_count = 0  # How many times website has been polled since last new article.

    while(not new_article_found):
        if news_source in SUPPORTED_NEWS_SOURCES: # Check if given news source is supported by our software.
            latest_article_list = SUPPORTED_NEWS_SOURCES[news_source](driver) or latest_article_list
            if not previous_articles and IGNORE_INITIAL_ARTICLES:
                previous_articles = latest_article_list
                print("\nInitialised Articles.")
            else:
                if previous_articles[:3] != latest_article_list[:3]:
                    print("New Articles Published!!")
                    new_article_found = True
                else:
                    poll_count = poll_count + 1
                    print(str(poll_count) + " -> No New Articles found. Sleeping for 60s")
                    time.sleep(60)
        else:
            print("Invalid News Source.")
        
    #debug    
    print(latest_article_list)
    print('\n\n AND \n\n')
    print(previous_articles)
    print('\n\n\n\n\n')
    # O(n**2 logic, make it better sometime.)    
    new_article_list = [d for d in latest_article_list if d not in previous_articles]
    return new_article_list



def the_hindu_listener(driver):

    article_list = []
    try:
        driver.get('https://www.thehindu.com/latest-news/')
    except:
        print("Check your Internet Connection.")
        return None

    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")
    articles = soup.find("ul", class_="latest-news") 

    for a in articles.find_all("li"):
        article = {}
        article['title'] = a.text
        article['link'] = a.find("a", recursive=False)['href']
        article_list.append(article)
    
    #print(article_list)

    if article_list:
        return article_list 
    else:
        return None



SUPPORTED_NEWS_SOURCES = {  # Map the listener function to the News Source Name.
    "The Hindu": the_hindu_listener
}