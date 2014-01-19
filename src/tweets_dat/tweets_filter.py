import sys

file_path = sys.argv[1]
f = open(file_path, 'r')
for line in f.readlines():
    print ' '.join(line.strip().split(' ')[5:])
f.close()
