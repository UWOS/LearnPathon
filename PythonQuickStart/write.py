#! python3

# write.py

import os

def make_story1():
    f = open('story.txt', 'w')
    f.write('Mary had a little lamb,\n')
    f.write('and then she had some more.\n')

def make_story2():
    if os.path.isfile('story.txt.'):
        print('story.txt already exists')
    else:
        f = open('story.txt', 'w')
        f.write('Mary had a little lamb,\n')
        f.write('and then she had some more.\n')

def add_to_story(line, fname = 'story.txt'):
    f = open(fname, 'a')
    f.write(line)

def insert_title(title, fname = 'story.txt'):
    f = open(fname, 'r+')
    temp = f.read()
    temp = title + '\n\n' + temp
    f.seek(0)
    f.write(temp)
