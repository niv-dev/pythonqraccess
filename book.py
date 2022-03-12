import urllib.request
import json
import textwrap

while True:

    base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    print("Welcome to Nivyan's Book Lookup for Library Database")
    user_input = input("\nEnter ISBN: ").strip()

    with urllib.request.urlopen(base_api_link + user_input) as f:
        text = f.read()

    decoded_text = text.decode("utf-8")
    obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
    volume_info = obj["items"][0] 
    authors = obj["items"][0]["volumeInfo"]["authors"]

    # displays title, summary, author, domain, page count and language
    print("\n***")  
    print("\nTitle:", volume_info["volumeInfo"]["title"])
    print("\nDate: ", volume_info["volumeInfo"]["publishedDate"])
    print("\nSummary: ")
    print(textwrap.fill(volume_info["searchInfo"]["textSnippet"], width=65))
    print("\nAuthor(s):", ",".join(authors))
    print("\nPublic Domain:", volume_info["accessInfo"]["publicDomain"])
    print("\nPage count:", volume_info["volumeInfo"]["pageCount"])
    print("\nLanguage:", volume_info["volumeInfo"]["language"])
    print("\nPublisher: ", volume_info["volumeInfo"]["publisher"])
    print("\n***")

    status_update = input("\nEnter another ISBN? y or n: ").lower().strip()

    if status_update == "n":
        print("\nThank you! Have a nice day.")
        break
