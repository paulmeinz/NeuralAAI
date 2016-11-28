import re
import docx
import os
import string


files = os.listdir("/home/paul/Documents/Code/NeuralAAI/python/files/")

pat = re.compile(".docx")
slt = re.compile("[ ,.-;:$&!]")

# Grab the files with the docx extension

docs = []

for i in files:
    if pat.search(i) != None:
        docs.append(i)

# Read the files

for i in docs:
    text = []
    doc = docx.Document('files/' + i)
    for j in doc.paragraphs:
        for k in j.runs:
            if k.bold == None and k.italic == None and k.underline == None:
                x = k.text
                x = x.replace(u"\u2019", "").replace(u"\u2013", "").replace(u"\u2018", "")
                x = slt.split(x)
                text.extend(x)
    print(text)

