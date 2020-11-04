import nltk
import numpy as np

from nltk.corpus import wordnet

#  add a list of user keywords
with open("KeywordsEnglish.txt") as English:
    Save_keywords = English.read()
    # print(Save_keywords)
    spaceReplace = Save_keywords.replace(" ", "_")
    key_list = spaceReplace.split('\n')
    print(key_list)
    # print(type(key_list)) ## list
    # print(len(key_list)) # check the len of characters I had 9 for "schools"
# test output for the keywords
# list must to be
# "outputTest" is the file name and "key_list" is our container consists of keywords in the right format
# with open("outputTest" + ".txt", "w") as w:
#     for listWords in key_list:
#         w.write('%s\n' % listWords)
# print("<<< don't forget google API here! <<<")
#
# print(">>>add keywords one by one in the Lemmatizer and create separate list>>>")

# print("<<<<<<<<<<<<<  Lemmatizer  <<<<<<<<<<<<<<<<<<<<<")

arr = np.array(key_list)
print(type(arr))
wn = nltk.WordNetLemmatizer()
for i in arr:
       input_keywords = (wn.lemmatize(i))
       # print(input_keywords)
       print(type(input_keywords)) # str

print("&&&%%%%% hypernyms %%%%%&&& ")

# does not work anymore??

Hypernyms1 = []
listSyns = wordnet.synset(input_keywords + '.n.01')

hypo = lambda s: s.hyponyms()
hyper = lambda s: s.hypernyms()
list(listSyns.closure(hypo, depth=1)) == listSyns.hyponyms()




# print("<<<<<<<<<<<<<<<<<  synsets <<<<<<<<<<<<<<<<")

# synonyms = []
# for syn in wordnet.synsets(input_keywords):
#     for l in syn.lemmas():
#         synonyms.append(l.name())
# semanticKeywords = set(synonyms)
# print(semanticKeywords)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# ###### translate and query
# ###### call functions from other files
# ###### from QueryTest.py query()
#
# print("-------- Hyponyms = details syn and hypernyms -----")
# listSyns = wordnet.synset(input_keywords + '.n.01')
# hypo = lambda s: s.hyponyms()
# hyper = lambda s: s.hypernyms()
# list(listSyns.closure(hypo, depth=1)) == dog.hyponyms()
#
# # school, frog
# list(listSyns.closure(hyper, depth=1)) == dog.hypernyms()
# hyo = list(listSyns.closure(hypo))
# hye = list(listSyns.closure(hyper))
# print(hyo)
# print(hye)
#
# print("-------------------similarity-----------------")
# w1 = wordnet.synset(input_keywords + '.n.01')
# # print(type(w1))
# w2 = wordnet.synset('employee.n.01')
# print( w1.wup_similarity(w2))
# # print(type(w1.wup_similarity(w2)))
# # print(w1.distance(w2))
# print("---------------------")
#
#
# print("ok")

