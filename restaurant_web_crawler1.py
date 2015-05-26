#!/usr/bin/python
import json
import urllib

def showsome(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  hits = data['results']
  print 'Top %d hits:' % len(hits)
  for h in hits: 
    print ' ', h['url']
    parse(h)

def parse(hit):
  print "hit"



showsome('best burgers in san francisco')