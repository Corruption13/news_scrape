from bs4 import BeautifulSoup
from newspaper import Article

def content_fetcher(article_list, driver=None):

    print("Fetching content.")
    for page in article_list:

        data = newspaper3kParser(page['link'])  # Use whatever parser you want, just return str, [list]
        page['content'] = data['content']
        page['keywords'] = data['keywords']

    return article_list

def newspaper3kParser(url):
        # https://github.com/codelucas/newspaper
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
    
            return {
                'content': article.text,
                'authors': article.authors,
                'publish_date': article.publish_date,
                'keywords': article.keywords
                }
                    

        except Exception as e:
            print("No Content Found.")
            print(e)
            return {'content': "", 'authors': "",'publish_date': "",'keywords': [] }

    
if __name__ == '__main__':
    url = input("Enter a URL: ")
    article = newspaper3kParser(url)
    print(article)