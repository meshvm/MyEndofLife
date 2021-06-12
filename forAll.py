# importing the libraries

from bs4 import BeautifulSoup
import requests
import csv
product = str(input("Give Name of product --->")).replace(" ", "")
url="https://endoflife.date/" + product

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
# print(soup.prettify()) # print the parsed data of html, complete skeleton
# print(soup.title)
# print(soup.title.text) 
try: 
    gdp_table = soup.find("table", attrs={"class": "lifecycle"})
    # print(gdp_table)
    #_____________________________x____________________________
    head_table_data = gdp_table.thead.find_all("th") # contains 2 rows
    # Get all the headings of Lists
    headings = []
    for td in head_table_data:
        # remove any newlines and extra spaces from left and right
        headings.append(td.text.replace('\n', ' ').strip())

    #print(headings)     
    #_____________________________x____________________________

    #getting data
    row_table_data = gdp_table.find_all("td") # contains n rows
    # print(row_table_data)
    # Get all the rows of Table
    records = []
    for td in row_table_data:
        # remove any newlines and extra spaces from left and right
        records.append(td.text.replace('\n', ' ').strip())

    # print(records) 

    # data to be written row-wise in csv fil
    n = len(headings)
    # using list comprehension 
    x = [records[i:i + n] for i in range(0, len(records), n)] 
    print(x)
    fileName = product+".csv"
    # opening the csv file in 'a+' mode i.e: append mode
    file = open(fileName, 'a+', newline ='')
    
    # writing the data into the file
    with file:    
        write = csv.writer(file)
        write.writerows([headings],)
        write.writerows(x)
except :
    print("This product is not available on this site --> https://endoflife.date")

