import re
import docx
import os
import string
import csv
import roget
import copy
from stemming.porter2 import stem
import pandas as pd

#read all files in aai directory
files = os.listdir("/home/paul/Documents/Code/NeuralAAI/python/files/")

#some reg ex for reading files and parsing text in an aai
pat = re.compile(".doc")
slt = re.compile('''[-&$#/~`?;:<> ,}{.-;:$&!)("]|\]|\[''')
grp = re.compile("\(.*?\)|\{.*?\}|\[.*?\]")
squote = re.compile(u"\u2019|\u2018")
dquote = re.compile(u"\u201c|\u201d")
dash = re.compile(u"\u2013|\u2014")
elipse = re.compile(u"\u2026")
cl = re.compile("\.")

#create roget object for word classification
r = roget.Roget()

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
df = True
for i in docs:
    counts = copy.deepcopy(dic)
    text = ''
    doc = docx.Document('files/' + i)
    name = cl.split(i)[0]
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
    	z = stem(k)
        l = r.word_cat(z)
        cats = []
        for m in l:
            cats.append(m[1])
            for n in cats:
            	if n != '0000':
            	    counts[n] += 1
    final = []        	    
    for o in counts.keys():
    	if cl.search(o) == None:
            final.append([r.num_cat[o],counts[o]])
    if df:
    	fd = pd.DataFrame(final, columns = ['ID',name]).set_index('ID').T
    	df = False
    if not df:
    	final = pd.DataFrame(final, columns = ['ID',name]).set_index('ID').T
    	fd = fd.append(final)


fd.to_csv('~/Documents/testing.csv')



          




