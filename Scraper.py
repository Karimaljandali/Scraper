########################################
#        Made by Karim Aljandali       #
#              05-11-18                #
########################################

#Directions:  Install the newest version of python.  Then pip install beautifulsoup4 and pip install lxml

import bs4 as bs
import urllib.request
import csv
import contextlib
import os

with contextlib.suppress(FileNotFoundError): #Delete index.csv if it exists already, don't want duplicate data if we have to run again.
    os.remove("index.csv")


blog_landing = 'http://defensecounsel.com/news/press-releases/'   #Add blog landing URL here

sauce = urllib.request.urlopen(blog_landing).read()
soup = bs.BeautifulSoup(sauce)
blog_urls = []
nav = soup.nav

variable = soup.find("div",{"class":"column-right"}).findAll("h3",{"class":"ccm-page-list-title"})  #specify what div each url on the blog landing is under.
for var in variable:
	test = var.find("a").get("href")
	url = 'http://defensecounsel.com/news/press-releases/' + test #Convert relative link to absolute
	blog_urls.append(url)  #Add each link to blog to list.
	print(blog_urls)

	##################################################
	#    Middle section of code. Top grabs links     #
	#    from the landing page, the bottom grabs     #
	#    content from the actual page itself.        #
	##################################################

# blog_urls = ['https://www.paperstreet.com/blog/law-firm-content-inspiration-best-law-firm-content-of-2018/']  #manual test if necessary

with open('index.csv','w', newline='', encoding="utf-8") as csv_file: #rename csv file to website name.csv
		writer = csv.writer(csv_file)
		writer.writerow(["Site", "Raw HTML", "Title", "Body"]) #Write header

for url in blog_urls:
	print("working on " + url) #test to see if loop is working
	sauce2 = urllib.request.urlopen(url).read()
	soup2 = bs.BeautifulSoup(sauce2)

	mydiv = soup2.find("div",{"class":"column-right"})  #specify what div the blog content is under
	try:
		title = mydiv.h1.text
	except AttributeError:
		title = "There was no H1 on this page!"
	body = mydiv.findAll("p")
	with open('index.csv','a', newline='', encoding="utf-8") as csv_file: #rename csv file to website name.csv
		writer = csv.writer(csv_file)
		writer.writerow([url, mydiv, title, body])
