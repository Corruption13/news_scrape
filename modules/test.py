# For testing python stuff lol
a = [{'hey': '1' },{ 'yo': '2'}]

b = [{'hey': '3' }, {'yo': '2'}, {'ko': '2'}, {'do': '2'}]

print(b[2:])



z = [d for d in a if d not in b]
print(z)


article_list = [{'title': '\nNearly ₹150-hike in gas price in five months leaves family budgets in tatters in Kerala  | Kerala, 16:16\n', 'link': 'https://www.thehindu.com/news/national/kerala/nearly-150-hike-in-gas-price-in-five-months-leaves-family-budgets-in-tatters-in-kerala/article35096630.ece'}]

text = "NEW DELHI: Having played a role in handling the security situation in Jammu and Kashmir after the abrogation of Article370, National Security Advisor Ajit Doval has been working behind the ongoing political process in the Union territory.The Centre's effort led by the ministry of home affairs to engage with the political parties would see an all-party meeting on June 24 which will be chaired by Prime Minister Narendra Modi . The NSA has been working all along for pushing this political process in the Union territory which used to be a state prior to August 2019 when Article 370 was removed, sources said.The NSA has also been holding meetings with the junior level leadership at different levels to know the ground situation, they said.Post Article 370 abrogation, the NSA had camped in the state for many days and met the people there at a time when it was being felt that there would be a strong response to the central decision.In the recent past also, he has been involved in the process to ensure the observance of the ceasefire agreements between the armies of India and Pakistan along the Line of Control. The guns of the two sides have also remained silent for more than 110 days now.Army chief Gen Manoj Mukund Naravane has also been reviewing the ground situation regularly and keeping the situation under control."

import os
dir_path = os.path.abspath("./modules")
print(dir_path)
#import spacy
#nlp = spacy.load("en_core_web_sm")

#doc = nlp(text)
#print(list(doc.ents))


stri = "123456789"

listi = [{"Apple":{"link": "A", "art": ['1', '2']}}]
print(list(listi[0].keys())[0])

a = "123"
b = "ABC"
c = ".exe"

print("{a} , {b}, {c},".format(a=a, b=b, c=c))











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