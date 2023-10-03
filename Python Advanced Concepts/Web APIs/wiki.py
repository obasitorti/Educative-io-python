# import wikipedia

# print(wikipedia.summary('Python (programming language)'))

# Creating a function to query wikipedia

import wikipedia

def print_wikipedia_results(word):
    """
    Searces for pages that match the specified word
    """
    results = wikipedia.search(word)

    for result in results:
        try:
            page = wikipedia.page(result)
        except wikipedia.DisambiguationError:
            print("DisambiguationError")
            continue
        except wikipedia.exceptions.PageError:
            print("PageError for result: " + result)
            continue

        print(page.summary.encode('utf-8'))
    
if __name__ == "__main__":
    print_wikipedia_results('wombat')