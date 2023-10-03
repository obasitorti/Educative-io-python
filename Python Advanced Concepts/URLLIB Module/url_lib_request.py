import urllib.request
url = urllib.request.urlopen('https://www.google.com/')
print(url.geturl())

print(url.info())

header = url.info()
print(header.as_string)

print(url.getcode())