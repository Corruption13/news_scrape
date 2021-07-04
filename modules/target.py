from GoogleNews import GoogleNews


def target(target_url, topic_list):
    topic_list = ['delivery', '150hike', 'revised', 'cylinder', 'cooking', 'hike', 'price', 'sections', 'leaves', 'return', 'nearly', 'gas', 'money', 'tatters', 'months', 'family', 'kerala', 'budgets']
    target_url = "thehindu"
    googlenews = GoogleNews()
    googlenews.set_lang('en')
    googlenews.set_period('7d')
    googlenews.set_time_range('02/01/2020','02/28/2020')
    googlenews.set_encode('utf-8')
    for topic in topic_list[3]:
        googlenews.get_news(topic)
        news_list = googlenews.results()
        
        for news in news_list[:20]:
            print(news['link'])



target("", [])
