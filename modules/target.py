from bs4 import BeautifulSoup
from time import sleep as timesleep

def find_relevant_articles(driver, article_list, target_domain, time_period=None, filter = None):

    for article in article_list:
        print("\n\nKeywords: ", article['data']['keywords'], '\n Keyword Articles Count', end="")
        article['related_articles'] = target(driver, target_domain, article['data']['keywords'], time_period, filter)

    return article_list

def target(driver, target_domain, topic_list, time_period=None, filter = None):

    keyword_map = {}
    for topic in topic_list:
        
        print(' | ' + topic, end=" -> ")
        url = construct_google_news_url(target_domain, topic, time_period, filter)
        keyword_map[topic] = google_news_search(driver, url)
        timesleep(2)

    return keyword_map



def construct_google_news_url(news_site_domain, keywords, time_period=None, filter=None):

        # typical google news url = https://news.google.com/search?q=keyword-here%20site%3Awww.news-site.com%20when%3A1y

        allowed_time_periods = ['1h', '1d', '7d', '1y']
        
        base_url = "https://news.google.com/search?q="
        query = keywords.replace("/", "")
        target_site = '%' + '20site%3A' + news_site_domain.replace("https://", "").replace("/", "")

        if time_period not in allowed_time_periods:
            time = ''
        else:
            time_period = '%' + '20when' + '%' +  '3A' + time_period
        if filter: 
            filter = " -" + " ".join(filter)
        else:
            filter = ""

        final_url = base_url + query + target_site + time_period + filter
        #print("URL: "+ final_url)

        return final_url

def google_news_search(webdriver, news_url):

    article_list = []
    webdriver.get(news_url)
    html = webdriver.page_source
    soup = BeautifulSoup(html, features="lxml")
    articles = soup.find_all("a", class_="DY5T1d RZIKme") 
    print(len(articles), end="")
    if not articles:
        #print("No Results!")
        pass
    else:
        for article in articles:
            link = "https://news.google.com" + article['href'][1:]
            title = article.text
            #print("Title: ", title)
            article_list.append({'title':  title, 'link': link})


    return article_list




# For Debug Purposes Only.
if __name__ == '__main__':

    import chromedriver_autoinstaller
    from WebDriver.driver import init_web_driver
    import json

    chromedriver_autoinstaller.install()
   
    keyword_list = ['delivery', '150hike', 'revised', 'cylinder', 'cooking' , 'price', 'sections', 'leaves', 'return', 'nearly', 'gas', 'money', 'tatters', 'months', 'family', 'kerala', 'budgets']
    target_domain = "timesofindia.indiatimes.com"
    time_period = '7d'
    filter = None

    driver = init_web_driver()
    keyword_map = target(driver, target_domain, keyword_list, time_period, filter)

    file = open("debugmap.json", "w+")
    file.write(json.dumps(keyword_map))
    file.close()
    driver.close()