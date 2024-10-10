def inter_unique(lst1, lst2):
    """
        >>> inter_unique([3, 5, 7, 6], [3, 3, 3, 3]) 
        []
        >>> inter_unique([3, 5, 7, 6], [-4, 0, 22, 6, 5, 3]) 
        [3, 5, 6]
        >>> inter_unique([3, 5, 7, 6], [-4, 0, 22, 6, 5, 3, 3, 3]) 
        [5, 6]
        >>> inter_unique([3, 5, 7, 6], [-14, 10, 56])              
        []
    """
    #--- YOUR CODE STARTS HERE
    new_lst =[]
    for i in lst1:
        if i in lst2 and lst1.count(i) == 1 and lst2.count(i) == 1:
            new_lst.append(i)
    return new_lst
def run_tests():
    import doctest
    # Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function
    doctest.run_docstring_examples(inter_unique, globals(), name='REC0',verbose=True)

if __name__ == "__main__":
    run_tests()