#!/usr/bin/env python
# coding: utf-8



import requests as req
from bs4 import *
import ssl
import csv
import pandas as pd


#ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.host_name = False
ctx.verfy_mode = ssl.CERT_NONE



r1 = req.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films#Highest-grossing_films")

soup = BeautifulSoup(r1.text,'html.parser')



# l=soup.select('title')

def init_csv(header):
    ''' will make 1 csv with given Header list'''

    #will work if Movie title is removed
    with open('movies.csv', 'w') as writeFile:
        writeFile.write(",".join(header))
        writeFile.write('\n')
    writeFile.close()

def append_row_csv(csv_row,f):
    ''' Append the given row in existing csv file'''

    #will work if Movie title is removed
    
        f.write(','.join(csv_row))
        f.write('\n')





count = 0


lines = ['Rank','Peak','Worldwide gross','Year','Reference','Title']
init_csv(lines)



rows_list = []   
for table in soup.find_all("tbody"):
    row = table.find_all('tr')
    for r in row:
        col = r.find_all("td")
        movie_name = r.find_all("th")
        #print(movie_name)
        movie_name = r.find_all("i")
        
        csv_row = []
        
        
        if(len(movie_name)) >=1:
            #print(movie_name[0].getText())
            movie_title = movie_name[0].getText()
        for i in col:
            data = i.getText().strip()
            print(data,end = ',')
            csv_row.append(data)
            
            
        if(len(movie_name)) >=1:
            m = movie_title.replace(':',"")
            #csv_row.append(m)
            '''TODO REMOVE NEXT LINE AFER TITLE FIX'''
            csv_row.append("ABC")
            print(m , end = "")
            rows_list.append(csv_row)
            
            #remove ':' from strings it is invalin in csv (clean string)
            #Avengers: Endgame -->  Avengers Endgame

            with open("movies.csv",'a') as f:
                append_row_csv(csv_row)
            

        
        print()
        #print(rows_list)
        count +=1
        
    if count > 50:
        f.close()
        break
df=pd.DataFrame(rows_list,columns=lines)
print(df)
# writer = pd.ExcelWriter('movie1.xlsx')
# df.to_excel(writer)
# writer.save()

"""FORMAT THE MOVIE TITLE """
        




