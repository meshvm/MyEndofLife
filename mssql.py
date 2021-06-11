# importing the libraries

from bs4 import BeautifulSoup
import requests
import csv

# url="https://docs.microsoft.com/en-us/sql/database-engine/install-windows/latest-updates-for-microsoft-sql-server?view=sql-server-ver15" 
url="https://github.com/MicrosoftDocs/sql-docs/blob/live/docs/database-engine/install-windows/latest-updates-for-microsoft-sql-server.md" 
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
# print(soup.prettify()) # print the parsed data of html, complete skeleton
# print(soup.title)
# print(soup.title.text) 
try: 
    able = soup.find("article", attrs={"class": "markdown-body entry-content container-lg"})
    # print(able.find_all("table"))
    head_table_data = able.find_all("table")
    # print(head_table_data[1])
    head = head_table_data[1].thead.find_all("th") # contains 1 row
    print(head)
#     #_____________________________x____________________________

        # Get all the headings of Lists
    headings = []
    for td in head:
        # remove any newlines and extra spaces from left and right
        headings.append(td.text.replace('\n', ' ').strip())

    print(headings)     
#     #_____________________________x____________________________

#     #getting data
    row_table_data = head_table_data[1].find_all("td") # contains n rows
    # print(row_table_data)
    # Get all the rows of Table
    records = []
    for td in row_table_data:
        # remove any newlines and extra spaces from left and right
        records.append(td.text.replace('\n', ' ').strip())

    print(records) 

    # data to be written row-wise in csv fil
    n = len(headings)
    # using list comprehension 
    x = [records[i:i + n] for i in range(0, len(records), n)] 
    # print(x)
        # opening the csv file in 'a+' mode i.e: append mode
    file = open('MSSQL.csv', 'a+', newline ='')
    
    # writing the data into the file
    with file:    
        write = csv.writer(file)
        write.writerows([headings],)
        write.writerows(x)
except :
    print("This product is not available on this site --> https://endoflife.date")