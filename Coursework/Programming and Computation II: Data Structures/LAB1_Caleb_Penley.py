# LAB 1
### Caleb Penley
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import math, random

# -------- SECTION 1
class Instructor:
    '''
        >>> t1= Instructor('John Doe')
        >>> t1.get_name()
        'John Doe'
        >>> t1.get_courses()
        []
        >>> t1.add_course('MATH140')
        >>> t1.get_courses()
        ['MATH140']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH141')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH140')
        >>> t1.get_courses()
        ['STAT100']
    '''
    #Init self attributes
    def __init__(self, name):
        #--- YOUR CODE STARTS HERE
        self.name = name
        self.courses = []
    #Gets name of instructor
    def get_name(self):
        #--- YOUR CODE STARTS HERE
        return self.name
    ## sets new name of instructor
    def set_name(self, new_name):
        #--- YOUR CODE STARTS HERE
        self.name = new_name
    # returns list of current courses
    def get_courses(self):
        #--- YOUR CODE STARTS HERE
        return self.courses
    #removes the requested course from list if its in the list
    def remove_course(self, course):
        #--- YOUR CODE STARTS HERE
        if course in self.courses:
            self.courses.remove(course)
    #add course to the list if its not already in the list
    def add_course(self,course):
        #--- YOUR CODE STARTS HERE
        if course not in self.courses:
            
            self.courses.append(course)


# -------- SECTION 2      
class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """
    #Init attributes
    def __init__(self):
        self.items = {}
    #str for pantry object
    def __repr__(self):
        #--- YOUR CODE STARTS HERE
        return f'I am a Pantry object, my current stock is {self.items}'
    #adds stock
    def stock_pantry(self, item, qty):
        #--- YOUR CODE STARTS HERE
        current = 0.0
        if self.items.get(item): #checks if the stock is even named in pantry and gets the item count if it is
            current = self.items.get(item)
        self.items.update({item:float(qty+current)}) # sets new count
        return f'Pantry Stock for {item}: {self.items.get(item)}'

    #takes out item from pantry
    def get_item(self, item, qty):
        #--- YOUR CODE STARTS HERE
        if not self.items.get(item): #checks if item even exists in pantry
            return f"You don't have {item}"
        elif self.items.get(item) == 0.0: #checks if there are any items
            return f"You don't have {item}"
        elif self.items.get(item) - qty > 0.0: #checks if there will be items left after they are taken
            self.items.update({item: float(self.items.get(item) - qty)})
            return f'You have {self.items.get(item)} of {item} left'
        elif self.items.get(item) - qty == 0.0: #checks if there are 0 items left as that calls for an addition to shopping list
            self.items.update({item: float((self.items.get(item) - qty))})
            return f'Add {item} to your shopping list!'
        elif self.items.get(item) - qty < 0.0: # checks if there are going to be less than 0 left as they can only have 0 items
            self.items.update({item: float(0)})
            return f'Add {item} to your shopping list!'
    #transfers items from one pantry to another
    def transfer(self, other_pantry, item):
        #--- YOUR CODE STARTS HERE
        current = 0.0
        if self.items.get(item): #checks if existence
            current = self.items.get(item)
        if not other_pantry.items.get(item): #checks existence
            return
        if other_pantry.items.get(item) > 0: #transfers items by updating in both pantrys
            self.items.update({item: float(other_pantry.items.get(item)+current)})
            other_pantry.items.update({item: float(0)})


# -------- SECTION 3
class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3.0'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300.0'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6.0'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9.0'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5.0 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10.0'
        >>> east_machine.cancelTransaction()
        'Take your $10.0 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''
    #init attributes
    def __init__(self):
        #--- YOUR CODE STARTS HERE
        
        self.items = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]} 
        self.balance = 0.0


    #does purchasing in machine
    def purchase(self, item, qty=1): #most are self explainatory with use of strings
        #--- YOUR CODE STARTS HERE
        
        if item not in self.items: 
            return "Invalid item" 
        elif self.isStocked == False: 
            return "Machine out of stock" 
        elif self.items[item][1] == 0: 
            return "Item out of stock" 
        
        elif self.items[item][1] < qty: #not enough stock
            return f"Current {item} stock: {self.getStock[item][1]}, try again" 
        elif self.balance < qty * self.items[item][0]: #more than price given
            remain = qty * self.items[item][0]-self.balance 
            
            return f"Please deposit ${remain}"
        
        elif self.balance == qty * self.items[item][0]: #dispense
            self.items[item][1] -=qty 
            self.balance = 0.0 
            return "Item dispensed" 
        
        elif self.balance > qty * self.items[item][0]:
            rest = self.balance - qty * self.items[item][0]
            
            self.balance = 0.0 
            self.items[item][1] -= qty 
            
            return f"Item dispensed, take your ${rest} back"
        

    #deposit money
    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        
        
        
        if self.isStocked == False: 
            return f"Machine out of stock. Take your ${float(amount)} back" 
        
        self.balance += amount 
        
        return f"Balance: ${self.balance}"

    #restock machine
    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE 
        
        if item not in self.items:
            return "Invalid item" 
        self.items[item][1] += stock 
        
        
        return f"Current item stock: {self.items[item][1]}" 




    #--- YOUR CODE STARTS HERE
    @property
    def isStocked(self): 
        
        for item in self.items: 
            
            if self.items[item][1] > 0: 
                
                return True 
        
        return False
        

    #--- YOUR CODE STARTS HERE
    @property
    def getStock(self):
        
        return self.items


    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self.balance == 0:
            return
        
        out = self.balance 
        self.balance = 0.0
        
        return f"Take your ${out} back" 
       



# -------- SECTION 4
class Point2D:
    #init attributes
    def __init__(self, x, y):
        
        self.x = x
        
        self.y = y
    
    #equal component
    def __eq__(self, other):
        
        if type(other) !=Point2D: 
            return False 
        elif self.x == other.x and self.y == other.y: 
            return True
        
        return False
    

    #multiplication component
    def __mul__(self, other):
        
        if type(other) != int: 
            return
        return Point2D(self.x* other , self.y* other) 

class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''

    #init values
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.p1= point1 #pt 1
        
        self.p2= point2 #pt 2


    #--- YOUR CODE STARTS HERE
    @property #distance formula
    def getDistance(self):
        
        out = ( (self.p2.x -self.p1.x)** 2 +(self.p2.y- self.p1.y)** 2 ) **(1/2)
        return round(out,3)
       
    
    #--- YOUR CODE STARTS HERE 
    @property #slope calculator
    def getSlope(self): 
        
        rise =self.p2.y -self.p1.y 

        run= self.p2.x -self.p1.x 
        
        if run == 0: 
            return float("inf") 
        out = (rise/ run)
        return round(out, 3)

    def __str__(self): #string output for user
        
        slope = self.getSlope 
        
        if slope == float("inf"):
            return "Undefined" 
        
        y = abs(round(self.p1.y - (slope * self.p1.x),3))
        
        if slope > 0 and y > 0 or slope < 0 and y > 0: 
            
            return f"y = {slope}x + {y}" 
        
        elif slope > 0 and y < 0: 
            
            return f"y = {slope}x - {y}" 
        
        elif slope == 0: 
            return f"y = {y}" 
        elif y == 0: 
            return f"y = {y}x"


    def __eq__ (self, other): #is equal comp
        
        if type(other) != Line: 
            return False 
        
        
        return self.p1 == other.p1 and self.p2 == other.p2
    
    def __mul__ (self, other): #Multiplation component
        
        newpt1 = self.p1* other 
        newpt2 = self.p2 *other 
        
        return Line(newpt1, newpt2)
    
    def __contains__ (self, other): 
        if type(other) != Point2D: 
            return False 
        if self.p1.y - other.y == (self.getSlope * (self.p1.x - other.x)): 
            return True 
        
        return False

    __repr__ = __str__ #creates the correct special method for the class to work


def run_tests():
    import doctest

    # Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Pantry with the name of the class you want to test
    #doctest.run_docstring_examples(VendingMachine, globals(), name='LAB1',verbose=True)

if __name__ == "__main__":
    run_tests()