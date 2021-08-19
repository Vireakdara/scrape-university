from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.4icu.org/kh/")
web_page = response.text
# print(web_page)

soup = BeautifulSoup(web_page, "html.parser")
all_title = [uni.getText() for uni in soup.select("tbody tr a")]
print(all_title)

with open("university.txt", mode="w") as file:
    i = 0
    for university in all_title:
        i += 1
        file.write(f"{i}.{university}\n")