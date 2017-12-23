import urllib.request
from xml.etree.ElementTree import XML

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
response = u.read()
doc = XML(response)

for j in doc:
    print(j.text)

"""
Selects all subelements, on all levels beneath the current element. For
example, .//egg selects all egg elements in the entire tree.
"""
for i in doc.findall('.//pt'):
    print(i.text)
