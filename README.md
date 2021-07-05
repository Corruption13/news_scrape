
# Modules

news-fetch
selenium
chromedriver_autoinstaller
bs4
newspaper3k

scrapy/rake/yake NLP module. (or you own, refer ot module/NLP/ for custom functions.)


## Instructions

In the script root directory, execute these commands:

    pip install -r requirements.txt
    python -m spacy download en_core_web_sm [ or en_core_web_md ]

To run the program, type in:

    python3 main.py



## Output Schema


    Intermediete Souce Article Output:

        {
            title: " ",
            'link': " ",
            'data': {
                'content': "     ",
                'authors': " ",
                'publish_date': " "
                'keywords': [str]
            }
            'related_articles:{
                keyword[0]: [
                    {
                        'title': " " ,
                        'link': " ",
                    }
                ]
            }
        }


    Final Output:

        {
            'title': " ",
            'link':  " ",
            'related_links_index': {Sorted_URL_Map}


        }


    (Sorted) URL Map:
        {   
            {
                URL1: [keyword1, keyword2, keyword4, keyword9],
            }
            {
                URL2: [keyword3, keyword9, keyword5],   // Decreasing number of keywords in common.
            }
        
        }
