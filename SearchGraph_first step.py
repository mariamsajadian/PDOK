import rdflib
# import pprint
# import SPARQLWrapper
from rdflib import Graph
import requests

# create a Graph
g = rdflib.Graph()

# parse in an RDF file
RDF = g.parse("ahn3test-ttl.ttl", format="ttl")

# print out the entire Graph in the RDF Turtle format
# print(RDF.serialize(format="turtle").decode("utf-8")) # true

# for s, p, o in RDF: # true
# # #for keyword in o.iter(rdflib.term.URIRef('http://example.com/says')):
#   print(o) # true
# is a server?? https://api.labs.kadaster.nl/datasets/pdok/metadata/services/metadata/sparql
# Run a Query
qres = RDF.query("""SELECT ?k WHERE { ?s <https://schema.org/keywords> ?k }""")
# list = [ ]
# for row in qres:
for row in qres:
    # list = row
    print(row)
print("Not bad!")
# print(type(list))
# print(len(list))
