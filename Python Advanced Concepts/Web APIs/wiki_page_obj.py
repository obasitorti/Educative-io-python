import wikipedia

page = wikipedia.page('Python(programming language)')
print(page)

print(page.title)

print(page.url)

print(page.content.encode('utf-8'))