def readDataFile():
    x = []
    alllines = ''
    filename = 'data.txt'
    with open(filename, 'r') as f:
        for line in f:
            if(line.startswith('>')):
                
                x.append(alllines)
                alllines = ''
                line = ''
            line = line.strip()
            alllines = line + alllines
        x.append(alllines)   
                
            
            
    return x


allchars = []
count = 0
totals = []
atotal = []
ctotal = []
gtotal = []
ttotal = []
consenus = []
x = readDataFile()
print('test')
for data in x:
    chars = []
    for c in data:
        c = c.strip()
        chars.append(c)
    allchars.append(chars)
    length = len(chars)
    
for x in range(length):
    totals.append(0)
    atotal.append(0)
    ctotal.append(0)
    gtotal.append(0)
    ttotal.append(0)
    consenus.append('')

for data in allchars:
    count = 0
    acount = 0
    for c in data:
        
        if c == 'A':
            a = atotal[count]
            atotal[count] = a + 1
        if c == 'G':
            g = gtotal[count]
            gtotal[count] = g + 1
        if c == 'C':
            c = ctotal[count]
            ctotal[count] = c + 1
        if c == 'T':
            t = ttotal[count]
            ttotal[count] = t + 1
        
        count = count + 1
    
for x in range(length):
    maxvalue = 0
    if atotal[x] > maxvalue:
        maxvalue = atotal[x]
        consenus[x] = 'A'
    if gtotal[x] > maxvalue:
        maxvalue = gtotal[x]
        consenus[x] = 'G'
    if ctotal[x] > maxvalue:
        maxvalue = ctotal[x]
        consenus[x] = 'C'
    if ttotal[x] > maxvalue:
        maxvalue = ttotal[x]
        consenus[x] = 'T'
print(len(consenus))
print(length)
print(len(atotal))

with open('testing.txt', 'w') as f:        
    for item in consenus:
        f.write(item)
    f.write('\nA:')
    for x in range(length):
        f.write(' '+str(atotal[x]))
    f.write('\nC:')
    for x in range(length):
        f.write(' ' + str(ctotal[x]))
    f.write('\nG:')
    for x in range(length):
        f.write(' ' + str(gtotal[x]))
    f.write('\nT:')
    for x in range(length):
        f.write(' ' +str(ttotal[x]))

      
