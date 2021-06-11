# # Importing library
# import csv
# product=['Version', 'Released', 'Support Status', 'Release']
# # data to be written row-wise in csv fil
# a = ['10.5', '9 months ago (24 Jun 2020)', 'Ends            in 4 years (24 Jun 2025)', '10.5.8', '10.4', '1 year and 9 months ago (18 Jun 2019)', 'Ends            in 3 years (18 Jun 2024)', '10.4.17', '10.3', '2 years and 10 months ago (25 May 2018)', 'Ends            in 2 years (25 May 2023)', '10.3.27', '10.2', '3 years and 10 months ago (23 May 2017)', 'Ends            in 1 year and 2 months (23 May 2022)', '10.2.36', '10.1', '5 years ago (17 Oct 2015)', 'Ended            5 months ago (17 Oct 2020)', 'NA', '10.0', '6 years and 12 months ago (31 Mar 2014)', 'Ended            1 year and 11 months ago (31 Mar 2019)', 'NA', '5.5 (LTS)', '8 years and 11 months ago (11 Apr 2012)', 'Ended            11 months ago (11 Apr 2020)', 'NA']
# n = len(product)
# # using list comprehension 
# x = [a[i:i + n] for i in range(0, len(a), n)] 
# print(x)

# # opening the csv file in 'w+' mode
# file = open('g4g.csv', 'w+', newline ='')
  
# # writing the data into the file
# with file:    
#     write = csv.writer(file)
#     write.writerows([product],)
#     write.writerows(x)





# importing the libraries
from bs4 import BeautifulSoup
import requests

url="https://docs.microsoft.com/en-us/lifecycle/products/" + str(input("Give Name of product --->")).replace(" ", "")

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
print(soup.prettify()) # print the parsed data of html, complete skeleton
# print(soup.title)
# print(soup.title.text) 





