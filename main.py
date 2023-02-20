from bs4 import BeautifulSoup
import requests #allows you to get data from particular url

response = requests.get('https://news.ycombinator.com/newest')
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", rel="nofollow") #gets the tag with the link
text = article_tag.get_text() #gets only the text from the link
article_link=article_tag.get("href")
article_upvotes=soup.find(name="span", class_="score").getText() #without getText() it just gets the tag

# print(text)
# print(article_link)
# print(article_upvotes)

#To get all results: change find for find_all():
articles = soup.find_all(name="a", rel="nofollow")

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.get("href")
    article_links.append(article_link)


# article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
#to get only point numbers, we can split the string by the space and grab the first item:
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

#Sort from highest upvotes to lowest:
