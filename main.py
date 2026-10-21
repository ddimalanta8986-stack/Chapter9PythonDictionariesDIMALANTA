counts = dict()
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
print(counts)