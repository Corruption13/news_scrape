from .content_fetch import content_fetcher

def filter(article_list, customer_filter_words, driver=None):
    cleaned_articles = content_fetcher(article_list, driver)    
    return cleaned_articles