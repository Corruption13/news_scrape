# Main App Module resides here.
# Made by S Sandeep Pillai ©
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

from newsfetch.google import google_search

def app():
    chromedriver_autoinstaller.install()
    print("\nStarting Systems..\n")
    
    news_source = int(input(
        "Enter news source:\n[1] The Hindu\n[2] ANI\n"))
    # user_filter = [str]

    news_target = input("Enter news website to target: ")

    google = google_search('Alcoholics Anonymous', 'https://timesofindia.indiatimes.com/')

    print(google.urls)
    
    #news = listen(news_source)
    #keywords = filter(news, user_filter)



