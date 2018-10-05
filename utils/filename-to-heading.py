#!/usr/bin/python3

import os

directory = os.fsencode('/home/gcharang/gitrepos/Documentation/utils/fileName-heading')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    numStars = len(filename) - 4
    path = str('fileName-heading/' + filename)
    f = open(path, 'w')
    for i in range(numStars):
        f.write('*')
    f.write('\n')
    f.write(filename[:-4])
    f.write('\n')
    for i in range(numStars):
        f.write('*')
    f.write('\n')
    f.close

