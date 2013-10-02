class Rodent:
    'Added a doc string to explain what rodents does'
    def __init__(self, tag_id):
        self.tag_id = tag_id
        self.weights = []
    
    def plot(self):
        return self.tag_id[0]
    
    def add_weight(self,weight):
        self.weights.append(weight)
    
class DNASequence:
    def __init__(self,seq):
        self.seq = seq
    
    def base_count(self,base):
        return self.seq.count(base)
    
    def gc_content(self):
        return 1.0*(self.seq.count("G")+self.seq.count("C"))/len(self.seq)
    
    
