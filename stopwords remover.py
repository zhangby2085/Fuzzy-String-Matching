# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:11:47 2018
#https://www.tutorialspoint.com/python/python_remove_stopwords.htm
@author: tibozh
"""

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#print stopwords.fileids()
u = en_stops = set(stopwords.words('finnish'))
U = ', '.join(u) #turn set into sr
#all_words = open("./TXT_40.txt").read().split()
all_words = open("./testrun.txt").read().split()
for word in all_words:
    uword = word.decode('utf-8')
    if uword not in en_stops:
        print(uword.encode('utf-8'))
