import requests

book = "https://www.gutenberg.org/files/1112/1112.txt"

response = requests.get(book)
handle = open("files/section-13/romeo-book.txt", "wb")

if response.status_code == 200:
    for chunk in response.iter_content(100_000): # 100_000 bytes
        handle.write(chunk)
else:
    print("error", response.status_code)

handle.close()