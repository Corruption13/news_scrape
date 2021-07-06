import json
import os
import errno
from slugify import slugify
from random import randint

def writeToCSV(file_name, data_map, file_mode="w+"):
    
    with open(file_name, file_mode) as out_file:
        out_file.write(json.dumps(data_map))


def readFromCSV(file_name, file_mode="r+"):
    with open(file_name, file_mode) as in_file:
        return json.loads(in_file.read())


def create_directory(filename):

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def writeArticleToCSV(source_website, article_list):
    
    for article in article_list:
        file_name = slugify(source_website+ article['title'][:15]) + str(randint(0,10)) # Incase same article title

        with open("Output/"+file_name + ".json", "w+") as json_file:
            json_file.write(json.dumps(article))
        try:
            with open("Output/"+file_name+".csv", "w+",  encoding="utf-8") as csv_file:
                csv_file.write("Title, Link, Keywords, Data\n")
                for related_article in article['related_links_index']:
                    title = related_article[0].replace(",", " ")
                    link = related_article[1]['link'].replace(",", " ")
                    keywords = " ".join(related_article[1]['keywords']).replace(",", " ")
                    csv_file.write("{a},{b},{c}, \n".format(a=title, b=link, c=keywords))
        except Exception as e:
            print(e)
        print("Saving File as", file_name)
