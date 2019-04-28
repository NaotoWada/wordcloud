from collections import Counter
from os import path
from PIL import Image
import os

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import MeCab as mc
import pandas as pd

import numpy as np

STOP_WORDS = ['し','かも','しまい','たい','する', \
              'なく','い','られる','いき','れ', \
              'なる','れる','み','こと','ば', \
              'かけ','でき','そう','もの','いれ', \
              'なっ','せ']
WORDS_OUTPUT_LIMIT = 45
FONT_PATH = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
RESULT_IMG_PATH = './wc.png'
MASK_PATH = "./data/cloud.png"
CSV_PATH = './data/sample.csv'
FETCH_COLUMNS = 'title'
VALID_TYPES = ['形容詞','動詞','名詞']

"""Analyze words using Mecab"""
def mecab_analyze_chasen(words):
    print("--mecab_analyze_chasen start--")
    t = mc.Tagger('-Ochasen')
    out = []
    for txt in words :

        node = t.parseToNode(txt)
        while(node):

            if node.surface == "" : 
                # header or footer
                node = node.next
                continue

            # append if type is matched terms.
            word_type = node.feature.split(",")[0]
            if word_type in VALID_TYPES :
                out.append(node.surface)
            node = node.next

    print("--mecab_analyze_chasen end--")
    return out


"""Create wordcloud data then show as plt"""
def create_wordcloud(text):
    print("--create_wordcloud start--")

    mask = np.array(Image.open(MASK_PATH))

    # freq function is NOT valid stop_words attribute
    wordcloud = WordCloud(background_color="white",
                          # contour_width=2, # use if wanna draw border line of masks
                          # contour_color='steelblue', # use if wanna paint color border line of masks
                          mask=mask,
                          font_path=FONT_PATH,
                          width=900,
                          height=500, 
                          max_words=WORDS_OUTPUT_LIMIT).generate_from_frequencies(text)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    
    return wordcloud
    print("--create_wordcloud end--")


"""Read csv file as value"""
def read_csv_resources() :
    print("--read_csv_resources start--")

    df = pd.read_csv(CSV_PATH)
    out = df[FETCH_COLUMNS].values

    print("--read_csv_resources end--")
    return out


"""Remove specific word from input words.Not desctuct function."""
def remove_stop_word(words):
    print("--remove_stop_word start--")

    out = []
    for text in words :
        if text not in STOP_WORDS :
            out.append(text)

    print("--remove_stop_word end--")
    return out


"""
Create wrodcloud picture img from csv word data.
Using Mecab library version 0.7(insure function only this version. ver0.9.6.6 might be unexpected result)
If you want to create wordcloud img as other surface, replace img file [./data/msk.img] which is black and white color only(white is background)
"""
def execute() :
    csv = read_csv_resources()
    analyzed = mecab_analyze_chasen(csv)

    removed = remove_stop_word(analyzed)
    c = Counter(removed)
    print(c)

    wordcloud = create_wordcloud(c)
    wordcloud.to_file(RESULT_IMG_PATH)

# do execute
execute()

