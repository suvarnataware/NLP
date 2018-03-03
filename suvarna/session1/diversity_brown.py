import nltk
from nltk.corpus import brown
#for cat in nltk.corpus.brown.categories():
diversity_score={}
for cat in ('romance','humor','fiction'):
    words_in_cat = nltk.corpus.brown.words(categories=cat)
    diversity_score[cat]=float(len(words_in_cat)) / len(set(words_in_cat));
    #diversity_score.append(float(len(words_in_cat)) / len(set(words_in_cat)));
    print ("lexical Diversity score for category "+cat + " {:3g}".format( float(len(words_in_cat)) / len(set(words_in_cat)) ))


print("Genre having maximum diversity is "+max(diversity_score.keys(), key=(lambda k: diversity_score[k])))


