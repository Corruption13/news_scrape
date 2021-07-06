from bs4 import BeautifulSoup

#
#
# News Source Listener Functions should follow the following structure for I/O:
# Function Argument: Selenium webdriver, [topic]
# Return a LIST[] of article json. If Empty list, return a None instead. (IMPORTANT!)
# Article json must contain keys: 
# {'title': '', 'link': ' '}
# Follow this format to implement your own listener for other websites.
# Import and add that listener in listen.py
#
#

def the_hindu_listener(driver, topic=None):
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
        print("(Webpage didn't load)", end="")
        return None