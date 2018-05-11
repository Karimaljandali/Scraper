import bs4 as bs
import urllib.request
import csv

blog_landing = 'http://dmclaw.com/publications'

sauce = urllib.request.urlopen(blog_landing).read()
soup = bs.BeautifulSoup(sauce,'lxml')

nav = soup.nav

variable = soup.find("div",{"class":"publications-list"}).findAll("li")
for var in variable:
	test = var.find("a")
	print(test)


# blog_urls = ['http://dmclaw.com/Publication-Susan-H-Briggs-Receives-2017-Altec-All-Star-Award','http://dmclaw.com/Publication-DMC-Expands-Its-Medicare-Compliance-Team']

# for url in blog_urls:
# 	sauce2 = urllib.request.urlopen(url).read()
# 	soup2 = bs.BeautifulSoup(sauce2,'lxml')

# 	nav2 = soup2.nav

# 	mydiv = soup2.findAll("div",{"class":"pub-detail"})

# 	with open('index.csv','a') as csv_file:
# 		writer = csv.writer(csv_file)
# 		writer.writerow([mydiv])
