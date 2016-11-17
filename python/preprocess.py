import re
import docx


doc = docx.Document('031.docx')
x = len(doc.paragraphs)

for i in doc.paragraphs:
  for z in i.runs:
    print z.bold, z.italic, z.underline
