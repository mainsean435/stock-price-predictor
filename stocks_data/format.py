#!/usr/bin/python3

import os
import re
from datetime import datetime

def sort_by_date(line):
  date = (line.split(',')[0]).split('-')
  y, m, d = int(date[0]), int(date[1]), int(date[2])
  return datetime(y, m, d)


csv_files = [f for f in os.listdir(os.getcwd()) if f.endswith(".csv")]

for file in csv_files:
  with open(file, 'r') as fd:
    contents = fd.readlines()
    h = contents.pop(0)

  for idx, line in enumerate(contents):
    date = line.split(',')[0]
    if re.search(r'\d+/\d+/\d+', date):
      month, day, year = date.split('/')
      year = '19'+year if int(year) > 22 else '20'+year
      line = line.replace(date, f"{year}-{month}-{day}")
      
  contents.reverse()
  with open(file, 'w') as fd:
    fd.write(h)
    fd.writelines(contents)
