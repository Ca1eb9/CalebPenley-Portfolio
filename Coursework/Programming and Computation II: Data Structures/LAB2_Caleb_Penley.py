# LAB 2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Caleb Penley
# All functions should NOT contain any for/while loops or global variables.
# Use recursion, otherwise no credit will be given
# No helper functions allowed!

def is_power_of(base, num):
    """
        >>> is_power_of(5, 625)  # pow(5, 4) = 5 * 5 * 5 * 5 = 625
        True
        >>> is_power_of(5, 1)    # pow(5, 0) = 1
        True
        >>> is_power_of(5, 5)    # pow(5, 1) = 5
        True
        >>> is_power_of(5, 15)   # 15 is not a power of 5 (it's a multiple)
        False
        >>> is_power_of(3, 9)
        True
        >>> is_power_of(3, 8)
        False
        >>> is_power_of(3, 10)
        False
        >>> is_power_of(1, 8)
        False
        >>> is_power_of(2, 0)    # 0 is not a power of any positive base.
        False
        >>> is_power_of(4, 16)
        True
        >>> is_power_of(4, 64)
        True
        >>> is_power_of(4, 63)
        False
        >>> is_power_of(4, 65)
        False
        >>> is_power_of(4, 32)
        False
    """
    ## YOUR CODE STARTS HERE
    ## Self Exaplainatory
    if num == 1:
        return True
    elif num == 0 or base == 1:
        return False
    elif num < base:
        return False
    elif (num % base) != 0:
        return False
    else:
        return is_power_of(base, num // base) #Recurseivly divides num to check again




def flat(a_list):
    """
        >>> lst = [3, [[5, 2]], 6, [4]]
        >>> flat(lst)
        [3, 5, 2, 6, 4]
        >>> lst
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    """
    ## YOUR CODE STARTS HERE
    if a_list == []: #checks if empty list
        return a_list
    
    if isinstance(a_list[0], list): #Checks if list and recursively flattens it
        return flat(a_list[0]) + flat(a_list[1:])
    
    return a_list[:1] + flat(a_list[1:]) ##Flattens the list




def right_max(num_list):
    """
        >>> right_max([3, 7, 2, 8, 6, 4, 5])
        [8, 8, 8, 8, 6, 5, 5]
        >>> right_max([1, 2, 3, 4, 5, 6])
        [6, 6, 6, 6, 6, 6]
        >>> right_max([1, 25, 3, 48, 5, 6, 12, 14, 89, 3, 2])
        [89, 89, 89, 89, 89, 89, 89, 89, 89, 3, 2]
    """
    ## YOUR CODE STARTS HERE
    if len(num_list) == 1: ##Base Case
        return [num_list[0]]
    
    max_list = right_max(num_list[1:]) #List except first element

    max = max_list[0] #new element to check
    if num_list[0]> max: ##check for new max
        max = num_list[0]

    return [max]+ max_list





def consecutive_digits(num):
    """
        >>> consecutive_digits(2222466666678)
        True
        >>> consecutive_digits(12345684562)
        False
        >>> consecutive_digits(122)
        True
    """
    ## YOUR CODE STARTS HERE
    if num < 10: ###checks for singular digit
        
        return False

    cur = num % 10 #Extracts each digit
    
    num //= 10 #
    
    next_digit = num % 10 #

    if cur == next_digit: #Checks if consecutive
        
        return True

    return consecutive_digits(num)



def only_evens(num):
    """
        >>> only_evens(4386112)
        311
        >>> only_evens(0)
        0
        >>> only_evens(468008666642)
        0
        >>> only_evens(13847896213354889741236)
        137913359713
    """
    ## YOUR CODE STARTS HERE
    #Initialize Var
    if num == 0:
        return 0

    # Extract digit
    digit = num % 10

    # Get Result from rest of number
    result = only_evens(num // 10)

    # Checking if even
    if digit % 2 == 0:
        return result
    else:
        return result * 10 + digit # Exclude odd


def run_tests():
    import doctest

    #- Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #- Run tests per function - Uncomment the next line to run doctest by function. Replace is_power_of with the name of the function you want to test
    #doctest.run_docstring_examples(right_max, globals(), name='LAB2',verbose=True)

if __name__ == "__main__":
    #right_max([3, 7, 2, 8, 6, 4, 5])
    run_tests()