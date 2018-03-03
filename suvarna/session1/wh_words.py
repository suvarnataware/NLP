from nltk.corpus import brown
import nltk
cfd = nltk.ConditionalFreqDist(
          (genre, word)
           for genre in brown.categories()
          for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['what', 'when', 'why', 'who', 'which', 'where']
cfd.tabulate(conditions=genres, samples=modals)

#text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
#tokens = text.tokens
#text.tokens
#wh_words = [word for word in tokens if word.startswith('wh')]
# above returns whah', "what're", 'wholly-owned', 'whoa', 'whipped', 'whereas', 'whips', 'wheel', 'whitetail', "where's", 'whoosh', 'what-will-t.', 'wher
#b = set(wh_words)
#print(b)
#cfd.tabulate(conditions=genres, samples=wh_words)