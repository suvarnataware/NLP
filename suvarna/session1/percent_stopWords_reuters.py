##Assignment4 - Calculate what percentage of words are stopwords in the reuters corpus 
import nltk
from nltk.corpus import reuters, stopwords
from six.moves import xrange

file_list = reuters.fileids()
#print(len(file_list))
##num_doc can be anything
num_doc=10
remove_top_n=5
corpus = [reuters.words(file_list[i]) for i in xrange(num_doc)]
#print(corpus)
voca = set(w.lower() for w in nltk.corpus.words.words())
print(len(voca))
#total words in corpus reuters
totalWords=len(voca)
stop = stopwords.words('english')
print(len(stop))
for doc in corpus:
    if isinstance(doc, str):
        doc = word_tokenize(doc)
doc = [word.lower() for word in doc if word.lower() in voca and word.lower()  in stop and len(word) != 1]
#print(doc)
#print(len(doc))
#total stops words in corpus reuters
totalStopWords=len(doc)
percent=totalStopWords*100/totalWords

#Percent Stop Words
print("percentage of stop words ",percent)

#plot which stopword and its count

fdist = nltk.FreqDist(doc)
#for word, frequency in fdist.most_common(50):
#    print(u'{};{}'.format(word, frequency))
fdist.plot()

#question - how to plot stopsword per file