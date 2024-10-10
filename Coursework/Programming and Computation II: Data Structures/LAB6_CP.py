# LAB 6
# CP
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


# ========= PART 1 ================

vector_plus_one = lambda lst: [i+1 for i in lst]       #-- Replace None with your lambda function
# Adds 1 to each value in dimension
collatz_steps = lambda lst: [i*3+1 if i%2 else i//2 for i in [i for i in lst if isinstance(i,int) and i>=1]]     #-- Replace None with your lambda function
# Uses collatz formula to update numbers and remove not numeric values in list
exchange_matrix = lambda n: [[1 if j == n-1-i else 0 for j in range(n)] for i in range(n)]       #-- Replace None with your lambda function
# Creates a matrix of any size with a diagonal pattern by checking the current position in the dimension
get_nonzero = None           #-- Replace None with your lambda function

matrix_adder = lambda m1,m2: [[m1[i][n]+m2[i][n] for n in range(len(u))] for i,u in enumerate(m1)]         #-- Replace None with your lambda function
# Adds matricies by adding each individual value in each dimension

# ========= PART 2 ================

def fused_fn(fn1, fn2): #Compares two composite functions and their outputs and returns true if they are equal
    """
        >>> plus_two = lambda num: num + 2       
        >>> square_it = lambda num: num ** 2   
        >>> comb = fused_fn(plus_two, square_it) 
        >>> comb(3)      # (3 ** 2) + 2  != (3 + 2) ** 2
        False
        >>> comb(-0.5)    # ((-0.5) ** 2) + 2  == (-0.5 + 2) ** 2
        True
    """
    def compare(n): #compare functions output
        return fn2(fn1(n)) == fn1(fn2(n))
    return compare



def mulDigits(num, fn): #Finds numbers that make the given fn true and mulitplies them
    """
        >>> isTwo = lambda num: num == 2
        >>> mulDigits(5724892472, isTwo)
        8
        >>> def divByFour(num):
        ...     return not num%4
        ...
        >>> mulDigits(5724892472, divByFour)
        128
        >>> mulDigits(155794, isTwo)
        1
        >>> mulDigits(67945125482222152, isTwo)
        64
        >>> mulDigits(679451254828822152, divByFour)
        8192
    """
    match_num = 1
    while num>0:
        current_digit = num % 10 #Extract number
        num //= 10
        if fn(current_digit): #found number
            match_num*=current_digit 
    return match_num



def get_digit(k): #Get kth digit of a number
    """
        >>> get_digit(2)(3456)
        5
        >>> get_digit(2)(5678)
        7
        >>> get_digit(1)(10)
        0
        >>> get_digit(4)(789)
        -1
    """
    def kth_digit(num): #Find kth digit
        num = abs(num) #make sure num is pos
        digit=k
        while num and digit>0:
            current_digit = num% 10 #extract each digit
            num //= 10
            digit-=1 #Update current position
        if digit !=0: #num is not long enough
            return -1
        else:
            return current_digit
    return kth_digit



class Dual_Iterator: #Iterator that enables the ability to reverse the iterator while in use
    """
        >>> it = Dual_Iterator([2, 4, 6, 8, 10]) 
        >>> next(it)
        2
        >>> next(it)
        4
        >>> next(it)
        6
        >>> it.reverse()
        >>> next(it)
        4
        >>> next(it)
        2
        >>> next(it)
        10
        >>> it.reverse()
        >>> next(it)
        2
        >>> next(it)
        4
        >>> next(it)
        6
        >>> it.reverse()
        >>> next(it)
        4
        >>> next(it)
        2
        >>> next(it)
        10
        >>> next(it)
        8
        >>> next(it)
        6
        >>> it2 = Dual_Iterator([2, 4, 6, 8, 10]) 
        >>> [next(it2) for _ in range(12)]
        [2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4]
        >>> it2.reverse()
        >>> [next(it2) for _ in range(12)]
        [2, 10, 8, 6, 4, 2, 10, 8, 6, 4, 2, 10]
    """
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = -1
        self.order = 1
        self.length = len(sequence)-1

    
    def __iter__(self):  # Do not modify
        return self

    def __next__(self): #returns sequence in accordance with the current index and iterates over the sequence
        if abs(self.index) < self.length: #Making sure the index is should not restart until it is more than the length of the list
            
            if self.order > 0: #Iterate based on current order method
                self.index += 1
            else:
                self.index -= 1
        else:
            self.index = 0
        return self.sequence[self.index]

    def reverse(self):
        self.order *=-1




def frange(*args): #Allows iterating over a range with float values
    '''
        >>> list(frange(7.5))
        [0, 1, 2, 3, 4, 5, 6, 7]
        >>> seq = frange(0,7, 0.1)
        >>> type(seq)
        <class 'generator'>
        >>> list(seq)
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9]
        >>> list(seq)
        []
        >>> list(frange(0,7, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75]
        >>> list(frange(0,7.75, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5]
        >>> list(frange(0,7.75, -0.5))
        []
        >>> list(frange(7.75,0, -0.5))
        [7.75, 7.25, 6.75, 6.25, 5.75, 5.25, 4.75, 4.25, 3.75, 3.25, 2.75, 2.25, 1.75, 1.25, 0.75, 0.25]
    '''
    start, step = 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError(f'frange expected at most 3 arguments, got {len(args)}')

    # - YOUR CODE STARTS HERE
    
    
    if step > 0: #Handles incrementing range
            while round(start,2) < stop:
                yield round(start,2)
                start += step
    
    elif step < 0: #Handles decrementing range
        
            while round(start,2) > stop:
                yield round(start,2)
                start += step

def get_numbers(k): #Get numbers from 1-k if number makes function true
    """
        >>> is_even = lambda num : num%2 == 0
        >>> list(get_numbers(8)(is_even))
        [2, 4, 6, 8]
        >>> seq = get_numbers(10)(lambda x: x%2!=0)   
        >>> next(seq)
        1
        >>> next(seq)
        3
        >>> next(seq)
        5
        >>> next(seq)
        7
        >>> next(seq)
        9
        >>> next(seq)
        Traceback (most recent call last):
        ...
        StopIteration
    """
    def correct_num(fn): #Iterate through k and find any numbers that makes function true
        for num in range(1,k+1):
            if fn(num):
                yield num
    return correct_num


# ========= TESTING ASSERTIONS FOR PART 1 - DO NOT MODIFY ================

def test_vector_plus_one():
    assert vector_plus_one([1, 2, 3]) == [2, 3, 4]
    assert vector_plus_one([0, 0, 0]) == [1, 1, 1]
    assert vector_plus_one([-1, -2, -3, -4, -5]) == [0, -1, -2, -3, -4]
    assert vector_plus_one([]) == []
    print('All cases for vector_plus_one passed!')

def test_collatz_steps():
    assert collatz_steps([1, 2, 3, 4]) == [4, 1, 10, 2]
    assert collatz_steps([0, "", -2, 1.5, 2.0]) == []
    assert collatz_steps([-1, -2, -3, -4, -5]) == []
    assert collatz_steps([]) == []
    print('All cases for collatz_steps passed!')


def test_exchange_matrix():
    assert exchange_matrix(1) == [[1]]
    assert exchange_matrix(2) == [[0, 1], [1, 0]]
    assert exchange_matrix(3) == [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    print('All cases for exchange_matrix passed!')


def test_matrix_adder():
    assert matrix_adder([[3, 1], [2, 7]], [[4, 2], [5, 7]]) == [[7, 3], [7, 14]]
    assert matrix_adder([[8, 2, -6, 2], [1, 5, 2, 24.5], [34, 4, 4, 2], [5, -98, 1.5, 4]], [[1, 7, 9, 55], [9.5, 45.5, 5, -9], [1, 5, 6, 67], [8, 4, 1, 7]]) == [[9, 9, 3, 57], [10.5, 50.5, 7, 15.5], [35, 9, 10, 69], [13, -94, 2.5, 11]]
    print('All cases for matrix_adder passed!')


# ========= STARTER TESTING ================

def run_tests():
    # For Part 1
    #-- Uncomment function per function to test
    #test_vector_plus_one()
    #test_collatz_steps()
    #test_exchange_matrix()
    #test_matrix_adder()

    # For Part 2
    import doctest    
    doctest.testmod(verbose=True)
    # -- Run tests per function - Uncomment the next line to run doctest by function.
    #doctest.run_docstring_examples(get_numbers, globals(), name='LAB6',verbose=True)   

if __name__ == "__main__":
    run_tests()
