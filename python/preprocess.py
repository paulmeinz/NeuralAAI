import re
import docx
import os
import string
import csv
import roget
import copy


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

# Initialize hash table

dic = copy.deepcopy(r.num_cat)
for i in dic.keys():
	dic[i] = 0

# Read the files

for i in docs:
    counts = copy.deepcopy(dic)
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
    text = text.encode('ascii')
    text = slt.split(text)
    newtext = [p for p in text if p != '']
    for k in newtext:
        l = r.word_cat(k)
        cats = []
        for m in l:
            cats.append(m[1])
            for n in cats:
            	if n != '0000':
            	    counts[n] += 1
    final = []        	    
    for o in counts.keys():
        final.append([r.num_cat[o],counts[o]])
    print(final)

          
    # mydict[i] = newtext




