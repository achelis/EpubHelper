#!/usr/bin/python
import fileinput

prv_line = ""

def process(line):
  global prv_line
  l = prv_line + line
  i = l.find("</")
  if i >= 0:
    j = l[i:].find(">") + i + 1
    prv_line = l[j:].rstrip()
    return l[:j]
  elif l.find("<") >= 0 and l.find("<body") == -1:
    prv_line = l.rstrip()
    return ""
  else:
    prv_line =  ""
    return l

for line in fileinput.input():
  print process(line)
