import re
import docx
import os


files = os.listdir("/home/paul/Documents/Code/NeuralAAI/python/files/")

pat = re.compile(".docx")

# Grab the files with the docx extension

docs = []

for i in files:
    if pat.search(i) != None:
        docs.append(i)

# Read the files

for i in docs:
    doc = docx.Document('files/' + i)
    for j in doc.paragraphs:
        for k in j.runs:
            print k.bold, k.italic, k.underline # Determine fonts

