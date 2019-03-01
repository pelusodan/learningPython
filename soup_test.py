html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
import requests
from bs4 import BeautifulSoup

#attempting to extract the HTML using the request module
import urllib.request, re
response = urllib.request.urlopen('https://danpeluso.wordpress.com/')
html = response.read()
#trying again with high school website for number of times town is said
# google says this is 15

response2 = urllib.request.urlopen('https://www.yourhtmlsource.com/')
html2 = response2.read()
#code from beutiful soup
soup = BeautifulSoup(html, 'html.parser')
print(soup.title())
for link in soup.find_all('a'):
    print(link.get('href'))
#print(soup.get_text())

soup2 = BeautifulSoup(html2, 'html.parser')
numsims = soup2.get_text().lower().count('html')


#function for finding number of instances of one word (why not lol)
# string -> number
def dans(txt):
    for i in range(len(txt)):
        if (txt[i] == ('P'or'p'))and(txt[i+1] == ('r'))and(txt[i+2] == 'o'):
            return (1 + dans(txt[i+3:]))
        continue
    return 0
# using this function to print the number of times my name
# appears in my personal website
print('pro was found in this page ' + str(dans(soup.get_text()))+' times !!')

print(soup.get_text().count("pro"))
#using the stupid regex from noah
print(len([m.start() for m in re.finditer('pro', soup.get_text())]))
#using froffmans solution
print(soup.get_text().lower().count('pro'))
#printing number of simsbury on the high school page
print(numsims)


#result of this is all the HTML from the python website being interpreted and
# received from beautiful soup and urllib

