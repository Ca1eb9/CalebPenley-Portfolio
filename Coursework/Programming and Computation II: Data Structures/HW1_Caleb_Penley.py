# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
## Caleb Penley ##

def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    lst1 = []
    while num >= 1: ###main loop iterating through sequence
        lst1.append(num)
        if num != 1:
            if (num%2)== 0: #####is even
                num //= 2
            else:
                num = 3*num+1
        else:
            num = num-1 #stop loop as we know we have reached one
    return lst1 #output sequence


def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    #- YOUR CODE STARTS HERE
    dec_num = 0
    mult_num = 1
    while oct_num: ###main loop
        #get last digit
        digit = oct_num%10
        oct_num //= 10

        #conversion to decimal and addition to number
        dec_num += digit * mult_num
        mult_num *= 8
    return dec_num ###return decimal number




def has_hoagie(num):
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
    """
    #- YOUR CODE STARTS HERE
    if num < 0: ###abs value if neg
        num *= -1

    while num >= 100:
        dig = num % 10 ## gets last digit
        hoagie_test = (num // 100) % 10###the "hoagie digit"

        if dig == hoagie_test: ###checks whether there is in fact a hoagie present
            return True
        
        num //= 10
    return False


def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    #- YOUR CODE STARTS HERE
    pre_num = num_1 % 10 ###init prev number to check
    mult_num = 10 ###power for wwhich we need to multiply by
    output = 0

    while num_1: ### deletes identical occurances of numbers in number 1
        digit = num_1%10

        #check for duplicates
        if digit != pre_num:
            output += digit * mult_num
            #increase power and continue iterating through number
            mult_num += 10
            pre_num = digit
        num_1 //= 10
    num_1 = output #for simplicity sake, keep num_1 as final number 1

    pre_num = num_2 % 10 ###init prev number to check
    mult_num = 10 ###power for wwhich we need to multiply by
    output = 0

    while num_2: ### deletes identical occurances of numbers in number 2
        digit = num_2%10

        #check for duplicates
        if digit != pre_num:
            output += digit * mult_num
            #increase power and continue iterating through number
            mult_num += 10
            pre_num = digit
        num_2 //= 10
    num_2 = output #for simplicity sake, keep num_2 as final number 2


    ###check if numbers are equal
    if num_1 == num_2:
        return True
    else:
        return False


def frequency(txt):
    '''
        Hidden tests for frequency
Testing frequency with the following input:

>>> frequency('A small mass of tissue located ABOVE the tongue')
{'a': 5, 's': 5, 'm': 2, 'l': 3, 'o': 4, 'f': 1, 't': 4, 'i': 1, 'u': 2, 'e': 5, 'c': 1, 'd': 1, 'b': 1, 'v': 1, 'h': 1, 'n': 1, 'g': 1}


>>> frequency('Y = 8Z^2+2Z+6')
{'y': 1, 'z': 2}


>>> frequency('Euouae$#Euouae')
{'e': 4, 'u': 4, 'o': 2, 'a': 2}


>>> frequency('- CMPSC132 Summer 2023, Penn State University -')
{'c': 2, 'm': 3, 'p': 2, 's': 4, 'u': 2, 'e': 4, 'r': 2, 'n': 3, 't': 3, 'a': 1, 'i': 2, 'v': 1, 'y': 1}

>>> frequency('aaaaa; [aa] ~ bcc (ab)')
{'a': 8, 'b': 2, 'c': 2}

>>> frequency('A nuT for A jar of tuna!')
{'a': 4, 'n': 2, 'u': 2, 't': 2, 'f': 2, 'o': 2, 'r': 2, 'j': 1}


>>> frequency('Sit on a potato pan, Otis')
{'s': 2, 'i': 2, 't': 4, 'o': 4, 'n': 2, 'a': 3, 'p': 2}

    '''
    # - YOUR CODE STARTS HERE -
    output_dict = {}

    #convert txt to lowercase
    txt =str.lower(txt)

    for i in txt: #### gets all freq of all letters in text
        if i.isalpha():
            output_dict[i] = output_dict.get(i, 0) + 1

    return output_dict



def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    # - YOUR CODE STARTS HERE -
    
    output_dict = {}
    occured = []
    dupli = []

    for key, i in d.items(): # removes duplicates in each key and inverts values and keys
        if i not in occured:    ###checks for duplication within values
            output_dict[i] = key
            occured.append(i)
        
        
        elif i not in dupli:  ###checks for compounded duplication and deletes technically key
            dupli.append(i)
            output_dict.pop(i)
    
    return output_dict




def employee_update(d, bonus, year):
    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """
    # - YOUR CODE STARTS HERE -
    d[year] = {}

    
    for year_indict in d.keys(): #####iterate through each value in dict and add bonus as intended
        if year_indict == year - 1:
            
            for worker, details in d[year_indict].items():
                new_salary = details[2] + bonus
                #add new salaries to dict
                d[year][worker] = [details[0], details[1], new_salary]

    return d



def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    #- YOUR CODE STARTS HERE
    for keys in d:  
        if keys == key: ###check for existing key in dict
            if not isinstance(d[keys],list): #Checks if list already in dictionary
                d[keys] = [d[keys]]
            d[keys] +=  [value]

    if key not in d:#### adds new key and value if there is no existing pair present
        d[key] = value


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    #- YOUR CODE STARTS HERE
    
    output_dict = {}
    
    for emp_id, details in d.items(): ####iterate through dict
        department = details.get('department')
        inf = {'emp_id': emp_id, 'name': details.get('name'), 'position': details.get('position')} #convert details to new structureed dict
        
        if department not in output_dict: #### solves issue incase departments not being included
                output_dict[department] = []
        output_dict[department].append(inf)
    
    return output_dict


def successors(file_name):#Creates a dictionary with prev word:succesor word
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
    """
    with open(file_name, 'r') as f: 
        contents = f.read()  # You might change .read() for .readlines() if it suits your implementation better 
    #- YOUR CODE STARTS HERE
        
    
    ##Init
    previous = '.'
    final_lst = []
    output_dict = {}
    temp = ''
    
    for i in (contents+'+'): #create a list with words and non alphanum characters
        if i == '+':
            if temp != '':
                final_lst.append(temp)
        elif i.isalnum():
            temp+=i
        elif i != ' ' and i != '\n':
            if temp != '':
                final_lst.append(temp)
            temp=''
            final_lst.append(i)
        elif temp != '':
            final_lst.append(temp)
            temp=''
        
    
    for i in (final_lst): ####adds succesors to their respective predecessors
        if previous in output_dict: #Add to previous list
            if i not in output_dict[previous]:
                output_dict[previous] += [i]
        else: #new previous
            output_dict[previous] = [i]
        previous = i #Prev = current

    return output_dict




def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE
    cur_dict = trie ###creates current dict
    
    for i in word: ####iterate through word and add it to trie
        if i not in cur_dict: 
            
            cur_dict[i] = {}
        
        cur_dict = cur_dict[i] ####concatenate possible word to dict
    
    cur_dict["word"] = True

    return None



def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    with open(file_name, 'r') as f: 
        contents = f.read()  # You might change .read() for .readlines() if it suits your implementation better 
    #- YOUR CODE STARTS HERE
    
    
    
    output_dict = {}
    words = contents.split()

    for i in words:#####adds the new words to the trie
        addToTrie(output_dict, i.lower())
    
    return output_dict


def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE
    cur = trie


    for i in word: 
        
        if i not in cur: ###checks for letter in trie to detect word
            return False
        
        cur = cur[i]
    return 'word' in cur











def run_tests():
    import doctest
    # Run start tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    #doctest.run_docstring_examples(wordExists, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    
    run_tests()