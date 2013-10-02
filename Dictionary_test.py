import sys

seq = sys.argv[1]

counts = {"G":seq.count("G"),"A":seq.count("A"),"T":seq.count("T"),"C":seq.count("C"),"U":seq.count("U")}

GC = 1.0*(counts["G"]+counts["C"])/(counts["G"] + counts["A"] + counts["T"] + counts["C"] + counts["U"])
if counts["U"]!=0:
    del counts["T"] 
else:
    del counts["U"]
print counts
print "GC content:", GC

