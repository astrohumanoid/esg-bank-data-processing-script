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

# Load English language model
nlp = spacy.load('en_core_web_sm')
print("-----LIB IMPORTED CORRECTLY-----")

df = pd.read_csv(r'list_url_trf(2004).csv')
df['Company Name'] = df['Company Name'].apply(lambda x: re.sub('/qq/', ',', x))
df.index.name = 'index_name'
df_reset = df.reset_index()

def remove_punctuation_words(text):
    words = text.split()
    pattern = r'[a-zA-Z0-9]'

    i = 0
    while i < len(words) :
        if not re.search(pattern, words[i]) :
            words.remove(words[i])
            i -= 1
        i += 1
    cleaned_text = " ".join(words)
    return cleaned_text

def create_txt_file(id, a, b, c, d) :
    filename = "sample/2004/" + str(id) + "_" + str(a) + "_" + str(b) + "_" + str(c)
    print("compiling: " + filename)
    f = open(filename + '_parsed.txt', "r", encoding = "utf-8")
    content = f.read()
    f.close()
    return content

def remove_punctuation_sentences (chunks) :
    i = 0
    while i < len(chunks) :
        words = chunks[i].split()
        pattern = r'[a-zA-Z0-9]'

        alphabet_exists = False
        for word in words :
            if re.search(pattern, word) :
                alphabet_exists = True
                break
        if not alphabet_exists :
            chunks.remove(chunks[i])
            i -= 1
        i += 1
    return chunks

def chunking (id, a, b, c, after_id) :
    if (id > after_id) :
        filename = "sample/2004/" + str(id) + "_" + str(a) + "_" + str(b) + "_" + str(c) + "_parsed.txt"
        with open(filename, 'r', encoding="utf-8") as file :
            text = file.read()
        text = text.replace(" \n", "")
        text = text.replace("\n", " ")

        # Process the text
        doc = nlp(text)

        # Extract sentences
        sentences = [sent.text.strip() for sent in doc.sents]
        sentences_cleaned = remove_punctuation_sentences(sentences)

        # Open a text file in write mode ('w')
        filename = "sample/2004/chunked/" + str(id) + "_" + str(a) + "_" + str(b) + "_" + str(c) + ".txt"
        print("transforming to txt: " + filename)
        with open(filename, 'w+', encoding="utf-8") as file:
            print(sentences_cleaned, file=file)

print("Start chunking...")
print(df_reset.head(5))
df_reset.apply(lambda x : chunking(x['index_name'], x['Year of the report'], x['Quarter of the report'], x['Central Index Key'], 3833), axis = 1)
print("Stop chunking...")
