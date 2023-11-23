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
verses_text = [f"{verse.getText()}\n" for verse in verses]

with open(f"C:\\Users\\Blaine Freestone\\Desktop\\Vulgate Verses\\{book_name}-{chapter}.txt", 'w') as file:
    file.writelines(verses_text)