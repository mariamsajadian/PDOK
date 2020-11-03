import nltk
from nltk.corpus import wordnet

#  add a list of user keywords
with open("KeywordsEnglish.txt") as English:
    Save_keywords = English.read()
    # print(Save_keywords)
    # key_list = Save_keywords.split('\n')
    # print(len(Save_keywords)) # check the len of characters I had 9 for "schools"

wn = nltk.WordNetLemmatizer()
input_keywords = (wn.lemmatize(Save_keywords))
print(input_keywords)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

synonyms = []
for syn in wordnet.synsets(input_keywords):
    for l in syn.lemmas():
        synonyms.append(l.name())
semanticKeywords = set(synonyms)
print(semanticKeywords)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


###### translate and query
###### call functions from other files
###### from QueryTest.py query()

print("--------Hyponyms = details syn-----")
print("https://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html#Lemma")
print("https://www.nltk.org/howto/wordnet.html")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
dog = wordnet.synset(input_keywords + '.n.01')
hypo = lambda s: s.hyponyms()
hyper = lambda s: s.hypernyms()
list(dog.closure(hypo, depth=1)) == dog.hyponyms()

# school, frog
list(dog.closure(hyper, depth=1)) == dog.hypernyms()
hyo = list(dog.closure(hypo))
hye = list(dog.closure(hyper))
print(hyo)
print(hye)

print("-------------------similarity-----------------")
w1 = wordnet.synset(input_keywords + '.n.01')
# print(type(w1))
w2 = wordnet.synset('employee.n.01')
print( w1.wup_similarity(w2))
# print(type(w1.wup_similarity(w2)))
# print(w1.distance(w2))
print("---------------------")


