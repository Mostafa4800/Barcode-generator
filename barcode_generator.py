#this barcode generator is made to learn python 
#the barcode generator will be used to generate barcodes from an csv file

import csv
import os

from barcode import Code128
from barcode.writer import ImageWriter

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

#csv file path/name 
csv_file = filedialog.askopenfilename(title="Open a CSV File using a semicolumn as delimiter", filetypes=[("CSV Files", "*.csv")])

#name of the rows
#ID
id = input("Enter the name of the ID row: ")
#Name
name1 = input("Enter the name of the Name row: ")
#foldername
foldername = input("Enter the name of the folder where the barcodes will be saved: ")

os.mkdir(os.path.join(os.path.dirname(csv_file), foldername))
currentDir = os.path.join(os.path.dirname(csv_file), foldername)
print(currentDir)

with open(csv_file, newline='') as file:
    csvFile = csv.DictReader(file, delimiter=';') 
    for row in csvFile:
        #generate barcode in the code128 format
        number = row[id]
        name = row[name1]
        barcodeNr = Code128(number, writer=ImageWriter())
        barcodeNr.save(os.path.join(currentDir, name))

        
        







