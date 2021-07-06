# Main App Module resides here.
# S Sandeep Pillai ©

from .listen import listener_controller
from .WebDriver.driver import init_web_driver

from .fetch import fetch_data
from .target import find_relevant_articles
from .analyse import find_link_relevance
from .file import writeToCSV, writeArticleToCSV, readFromCSV


def app(parameters):  # Skeleton Model for project defined as comments.

    print("\nStarting Systems..\n")
    driver = init_web_driver()  # Global Web Driver for Selenium.  
    previous_articles = []
    iteration = 1
    while(iteration < 4):
        print("\n\n\nIteration: ", iteration)
        print(previous_articles[:10])
        previous_articles = app_loop(driver, parameters, previous_articles)
        iteration += 1

    driver.quit()
    print("\n\nShutting Down\nContact @ https://corruption13.github.io/")
    


def app_loop(driver, parameters, previous_articles=None):


    # Listens to a source website for new articles every x seconds

    (new_articles, previous_article_dict) = listener_controller(
                        driver=driver, 
                        news_source=parameters['source_news'], 
                        must_contain_title_keyword=parameters['must_contain_in_title'], 
                        previous_articles=previous_articles, 
                        sleep_duration=45)

    # Tasks to Execute when new articls found.
    article_found_tasks(driver, parameters, new_articles)

    # Return existing articles of source website to restart listening loop again.
    return previous_article_dict


def article_found_tasks(driver, parameters, new_articles):

    # Fetches the article content and finds relevant keywords with NLP.
    cleaned_articles = fetch_data(
                        article_list=new_articles, 
                        customer_filter_words=parameters['remove_keywords'], 
                        driver=driver)
  
    # Intermediette File Output of source website data. 
    #writeToCSV("debug_source_article.json", cleaned_articles, 'w+') # For Debugging.

    # Finds related articles to source and adds to above data structure.
    data_map = find_relevant_articles(
                        driver=driver, 
                        article_list=cleaned_articles, 
                        target_domain=parameters['target_domain'],
                        time_period=parameters['time_period'])

    # Finds Inverse of data_map, returning a link strength JSON
    link_map = find_link_relevance(data_map)
    writeArticleToCSV(parameters['source_news'], link_map)
    print("News Data Recorded.")
    
    #Send Email 
    #send_notification_email(link_map) #TODO
