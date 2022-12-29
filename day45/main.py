from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text 

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.title.string)

articles= soup.find_all(name="span", class_="titleline")
# print(article_tag)
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.a.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts) 
# print(article_links)
# print(article_upvotes)

largest_numbser = max(article_upvotes)
largest_index = article_upvotes.index(largest_numbser)
print(largest_numbser)
print(largest_index)
print(article_texts[largest_index]) 
print(article_links[largest_index]) 









# -----------------------------BeautifulSoup Learning ----------------------------
# import lxml
# import os
# os.chdir("/Users/mahan/Desktop/100DaysOfCodePython-master/day45")

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify)
# # print(soup.p)
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass

# heading = soup.find(name="h1", id="name")
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# # print(company_url)

# name = soup.select_one(selector="#name")
# # print(name)

# heading = soup.select(".heading")
# print(heading)

input(">")