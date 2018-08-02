# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:11:47 2018

@author: tibozh
"""

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#print stopwords.fileids()
en_stops = set(stopwords.words('finnish'))
all_words = open("./testrun.txt").read().splitlines()
for word in all_words: 
    if word not in en_stops:
        print(word)
