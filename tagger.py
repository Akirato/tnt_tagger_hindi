#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import pickle
import nltk
import sys
import codecs

if len(sys.argv)<3:
    print("Format: python tagger.py input-file output-format")
    exit(0)
else:
    script,inp,typ = sys.argv

f = open('tnt_treebank_pos_tagger.pickle','rb')
tnt_tagger = pickle.load(f)

data = codecs.open(inp,'rb').readlines()
if typ != 'terminal':
    out = codecs.open(typ,'wb',encoding='utf-8')

count = 0
for line in data:
    print("Line Number:",count,file=out)
    for i in tnt_tagger.tag(nltk.word_tokenize(line.decode('utf-8'))):
        if typ == 'terminal':
            print(i[0],'\t',i[1])
        else:
            print(i[0],'\t',str(i[1]),file=out)
    count+=1
if typ != 'terminal':
    out.close()

