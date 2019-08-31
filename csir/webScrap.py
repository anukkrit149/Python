import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_pharmaceutical_manufacturers_in_the_United_Kingdom'


response = requests.get(url)


soup = BS(response.text, "html.parser")

div = soup.find('div', {"class": "mw-parser-output"})

links = soup.find_all("li")




# Facultylinks = []
#
# possible_links = soup.find_all('a', {"class": "faculty-item"})
# for link in possible_links:
#     if link.has_attr('href'):
#         Facultylinks.append(link.attrs['href'])
#
# FacultyDetails = []
#
# for url in Facultylinks:
#     # print(requests.get("https://www.suffolk.edu"+url))
#     ht = BS(requests.get("https://www.suffolk.edu"+url).text, "html.parser")
#     time.sleep(2)
#     name = ht.find("h1", {"class": "title"}).text
#     post = ht.find("p", {"class": "sub-title"})
#     facultyBox = ht.find("div", {"class": "faculty-box"})
#     phone = facultyBox.find("li").text
#     email = facultyBox.find("a").text
#     if post is None:
#         post = "Unavailable"
#     else:
#         post = post.text
#     FacultyDetails.append({"Name": name, "Designation": post, "Phone Number": phone, "Email": email, "URL":
#         "https://www.suffolk.edu"+url})
#
#
# df = pd.DataFrame(FacultyDetails)
# col = ['Name','Designation','Phone Number','Email','URL']
# df = df.reindex(columns=col)
# file = pd.ExcelWriter('suffolkData.xls')
# df.to_excel(file, 'CAS')
# file.save()
#
# Facultylinks.count()