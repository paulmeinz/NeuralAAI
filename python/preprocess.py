import re
import docx
import os
import string
import csv
import roget


files = os.listdir("/home/paul/Documents/Code/NeuralAAI/python/files/")

pat = re.compile(".doc")
slt = re.compile('''[-&$#/~`?;:<> ,}{.-;:$&!)("]|\]|\[''')
grp = re.compile("\(.*?\)|\{.*?\}|\[.*?\]")
squote = re.compile(u"\u2019|\u2018")
dquote = re.compile(u"\u201c|\u201d")
dash = re.compile(u"\u2013|\u2014")
elipse = re.compile(u"\u2026")
r = roget.Roget()

mydict = {}

# Grab the files with the docx extension

docs = []

for i in files:
    if pat.search(i) != None:
        docs.append(i)

# Read the files

for i in docs:
    text = ''
    doc = docx.Document('files/' + i)
    for j in doc.paragraphs:
        for k in j.runs:
            if k.bold == None and k.italic == None and k.underline == None:
                x = k.text
                text += x.lower()

                
    text = re.sub(squote, "'", text)
    text = re.sub(dquote, '''"''', text)
    text = re.sub(dash, "-", text)
    text = re.sub(elipse, "...", text)
    text = re.sub(grp, "", text)
    text = slt.split(text)
    newtext = [p for p in text if p != '']     
    mydict[i] = newtext

print(mydict[i])


