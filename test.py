import subprocess

child = subprocess.Popen('pdf2txt.py Syllabus3.pdf > output.txt', shell=True)
raw = open('output.txt')
lines = []
for line in raw:
    if "" == line.strip() || re.search(:
        continue
    lines.append(line.strip())
    print line,


raw.close()
