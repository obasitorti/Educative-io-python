import re

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:
    regex = re.compile(string)
    match = re.search(regex, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))

# The primary reason we use compile is to save the 
# string to be reused later in our code. However, compile
# also takes some flags that can be used to enable various
# special features