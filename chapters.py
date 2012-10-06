#!/usr/bin/python
import glob
import os
import sys

header = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n'
header += '<meta content="http://www.w3.org/1999/xhtml; charset=utf-8" http-equiv="Content-Type"/>\n'
header += '<link href="stylesheet.css" type="text/css" rel="stylesheet"/>\n'
header += '<style type="text/css">@page { margin-bottom: 5.000000pt; margin-top: 5.000000pt; }</style>\n'
header += '</head>\n<body class="calibre">\n'

footer = '</body>\n</html>'

def pad(s):
  if len(str(s)) < 2:
    return "0" + str(s)
  return str(s)

def chaptername(i):
  return "chapter" + pad(i)

def isHeaderTag(s):
  if s.find("<html") >= 0:
    return 1
  if s.find("</html") >= 0:
    return 1
  if s.find("<?xml") >= 0:
    return 1
  if s.find("<meta") >= 0:
    return 1
  if s.find("<body") >= 0:
    return 1
  if s.find("</body") >= 0:
    return 1
  if s.find("<link") >= 0:
    return 1
  if s.find("<style") >= 0:
    return 1
  if s.find("</style") >= 0:
    return 1
  if s.find("<head") >= 0:
    return 1
  if s.find("</head") >= 0:
    return 1
  if len(s.strip()) == 0:
    return 1
  return 0
 

os.chdir(sys.argv[1])
files = sorted(glob.glob("index_*"))

chapters = []

chapter = 0
c = open(chaptername(chapter) + ".html", 'w')
c.write(header)
for filename in files: 
  f = open(filename)
  for l in f.readlines():
    if l.find("CHAPTER") != -1:
      chapters.append(chaptername(chapter))
      chapter += 1
      c.write(footer)
      c.close()
      c = open(chaptername(chapter) + ".html",'w')
      c.write(header)
    if isHeaderTag(l) == 0:
      c.write(l)
  f.close()
c.write(footer)
c.close()

chapters.append("chapter" + pad(chapter))

c_str = "content.opf"
nc_str = c_str + ".tmp"

content = open(c_str)
newcontent = open(nc_str, 'w')

b = 1
b2 = 1

for l in content.readlines():
  if l.find("index_") > 0:
    if b == 1:
      for c in chapters:
        newcontent.write('<item href="' + c + '.html" id="' + c + '" media-type="application/xhtml+xml"/>\n')
      b = 0
  elif l.find("itemref") > 0:
    if b2 == 1:
      for c in chapters:
        newcontent.write('<itemref idref="' + c + '"/>\n')
      b2 = 0
  else:
    newcontent.write(l)
content.close()
newcontent.close()    
os.rename(nc_str, c_str)
