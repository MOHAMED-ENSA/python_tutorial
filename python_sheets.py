import random as rd 
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credential.json',scope)
client = gspread.authorize(creds)
sheets = client.open('login').sheet1
#1 print all data
#data = sheets.get_all_records()
data = sheets.get_all_values()
print(data , type(data) , len(data))
#print (data[0]["CNE"])
#2 get the specific row values
#row = sheets.row_values(1)
#print(row)
#3 get the specific cell
#cell = sheets.cell(3,3).value
#print(cell)
#4 get the specefic col 
#col = sheets.col_values(2) 
#print(col)
#5 delete a row / column
# sheets.delete_row(1)
# sheets.delete_row(1)
# sheets.delete_columns(4)
#6 insert into data 
# values = ["foad" , 1234646454 , 3 , 'FST']
# sheets.insert_row(values , index=4 )
# value1 = ["foad" , 1234555554 , 5 , 'UST']
# value2 = ["Moussa" , 12346455654 , 2 , 'FM']
# values = [value1,value2]
# sheets.insert_rows(values , row = 5 )


#7 update a cell
#sheets.update_cell(6,8,None)
#sheets.update_cell(6,2,1234645664)
# 8 : search for a value 
#a first instance
# name = sheets.find('Ali')
# print( name._row , name._col ,name.value)
#b all occuration
# names = sheets.findall('ali')
# for name in names : 
#     print(name.value , name.row , name.col)


# random modulde
#import random as rd 
# random flot between 0 and 1
#a = rd.random()
#b = rd.randint(2,5)
#c = rd.randrange(1,20,2)
#print(b)
#names = ("ali" , "mohamed" , "noura" , "kamal")
# d = rd.choice(names)
# print(d)
# choice multiple elements
# e = rd.sample(names , 2)
# print(e,type(e))
# choice multiple elements with possibily of repetetion
# f = rd.choices(names , k = 3) 
# print(f , type(f))

# inserting random rows  
# names = ["mohamed" , "ahmed" , "yassin" , "houda" , 
# "noura" , "aymen" , "alaa" , "abdo" , "fatima" , "soumaya"]
# levels = [1,2,3,4,5] 
# shcools = ["ENSAO"  , "FST" , "EST" , "FS" , "FM" , "FLSH" , "FSEJS"]

# for i in range(7,100) :
#     rowToadd = [rd.choice(names), rd.randint(1100000000,1800000000),rd.choice(levels),rd.choice(shcools)] 
#     sheets.insert_row(rowToadd,i)
