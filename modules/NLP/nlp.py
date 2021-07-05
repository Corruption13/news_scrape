import spacy
from rake_nltk import Rake
import yake

# Use any of the functions.
# You may define your own custom NLP and import into ../filter.py 
# KeywordGen function must take in a text string as argument and output a list[] of keywords.

def SpacyKeywordGen(text):

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return doc.ents

def RakeKeywordGen(text):
    
    rake_nltk_var = Rake()    
    rake_nltk_var.extract_keywords_from_text(text)
    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    #print(keyword_extracted)
    return keyword_extracted

def YakeKeywordGen(text):
    
    kw_extractor = yake.KeywordExtractor()
    #text = """spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython. The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion."""
    language = "en"
    max_ngram_size = 2
    deduplication_threshold = 0.955
    numOfKeywords = 10
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = []
    keyword_tuple = custom_kw_extractor.extract_keywords(text)
    for key in keyword_tuple:
        keywords.append(key[0])


    return keywords

