import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
#  add a list of user keywords
with open("KeywordsEnglish.txt") as English:
    Save_keywords = English.read()

wn = nltk.WordNetLemmatizer()
input_keywords = (wn.lemmatize(Save_keywords))

setAList = [input_keywords]
for root in setAList:
    hypoHyper = wordnet.synset(root + '.n.01')
    hypoHyperStr = hypoHyper.name()
    # print(hypoHyperStr)
    # print("it is:", type(hypoHyperStr))
    hypo = lambda s: s.hyponyms()
    hyper = lambda s: s.hypernyms()
    # the make 'Synset' object iterable, I need a closure
    # Compute transitive closures of synsets regarding a relation via breadth-first search

    list(hypoHyper.closure(hypo)) == hypoHyper.hyponyms()
    list(hypoHyper.closure(hyper)) == hypoHyper.hypernyms()
    hyo = list(hypoHyper.closure(hypo))
    hye = list(hypoHyper.closure(hyper))
    # print(hyostr)
    # print(hyo_distance)

for hy in hyo:
    hyoStr = hy.name()
    w1 = wordnet.synset(hypoHyperStr)
    # print("this w1:",w1)
    w2 = wordnet.synset(hyoStr)
    # print("this w2:",w2)
    similarity = w1.wup_similarity(w2)
    # print("this is:", similarity)

for hy in hye:
    c = hy.name()
    w3 = wordnet.synset(hypoHyperStr)
    # print("this w3:",w3)
    w4 = wordnet.synset(c)
    # print("this w4:",w4)
    similarity = w1.wup_similarity(w2)
    # print(similarity)

setAList = [input_keywords]
synonyms = []
for TheList in setAList:
    # print("the is:",TheList)
    for syn in wordnet.synsets(TheList):
        # print("in is:", syn)
        for l in syn.lemmas():
            synonyms.append(l.name())
            semanticKeywords = list(synonyms)
            semanticKeywordsUnique = list(dict.fromkeys(semanticKeywords)) # remove duplicates from a List

print(semanticKeywordsUnique)