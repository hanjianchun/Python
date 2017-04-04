# -*- coding:utf-8 -*-

import jieba
import numpy
import codecs
import pandas
import matplotlib.pyplot as plt
#%matplotlib inline

import csv
from wordcloud import WordCloud

file = codecs.open(u"leilei.csv","r")
content = file.read()
file.close()

segment = []
segs = jieba.cut(content)
for seg in segs:
	if len(seg)>1 and seg!='\r\n':
		segment.append(seg)
print segment
words_df = pandas.DataFrame({'segment':segment})
words_df.head()
stopwords = pandas.Series(['不','呀','吗'])
words_df = words_df[~words_df.segment.isin(stopwords)]

word_stat = words_df.groupby(by=['segment'])['segment'].agg({'计数':numpy.size})
word_stat = word_stat.reset_index().sort(columns='计数',ascending=False)
print word_stat.head(100)
