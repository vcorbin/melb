import sys

input = sys.argv[1]

F = open(input,"r")
count = 0

for line in F:
    if (line[0]==">") and ("OS=Homo sapiens" in line):
        count += 1

F.close()

print "Number of human proteins inside SwissProt:", count
