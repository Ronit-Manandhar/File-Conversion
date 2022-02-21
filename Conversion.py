import pandas as pd
import csv
import json

#convert txt file to csv
account = pd.read_csv("example.txt", delimiter='\t')
account.to_csv('example.csv',index=None)

#Convert the record delimeter from tab to comma
reader = csv.reader(open("example.txt", "r"), delimiter='\t')
writer = csv.writer(open("example1.txt", 'w'), delimiter=',')
writer.writerows(reader)

#Create a JSON object array/file of the first five rows of data from csv file
def logic(index):
    if index >5:
       return True
    return False

df = pd.read_csv('example.csv', skiprows= lambda x: logic(x))
df.to_json ('example.json', orient='records')
with open('example.json', 'w') as f:
    json.dump({'Employees': df.to_dict(orient='records')}, f, indent=4)






