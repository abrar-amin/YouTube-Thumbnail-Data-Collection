from openpyxl import load_workbook
import os
workbook = load_workbook(filename="C:/Users/.../Youtube Trending Videos.xlsx")
sheet = workbook.active


letters = ["A","B","C","D","E","F"]

row = 3
column = 1

while(row<=253):
    for i in range(1,6):
        print(sheet[letters[i] + str(row)].value)
    row+=4
