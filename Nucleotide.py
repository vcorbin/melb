import string

class InvalidBaseException(Exception):
    pass

class NucleotideSequence:
    '''Takes a sequence and operates on it
    '''
    complements = {'G': 'C',
                       'C': 'G',
                       'A': 'T',
                       'T': 'A'}
    def __init__(self, sequence):
        '''Create the sequence and a empty base count dictionary
        '''
        if set(sequence).difference(set(complements)):
            raise InvalidBaseException("Wrong sequence")
        self.sequence = sequence
        self.base_counts = {}
        
    def base_count(self, base):
        '''
            Given a base, returns the number of counts for that base.
        '''
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
    
    def gc_content(self):
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)
        
    def reverse_complement(self):
        
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
            
        return rev_c
class DNASequence(NucleotideSequence):
    pass

class RNASequence(NucleotideSequence):
    complements = {'G': 'C',
                       'C': 'G',
                       'A': 'U',
                       'U': 'A'}
