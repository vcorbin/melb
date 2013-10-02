#Testing
#Change number 2
#Change number 3

class DNASequence:
    'Doc string here'
    def __init__(self,seq):
        self.seq = seq
    
    def base_count(self,base):
        return self.seq.count(base)
    
    def gc_content(self):
        return 1.0*(self.seq.count("G")+self.seq.count("C"))/len(self.seq)
        
    def reverse(self):
        rev = ""
        rs = self.seq[::-1]
        for el in rs:
            if el == "G": rev+="C"
            elif el == "C": rev+="G"
            elif el == "A": rev+="T"
            elif el == "T": rev+="A"
        print rev
