# HW3
#Caleb Penley
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self): #Detectst if empty
        # YOUR CODE STARTS HERE
        if self.top:
            return False
        else:
            return True

    def __len__(self): #count stack length
        # YOUR CODE STARTS HERE
        
        if self.top is None:
            return 0
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count


    def push(self,value): #Send value to top of stack
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        if self.top is not None:
            new_node.next = self.top
        self.top = new_node

     
    def pop(self): #Get top while popping
        # YOUR CODE STARTS HERE
        
        if self.top is not None:
            out = self.top
            self.top = self.top.next
            return out.value
        else:
            return None
        

    def peek(self): #See top without popping
        # YOUR CODE STARTS HERE
        if self.top is not None:
            return self.top.value
        else:
            return None


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt): #Detects float
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try: #Force trys to convert to float
            float(txt)
            return True
        except:
            return False


    def _priority(self,op): ##Helper Function for __getPostfix to test priority of operator
        if op in '+-':
            return 1
        elif op in '*/':
            return 2
        elif op in '^':
            return 3
        else:
            return 0

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + [ 1 + 4 ]')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        postfix_output = ''
        prev_char = ''
        balance = 0
        txt = txt.split()
        for i in range(len(txt)):#Iterates over all items in expression to convert to post_fix
            item = txt[i]
            if item.isalpha() or self._isNumber(item): # Checks if a number and adds it to post_fix
                postfix_output += str(float(item)) + ' '
                if i > 0 and self._isNumber(prev_char):
                    return None  # Missing operators
                    
            elif item in '([{': #Handles bracket work, including bracket balancing
                if item == '(':
                    balance += 1
                elif item == '{':
                    balance += 2
                elif item == '[':
                    balance += 3
                if i + 1 < len(txt) and txt[i + 1] in {')', ']', '}'}:
                    return None #missing operands
                    
                if i + 1 >= len(txt):
                    return None #Bracket at end if expr
                    
                if i > 0 and (self._isNumber(txt[i - 1]) or txt[i - 1] in ')]}'): #
                    while (not postfixStack.isEmpty() and self._priority('*') <= self._priority(postfixStack.peek())):
                        postfix_output += postfixStack.pop() + ' '
                    postfixStack.push('*')
                    

                postfixStack.push(item)
            elif item in '}])':
                if item == ')':
                    balance -= 1
                elif item == '}':
                    balance -= 2
                elif item == ']':
                    balance -= 3
                while not postfixStack.isEmpty() and postfixStack.peek() not in '({[':
                    postfix_output += postfixStack.pop() + ' '
                opening_bracket = postfixStack.peek()
                if (item == ')' and opening_bracket != '(') or (item == '}' and opening_bracket != '{') or (item == ']' and opening_bracket != '['):
                    return None  #Mismatched closing bracket
                postfixStack.pop()  # not adding bracket to output
                if i == 0:
                    return None  #Handle implicit multiplication after closing bracket
                    
                    
            elif self._priority(item) == 0:
                return None
                
                
            else:
                if i == 0 or i == len(txt) - 1 or self._priority(prev_char) != 0:
                    return None  # Consecutive operators
                    
                while (not postfixStack.isEmpty()) and (self._priority(item) < self._priority(postfixStack.peek()) or (self._priority(item) == self._priority(postfixStack.peek()) and item != '^')):
                    postfix_output += postfixStack.pop() + ' '
                postfixStack.push(item)
            prev_char = item
        
        if balance != 0: ##Bracket Balancing
            return None
            
        while not postfixStack.isEmpty(): #Sends stack to postfix text
            postfix_output += postfixStack.pop() + ' '
        return postfix_output.strip()







    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * { 5 - 3 ^ 2 } + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * [ 4 ] ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        post_fix = self._getPostfix(self.getExpr)
        if post_fix == None:
            return None
        post_fix = post_fix.split()
        for i in range(len(post_fix)): #Iterates through post_fix expr, adding to stack and calculating as ops show up and removing as shown
            current = post_fix[i]
            if not self._isNumber(current): #if op then calculate
                second = calcStack.pop() #get most recent num
                first = calcStack.pop() #get first num
                #Calculate using the nums
                if current == '+':
                    calcStack.push(first + second)
                elif current == '-':
                    calcStack.push(first - second)
                elif current == '*':
                    calcStack.push(first * second)
                elif current == '/':
                    calcStack.push(first / second)
                elif current == '^':
                    calcStack.push(first ** second)
            else:
                #Send number to stack
                calcStack.push(float(current))
        out = ''
        while not calcStack.isEmpty(): #sends stack to output
            out = calcStack.pop()
        return float(out)



#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions()
        {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):#Checks if variable
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        for i in word: #making sure there are no non alphanumeric in var
            if not i.isalpha():
                try:
                    int(i)
                except:
                    return False
        if word[0].isalpha(): #Checks for 1st letter for sur being a letter to make it a var
            return True
        else:
            return False
       

    def _replaceVariables(self, expr): ##Replace var in expression with var stored in states
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        for var, value in self.states.items(): ##replaces each var in expr if that var is in states
            expr = expr.replace(var, str(value))
        for i in expr: #returns none if there is still a var not defined
            if self._isVariable(i):
                return None
        return expr

    
    def calculateExpressions(self): #Calculates the expression of advanced calc
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        out_d = {}
        expr = self.expressions.split(';') #gets each expression
        for i in expr:
            ####gets variables and equations from expressions
            if 'return' in i:
                i = i.replace('return', '')
                i = i.strip()
                var,equa = '_return_', i
            else:
                var, equa= i.split('=')
                var, equa = var.strip(), equa.strip()
            
            equa = self._replaceVariables(equa) #replace var
            if equa is None:
                self.states = {}
                return None
            calcObj.setExpr(str(equa))
            sol = calcObj.calculate
            if var == '_return_': #bit different if return expression as states wont be included
                out_d[var] = float(sol)
            
            else: ##updates states and final dict
                self.states[var] = float(sol)
                out_d[i] = self.states.copy()
            
        return out_d



def run_tests():
    import doctest

    #- Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    #doctest.run_docstring_examples(Calculator.calculate, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()