import requests, bs4

is_new_testament = True
collection = "gospel"
book_name = "john"
chapter = 1

url_prefix = "https://vulgate.org"

if is_new_testament:
    url_suffix = f"/nt/{collection}/{book_name}_{chapter}.htm"

res = requests.get(url_prefix + url_suffix)
res.raise_for_status()
vulgate_soup = bs4.BeautifulSoup(res.text, 'html.parser')

verses = vulgate_soup.select('.Latin')
for verse in verses:
    print(verse.getText())