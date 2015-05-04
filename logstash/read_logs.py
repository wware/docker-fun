import json
import pprint
import urllib2

x = urllib2.urlopen("http://localhost:9200/_search?pretty").read()
x = json.loads(x)

# check if successful, otherwise...

x = x["hits"]["hits"]

def fixer(piece):
    z = piece["_source"]["message"]
    piece["_source"]["message"] = json.loads(z)
    return piece

x = map(fixer, x)

def timesort(piece1, piece2):
    def timefind(piece):
        return piece["_source"]["message"]["@timestamp"]
    return cmp(timefind(piece1), timefind(piece2))

x.sort(timesort)

pprint.pprint([y["_source"] for y in x])
