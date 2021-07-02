# For testing python stuff lol
a = [{'hey': '1' },{ 'yo': '2'}]

b = [{'hey': '3' }, {'yo': '2'}, {'ko': '2'}, {'do': '2'}]

print(b[2:])



z = [d for d in a if d not in b]
print(z)


article_list = [{'title': '\nNearly ₹150-hike in gas price in five months leaves family budgets in tatters in Kerala  | Kerala, 16:16\n', 'link': 'https://www.thehindu.com/news/national/kerala/nearly-150-hike-in-gas-price-in-five-months-leaves-family-budgets-in-tatters-in-kerala/article35096630.ece'}]



















############################# Archived
html_article_div_tag_ID = {'The Hindu': 'content-body-14269002-35096630', } 
html_article_div_tag_CLASS = {}

def content_fetcher_2(driver, article_list):
    
    for article in article_list:
        try:
            driver.get(article['link'])
            html = driver.page_source
        except:
            print("Check your Internet Connection.")
            continue 
        soup = BeautifulSoup(html, features="lxml")
        article['content'] = content_finder_loop(soup).text


def content_finder_loop(soup):
                                                    # Supported Websites defined above.
    ID_List = [*html_article_div_tag_ID.values()]       # Some Websites put content in a div tag with ID identifier
    Class_List = [*html_article_div_tag_CLASS.values()] # Some Websites put content in a div tag with Class identifier

    for website_tag in ID_List:
        content = soup.find("div", id=website_tag)
        if content:
            return content
    for website_tag in Class_List:
        content = soup.find("div", class_=website_tag)
        if content:
            return content 
    else:
        return "No Content Found"