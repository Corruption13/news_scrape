# Analysing URL strength with relation to the keywords.
# Simply finds common occourance of a link among the source article's keywords.



def find_link_relevance(article_list):

    result_list = []
    for article in article_list:
        result_list.append({
                'title': article['title'],
                'link': article['link'],
                'related_links_index': link_strength(article)
                }
            )
    return result_list


def link_strength(article):

    url_map = {}
    related_articles = article['related_articles']
    for keyword in related_articles:
        
        for url in related_articles[keyword]:
            if url['title'] in url_map:
                url_map[url['title']]['keywords'].append(keyword)
            else:
                url_map[url['title']] = {
                    'keywords': [keyword],
                    'link': url['link']
                }
    
    sorted_url_map = sorted(url_map.items(), key=lambda x: len(x[1]['keywords']), reverse=True) # Sort URL map my count of keywords
    return sorted_url_map

    



'''
    (Sorted) URL Map Sc:
    {   
        {
            URL1: [keyword1, keyword2, keyword4, keyword9],
        }
        {
            URL2: [keyword3, keyword9, keyword5],
        }
    
    }
'''