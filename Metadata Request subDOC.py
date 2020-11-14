# extract keywords from metadata. I think it is suitable for recommending keywords to users
# or design an advance user interface
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://api.labs.kadaster.nl/datasets/pdok/metadata/services/metadata/sparql')
# here I assumed that we have user interface.
# So, we can set search by and URI comes from the Metadata Request Group keywords.py file.
URI = "<https://www.pdok.nl/introductie/-/article/terugmeldingen-1>"
# you can search by: (keywords, about, dateIssued, name), contentRating, description, encodingFormat, identifier, inLanguage, license
# geographic phenomena are only in the (keywords, about, dateIssued, name).
SearchBy = "about"
sparql.setQuery("""
PREFIX sdo: <https://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT * WHERE { """ + URI + """sdo:""" + SearchBy + """ ?obj } """)
# you also can check sdo:about, sdo:name, and sdo:dateIssued
# return JSON
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
# print(results)

# convert dictionary to string
# where is my counter, I need to keep my objects in variables
for result in results["results"]["bindings"]:
    dictionary = result
    dic2 = dictionary["obj"]
    value = dic2['value']
    print(value)
    key_list = value.split('\n')
    # print(key_list)
    # print(type(key_list))

print("---------------------------------------------------------------------")
print("ok! now you need an excel file to replace keywords(in both excel file and metadata), URIs  in the algorithm to make more automatic ")
