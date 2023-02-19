from bs4 import BeautifulSoup
import requests #allows you to get data from particular url

response = requests.get('https://news.ycombinator.com/newest')
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", rel="nofollow") #gets the tag with the link
text = article_tag.get_text() #gets only the text from the link
article_link=article_tag.get("href")
article_upvotes=soup.find(name="span", class_="score").getText() #without getText() it just gets the tag

print(text)
print(article_link)
print(article_upvotes)