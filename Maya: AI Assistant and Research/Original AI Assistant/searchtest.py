subscription_key = "secret"
assert subscription_key
search_url = "https://api.bing.microsoft.com/v7.0/search"
search_term = ""
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term,}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()
def html_parser(req):
  html_page = urlopen(req)
  soup = BeautifulSoup(html_page, "html.parser")
  text = soup.get_text()
  print(text)
import pprint
pprint.pprint(search_results)
try:
  if search_results['computation']:
    print(search_results['computation']['value'])
except:
  try:
    if search_results['entities']:
      print('here')
      paragraph = str(search_results['entities']['value'][0]['description'])
      site=search_results['entities']['value'][0]['contractualRules'][0]['url']
      print(paragraph)
      sentence_index = paragraph.find('.')
      print(paragraph[0: sentence_index])
      sentences = paragraph.split('.')
      print(''.join(sentences[0:2]))
  except:
    #try:
      #if search_results['relatedSearches']:
        #print(search_results['relatedSearches']['value'][0])
        #response = requests.get(search_results['relatedSearches']['value'][0]['webSearchUrl'])
        #pprint.pprint(response)
        #req = Request(search_results['relatedSearches']['value'][0]['webSearchUrl'])
        #html_parser(req)
        

    # there may be more elements you don't want, such as "style", etc.]
        #sentence_index = str().find('.')
        #print (response.status_code)
        #print (response.content[0: sentence_index])
    #except:
      print(search_results['webPages']['value'][0]['url'])
      response = requests.get(search_results['webPages']['value'][0]['url'])
      pprint.pprint(response)
      req = Request(search_results['webPages']['value'][0]['url'])
      html_parser(req)

#when was this published