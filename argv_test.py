import sys

try: 
    L = sys.argv[1:]
    L.sort()
    L[-1] = "and " + L[-1] + "."
    output = ", ".join(L)
    print(output.capitalize())
except IndexError: 
    print "No valid input"
    


