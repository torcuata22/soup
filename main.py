from bs4 import BeautifulSoup
#if I need xml: import lxml (need to install module), then use 'lxml' instead of html
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser') #represents the whole html code

#soup.elementIWant, for example:
# print(soup.title) #full line where title tag is

#treat it like a pyhthon object:
# print(soup.title.name) #name of the title tag
# print(soup.title.string) #what's between the title tags (a string)
# print(soup.a) #first anchor tag it finds
# print(soup.prettify()) #prints the whole html text but "pretty" (easier to read)

#To find all of the elements of one tag: use find_all(). Examples:
# all_anchor_tags = soup.find_all(name='a') #finds all tags with name = 'a', returns a list
# print(all_anchor_tags)

#to get a hold of the text inside the anchor tags:
# for tag in all_anchor_tags:
    # print(tag.getText()) #bs4 method

#to get a hold of the links themselves:
# for tag in all_anchor_tags:
#     print(tag.get("href"))

#find things by their attribute name (tag's id, for example):
# soup.find_all() #finds everything
# soup.find(name="h1", id="name") #finds first case that matches the query, in this case, h1 tag with id="name"

# section_heading = soup.find(name="h3", class_="heading")

#Also works for CSS:
