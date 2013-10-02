import sys

input = int(sys.argv[1])

if input<50 and input>0:
    print "Minor"
elif input>=50 and input<1000:
    print "Major"
else:
    print "Severe"

    
