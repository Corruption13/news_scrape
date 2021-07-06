from newspaper import Article
from .NLP.nlp import SpacyKeywordGen, YakeKeywordGen, RakeKeywordGen
NLP_Functions = {
    'spacy': SpacyKeywordGen,
    'yake': YakeKeywordGen,
    'rake': RakeKeywordGen,
}
# Use custom NLP function if needed, just take String Text as argument and output a list[] of keywords.
PARSER = "spacy" # Pre Made NLP: spacy, yake, rake

def fetch_data(article_list, customer_filter_words, driver=None):

    print("Fetching content.")
    for page in article_list:
        # Use whatever parser you want, just return str, [list]
        page['data'] = newspaper3kFetcher(page['link'])


    cleaned_articles = custom_cleaner(article_list, customer_filter_words)
    return cleaned_articles

def custom_cleaner(article_list, remove_keyword):
    
    # Add custom filter here. - Done.
    for article in article_list:
        article['data']['keywords'] = [x for x in article['data']['keywords'] if x not in remove_keyword]

    return article_list


def newspaper3kFetcher(url, include_content=False):
    # https://github.com/codelucas/newspaper
    try:
        article = Article(url)
        article.download()
        article.parse()
        keywords = NLP_Functions[PARSER](article.text)  # refer to nlp_functions.py
        article.nlp()
        data= {'content': article.text,
               'authors': article.authors,
               'publish_date': article.publish_date,
               'keywords': article.keywords }
        if include_content:
            data['content']= article.text
        
        return data
    
    except Exception as e:
        print("No Content Found. Error:")
        print(e)
        return {'content': "", 'authors': "",'publish_date': "",'keywords': [] }


# For debugging Purposes.
if __name__ == '__main__':
    url = input("Enter a News URL: ")
    article = newspaper3kFetcher(url)
    print("Parser Used: " + PARSER)
    print(article['keywords'])