from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
articles_upvote = [int(score.getText().split()[0])for score in soup.find_all(name="span", class_="score")]


article_links = []
article_texts = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    line = article.find_all(name="a")
    for i in line:
        link = i.get("href")
        article_links.append(link)

largest_number = max(articles_upvote)
largest_index = articles_upvote.index(largest_number)

print(article_texts[largest_index + 1])
print(article_links[largest_index])

print(article_texts)
print(article_links)
print(articles_upvote)



# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# print(soup.title)


# all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)
