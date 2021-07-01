import time
from bs4 import BeautifulSoup

INITIAL_ARTICLES_COUNTS = False
# News Sources defined in dictionary at bottom of this file.
# News Source Functions should follow the following structure for IO:
# Take in a Link
# Output a list of article structures.
# Article structure must contain keys: 
# url, title ..


def listener(driver, news_source, link):
    latest_article_list = []
    previous_articles = []
    new_article_found = False

    while(not new_article_found):
        if news_source in NEWS_SOURCE_DICT:
            latest_article_list = NEWS_SOURCE_DICT[news_source](driver)
            if not previous_articles:
                previous_articles = latest_article_list
            else:
                if previous_articles != latest_article_list:
                    print("New Articles Published!!")
                    new_article_found = True
                    previous_articles = latest_article_list
                else:
                    print("No New Articles found. Sleeping for 60s")
        else:
            print("Invalid News Source.")
        
        time.sleep(60)

    print(latest_article_list)
    print('\n\n\n\n\n')
    # O(n**2 logic, make it better sometime.)    
    new_article_list = [d for d in latest_article_list if d not in previous_articles]
    return new_article_list



def the_hindu(driver):

    article_list = []
    driver.get('https://www.thehindu.com/latest-news/')
    html = driver.page_source
    
    soup = BeautifulSoup(html, features="lxml")
    articles = soup.find("ul", class_="latest-news") 

    for a in articles.find_all("li"):
        article = {}
        article['title'] = a.text
        article['link'] = a.find("a", recursive=False)['href']
        article_list.append(article)
    
    #print(article_list)

    debug_file = open("debug.html", 'w+')
    debug_file.write(html)

    return article_list



NEWS_SOURCE_DICT = {
    1: the_hindu
}