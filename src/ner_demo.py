from twitter_nlp.bio_parser import *
import codecs
import json

input_tagged_path = './tagged_text1.txt'
f = open(input_tagged_path, 'r')

for line in f.readlines():
    print line.strip()
    print bio_parse(line.strip())
    print

f.close()
