import doctest

def factorial(integ):
    ''' 
        Takes an integer and Returns the factorial of integ
        
        >>> factorial(-3)
        1
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(4)
        24
    '''
    if type(integ) != int:
        raise Exception("Must be an integer")
    if integ<=1:
        return 1
    fact = 1
    for el in range(2,integ+1):
        fact *= el
    return fact
    
if __name__ == "__main__":    
    doctest.testmod()

def fibonacci(n):
    '''
        Return the Nth value in the Fibonacci sequence
        
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(5)
        5
    '''
    fib1,fib2 = 0,1
    for i in range(1,n):
        fib1,fib2 = fib2,fib1+fib2
    return fib2

def base_count(sequence, base):
    return sequence.count(base)

def gc_content(sequence):
    return 1.0*(sequence.count("G")+sequence.count("C"))/len(sequence)


#print base_count("GATCTAGTGATGCAC","G")
#print gc_content("GATCTAGTGATGCAC")
#print fibonacci(100)
#print factorial(0)
