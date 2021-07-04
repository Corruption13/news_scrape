from bs4 import BeautifulSoup



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
        return None