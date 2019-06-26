import re

fname =  input("enter file name")
fh = open(fname)
num = None
sum = []
output = []
x = None
y = None
total = 0
for line in fh:
    num = re.findall('[0-9]+', line)
    sum.append(num)
while [] in sum:
    sum.remove([])
for x in sum:
    for y  in x:
        output.append(y)
        total =  total + int(y)
print(total)
