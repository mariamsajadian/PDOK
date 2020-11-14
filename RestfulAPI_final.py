from SPARQLWrapper import SPARQLWrapper, JSON
import os
import json

# API address
sparql = SPARQLWrapper('https://api.labs.kadaster.nl/datasets/pdok/metadata/services/metadata/sparql')
# create folder
path = "C:\\Users\\SMSaj\\OneDrive\\Desktop\\Pythoncodes\\API\\Request\\output"
# txt file contains keywords in the questions that is replaced in the SPARQL query as object
with open("KeywordExtension.txt") as Dutch:
    Save_keywords = Dutch.read()

Input_Keyword = Save_keywords

# you can search by: keywords, about, dateIssued, name
def query():
    sparql.setQuery(""" PREFIX sdo: <https://schema.org/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT "dataset" ?resource ?keyword WHERE {
          VALUES (?type ?class) {
          ("dataset" sdo:Dataset)
        ("service" sdo:WebAPI)
       }
        ?resource <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?class;
        (sdo:about|sdo:keywords|sdo:name|sdo:dateIssued) ?keyword.
         FILTER(CONTAINS(LCASE(STR(?keyword)), LCASE(STR(""" + Input_Keyword + """))))
       }
        ORDER BY ("dataset") (?resource) (?keyword) """)
query()

def output():
  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()
  print(results)

  lineList = []
  for result in results["results"]["bindings"]:
    a = result
    listOfDictionary = (a['resource'])
    URI = (listOfDictionary['value'])
    metadata = "https://data.labs.kadaster.nl/pdok/metadata/browser?resource=" + URI
    print(metadata)
    # append the lists in the loop(mutable and Immutable and initialize strings and data structure
    lineList.append(metadata)
# print the number of list
  number = (len(lineList))
  number = str(number)
  print(number)

  for i in range(1,2):
    os.chdir(path)
    newFolder = Input_Keyword + str(i)
    try:
        if not os.path.exists(newFolder):
           os.makedirs(newFolder)
           path2 = path + "\\" + newFolder
           os.chdir(path2)
        for j in range(1,1):
           subFolder = "subDocument" + str(j)
           os.makedirs(subFolder)
    except OSError:
        print('Error: Directory already exists, change the newFolder name')
# write a URI to a file
  with open("URI" + Input_Keyword + number + ".txt", "w") as w:
# for meta in lineList:
   print(lineList, file = w)
   w.write(metadata)

# write JSON in a file
  with open("JSON" + Input_Keyword + ".json", "w") as json_file:
    json.dump(results, json_file)

output()
