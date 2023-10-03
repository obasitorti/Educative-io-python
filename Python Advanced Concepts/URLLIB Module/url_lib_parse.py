# from urllib.parse import urlparse
# result = urlparse('https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa')
# print (result)

# print (result.netloc)

# print (result.geturl())

# print (result.port)  

import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'q': 'Python'})
print(data)


url = 'http://duckduckgo.com/html/'
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)
with open('results.html', 'wb') as f:
    f.write(response.read())