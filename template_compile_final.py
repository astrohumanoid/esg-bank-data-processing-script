import numpy as np
import pandas as pd
import csv
import re
import requests
from html.parser import HTMLParser as htmlpar
from bs4 import BeautifulSoup
import html2text
import html
import spacy
import ast

import ast 

df = pd.read_csv(r'list_url_trf(2004).csv')
df['Company Name'] = df['Company Name'].apply(lambda x: re.sub('/qq/', ',', x))
df.index.name = 'index_name'
df_reset = df.reset_index()

f = open('dictionary.txt', 'r')
content = f.read()
words = content.split(',')
dictionary_esg = [word.strip() for word in words]
print("-----DICTIONARY IMPORTED CORRECTLY-----")
f.close()

def is_word_in_string(word, string):
    # Convert both the word and the string to lowercase (or uppercase)
    word_lower = word.lower()
    string_lower = string.lower()
    
    # Check if the word exists in the string
    if word_lower in string_lower:
        return True
    else:
        return False

def finalize_csv(id, a, b, c, after_id) :
    if (id > after_id) : 
        filename = "sample/2004/chunked/" + str(id) + "_" + str(a) + "_" + str(b) + "_" + str(c) + ".txt"
        with open(filename, 'r', encoding="utf-8") as file :
                text = file.read()
        
        sentences = ast.literal_eval(text)

        relevant_sentences = []

        # Print the extracted sentences
        for i in range(len(sentences)):
            dictio = list()
            relevance = False
            for word in dictionary_esg:
                formula = '[^A-Za-z0-9]+' + word.lower() + '[^A-Za-rt-z0-9]+'
                #if is_word_in_string(word, sentences[i]):
                if re.search(formula, sentences[i].lower()):
                    relevance = True
                    if not word in dictio : 
                        dictio.append(word)
            if relevance:
                relevant_sentences.append((i, sentences[i], dictio))
            del dictio

        # Open a text file in write mode ('w')
        filename = "sample/2004/relevant/" + str(id) + "_" + str(a) + "_" + str(b) + "_" + str(c) + ".txt"
        print("finalizing: " + filename)
        with open(filename, 'w+', encoding="utf-8") as file:
            # Write some text to the file
            for sent in relevant_sentences :
                print(sent, file=file)

print(df.head(5))
df_reset.apply(lambda x : finalize_csv(x['index_name'], x['Year of the report'], x['Quarter of the report'], x['Central Index Key'], 3833), axis = 1)