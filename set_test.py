import sys
import string
sent = sys.argv[1]
sent2 = sys.argv[2]

sent = sent.lower()
sent2 = sent2.lower()

x = set(sent)
x2 = set(sent2)

x = x.intersection(string.lowercase)
x2 = x2.intersection(string.lowercase)

number = len(x)
common = len(x.intersection(x2))
difference = number - common

print "Number:", number
print "common:", common
print "difference:", difference




