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


blog_landing = 'http://dmclaw.com/publications'   #Add blog landing URL here

sauce = urllib.request.urlopen(blog_landing).read()
soup = bs.BeautifulSoup(sauce,'lxml')
blog_urls = []
nav = soup.nav

variable = soup.find("div",{"class":"publications-list"}).findAll("li")  #specify what div each url on the blog landing is under.
for var in variable:
	test = var.find("a")
	blog_urls.append("http://dmclaw.com/" + test.get("href").replace("%2D","-"))  #change beginning URL 

	print(blog_urls)

# blog_urls = ['http://dmclaw.com/Publication-Susan-H-Briggs-Receives-2017-Altec-All-Star-Award',
# 'http://dmclaw.com/Publication-Narrowing-the-Scope-of-Medical-Malpractice-E-Discovery-Requests']  #manual test if necessary

with open('index.csv','a') as csv_file: #rename csv file to website name.csv
		writer = csv.writer(csv_file)
		writer.writerow(["Site", "HTML", "title", "body"]) #Write header

for url in blog_urls:
	print("working on" + url) #test to see if loop is working
	sauce2 = urllib.request.urlopen(url).read()
	soup2 = bs.BeautifulSoup(sauce2,'lxml')

	mydiv = soup2.find("div",{"class":"pub-detail"})  #specify what div the blog content is under
	title = mydiv.h1
	body = mydiv.findAll("p")

	with open('index.csv','a') as csv_file: #rename csv file to website name.csv
		writer = csv.writer(csv_file)
		writer.writerow([url,mydiv,title,body])
