#! python3

# printfile.py

def print_file1(fname):
    f = open(fname, 'r')
    for line in f:
        print(line, end = '')
        #print(line)
    f.close()

def print_file2(fname):
    f = open(fname, 'r')
    print(f.read())
    f.close()

def is_gif(fname):
    f = open(fname, 'br')
    first4 = tuple(f.read(4))
    return first4 == (0x47, 0x49, 0x46, 0x38)
