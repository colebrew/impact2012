import subprocess
import re

child = subprocess.Popen('pdf2txt.py Syllabus3.pdf>output.txt', shell=True)
raw = open('output.txt')
lines = []
for line in raw:
    if ("" == line.strip()) or (re.search(re.compile('(?<=exam)'), line) == None):
        continue
    lines.append(line.strip())
    print line,

raw.close()
