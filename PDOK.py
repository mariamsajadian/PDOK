import xml.etree.ElementTree as ET
import requests
url = 'https://geodata.nationaalgeoregister.nl/ahn3/wfs?request=GetCapabilities'
AHN3 = requests.get(url)
#print(AHN3.text)
tree = ET.fromstring(AHN3.text)
# for child in tree:
#     print(child)
for c in tree.findall('{http://www.opengis.net/ows/1.1}ServiceIdentification'):
    for keyword in c.iter('{http://www.opengis.net/ows/1.1}Keyword'):
        print(keyword.text)
print('Well done!, you extracted keywords from XML :). Best, Mariam')


