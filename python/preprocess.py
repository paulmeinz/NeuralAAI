import re
import docx


doc = docx.Document('031.docx')
x = len(doc.paragraphs)
print(x)
