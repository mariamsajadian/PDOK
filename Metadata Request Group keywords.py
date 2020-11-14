# In this code, a group of keywords read as input and each keyword have an answer
# I assumed that a user enters keywords in the search bar and it is the result
# I do not know whether it is suitable for our job or not?
from SPARQLWrapper import SPARQLWrapper, JSON
# from tkinter import *
# from rdflib import Graph

sparql = SPARQLWrapper('https://api.labs.kadaster.nl/datasets/pdok/metadata/services/metadata/sparql')

# txt file contains keywords in the questions that is replaced in the SPARQL query as object
with open("KeywordsDutch.txt") as Dutch:
    Save_keywords = Dutch.read()
    # print(Save_keywords)

key_list = Save_keywords.split('\n')
# print(type(key_list))
# you can search by: (keywords, about, dateIssued, name), contentRating, description, encodingFormat, identifier, inLanguage, license
# geographic phenomena are only in the (keywords, about, dateIssued, name).
SearchBy = "keywords"

for k in key_list:

    sparql.setQuery("""
        PREFIX sdo: <https://schema.org/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT * WHERE {  ?sub sdo:""" + SearchBy + k + """. } """)
    # call JSON
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    # extract URls
    for result in results["results"]["bindings"]:
     a = result
    # print(a)
    # print(type(a))
    listOfDictionary = (a['sub'])
    # print (listOfDictionary)
    # print(type(listOfDictionary))
    URI = (listOfDictionary['value'])
    Reteive_metadata = "https://data.labs.kadaster.nl/pdok/metadata/browser?resource=" + URI
    print(k)
    # print (URI)
    print(Reteive_metadata)
print('-------------------------------------------')
print("well done! now open the answer in a browser")
print('What is the next step?')
print('I do not know?!')
