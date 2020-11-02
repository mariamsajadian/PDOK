# https://metacpan.org/pod/release/TPEDERSE/WordNet-Similarity-1.03/lib/WordNet/Similarity/wup.pm
from nltk.translate import *
from nltk.corpus import wordnet
import nltk

input_keys = "schools"
input_keys_compare = "school"
# with open("KeywordsEnglish.txt") as English:
#     Save_keywords = English.read()
#     # print(Save_keywords)
# with open("AnswerKeywordsEnglish.txt") as English:
#     answer_keywords = English.read()
# key_list = Save_keywords.split('\n')
# input_keywords = input_keys
# input_keywords_compare = input_keys_compare

wn = nltk.WordNetLemmatizer()
input_keywords = (wn.lemmatize(input_keys))
# input_keywords_compare = (wn.lemmatize(input_keys_compare))
# print(input_keywords_compare)
print(input_keywords)

# w1 = wordnet.synset(input_keywords + '.n.01')
# # print(type(w1))
# w2 = wordnet.synset(input_keywords_compare + '.n.01')
# a = w1.wup_similarity(w2)
# print(a)
# if a == 1.0:
#     print("yes")
# else:
#     print("no")

syns = wordnet.synsets(input_keywords)
print(syns[0].name())
print(set(syns))
print("------------+++++++++------------------")
# Get the synonyms
newKeyword = "arcade"
synonyms = []
for syn in wordnet.synsets(newKeyword):
    for l in syn.lemmas():
        synonyms.append(l.name())
semanticKeywords = set(synonyms)
print(semanticKeywords)
print("---------------------")

print("--------Hyponyms = details syn-----")

w1 = wordnet.synset(input_keywords + '.n.01')
w2 = wordnet.synset(input_keys_compare + '.n.01')
print(w1.wup_similarity(w2))
print("---------------------")
#
w1 = wordnet.synset(newKeyword + '.n.01')
# print(type(w1))
w2 = wordnet.synset("building" + '.n.01')
print( w1.wup_similarity(w2))
# print(type(w1.wup_similarity(w2)))
# print(w1.distance(w2))
print("---------------------")