import codecs
from nltk.tag import tnt
import pickle
import sys

if len(sys.argv)<3:
    print "Format: python tnt_tagger.py train_file test_file"
    exit(0)
else:
    script,trainf,testf = sys.argv

tnt_tagger = tnt.TnT()
train = codecs.open(trainf,'rb',encoding='utf-8')
test = codecs.open(testf,'rb',encoding='utf-8')
train_data = train.readlines()
test_data = test.readlines()
train_li,test_li = [],[]

for line in train_data:
    m = line.split('\t')
    sent = []
    if len(m)>1:
        a,b = m[0].strip(),m[1].strip()
        for j in b.split():
            tu = j.split('8908')
            if len(tu)>1:
                sent.append(tuple([tu[0],tu[1]]))
    train_li.append(sent)

for line in test_data:
    m = line.split('\t')
    sent = []
    if len(m)>1:
        a,b = m[0].strip(),m[1].strip()
        for j in b.split():
            tu = j.split('8908')
            if len(tu) > 1:
                sent.append(tuple([tu[0],tu[1]]))
    test_li.append(sent)
"""
for sent in test_li:
    print sent
    for w,t in sent:
        print w,t
"""
tnt_tagger.train(train_li)
f = open('tnt_treebank_pos_tagger.pickle', 'w') 
pickle.dump(tnt_tagger, f)
f.close()
print tnt_tagger.evaluate(test_li)
