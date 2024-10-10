# HW2
# Caleb Penley
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits): #Vars init
        # YOUR CODE STARTS HERE
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self): #String display method
        # YOUR CODE STARTS HERE
        return self.cid + f'({self.credits}): '+self.cname

    __repr__ = __str__

    def __eq__(self, other): #Equal method and detecting edge cases
        # YOUR CODE STARTS HERE
        if not other or not self:
            return False
        elif not isinstance(self, Course) or not isinstance(other, Course):
            return False
        elif self.cid == other.cid:
            return True
        else:
            return False



class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self): #Vars init
        # YOUR CODE STARTS HERE
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits): #Adds course if not already in course offerings
        # YOUR CODE STARTS HERE
        if cid not in self.courseOfferings:
            self.courseOfferings.update({cid:Course(cid,cname,credits)})
            return 'Course added successfully”'
        else:
            return 'Course already added”'
    
    def removeCourse(self, cid): #Removes course if in offerings
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:
            self.courseOfferings.pop(cid)
            return "Course removed successfully"
        else:
            return "Course not found"

    def _loadCatalog(self, file): #Load data from file for catalog
        with open(file, 'r') as f: 
            course_info = f.readlines()  # You might change .readlines() for .read() if it suits your implementation 
        # YOUR CODE STARTS HERE
        
        for line in course_info:
            line = line.strip('\n')
            line = line.split(',')
            cid = line[0]
            cname = line[1]
            credits = line[2]
            self.addCourse(cid,cname,credits)

class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self): #Vars init
        # --- YOUR CODE STARTS HERE
        self.courses = {}



    def __str__(self): #Creates a string output for semester of courses by getting all course objects within the dict
        # YOUR CODE STARTS HERE
        out = ''
        if len(self.courses) > 0:
            cnt = len(self.courses)
            for course in self.courses:
                out += course
                if cnt != 1:
                    out += '; '
                cnt -= 1
            return out
        else:
            return "No courses"

    __repr__ = __str__

    def addCourse(self, course): #Adds course to semester if not already in it
        # YOUR CODE STARTS HERE
        if course.cid not in self.courses:
            self.courses.update({course.cid: course})
        else:
            return 'Course already added'

    def dropCourse(self, course): #Drops course if exists in semester
        # YOUR CODE STARTS HERE
        if course.cid in self.courses:
            self.courses.pop(course.cid)
        else:
            return "No such course"

    @property
    def totalCredits(self): #Calc total credits for each course
        # YOUR CODE STARTS HERE
        credits = 0
        for course in self.courses:
            credits += int(self.courses[course].credits)
        return credits

    @property
    def isFullTime(self): #Full time if more than or 12 credits this semester
        # YOUR CODE STARTS HERE
        if self.totalCredits < 12:
            return False
        else:
            return True

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount): #Vars init
        # YOUR CODE STARTS HERE
        self.loan_id = self.__getloanID
        self.amount = amount


    def __str__(self): #Str for loan balance
        # YOUR CODE STARTS HERE
        return "Balance: $" + str(self.amount)

    __repr__ = __str__


    @property
    def __getloanID(self): #attribute method for random load id
        # YOUR CODE STARTS HERE
        return random.randint(10000, 99999)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''
    def __init__(self, name, ssn): #Var init
        # YOUR CODE STARTS HERE
        self.name = name
        self.__ssn = ssn

    def __str__(self): #Str for person object using string manipulation
        # YOUR CODE STARTS HERE
        return f'Person({self.name}, ***-**-{str(self.get_ssn())[7:]})'

    __repr__ = __str__
    

    def get_ssn(self): #Getter method for private ssn attribute
        # YOUR CODE STARTS HERE
        return self.__ssn

    def __eq__(self, other): #Equality method while detecting for certain edge cases
        # YOUR CODE STARTS HERE
        if not self or not other:
            return False
        elif not isinstance(self, Person) or not isinstance(other, Person):
            return False
        elif self.get_ssn() == other.get_ssn():
            return True
        return False


class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):#Var init
        # YOUR CODE STARTS HERE
        super().__init__(name,ssn)
        self.__supervisor = supervisor

    def __str__(self): #Str for staff with name and id
        # YOUR CODE STARTS HERE
        return f'Staff({self.name}, {self.id})'

    __repr__ = __str__


    @property
    def id(self):#Creates id through some str manipulation and getting ssn
        # YOUR CODE STARTS HERE
        initials = ''
        for i in self.name.split(' '):
            initials += i[:1]
        initials = initials.lower()
        return f'905{initials}{str(super().get_ssn())[7:]}'

    @property   
    def getSupervisor(self): #Getter method for private supervisor attribute
        # YOUR CODE STARTS HERE
        return self.__supervisor
    
    def setSupervisor(self, new_supervisor): #Setter method for setting supervisor to person
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor,Staff):
            self.__supervisor = new_supervisor
            return 'Completed!'
        else:
            return

    def applyHold(self, student): #Apply hold if student instance
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = True
            return 'Completed!'
        else:
            return

    def removeHold(self, student): #Removes hold if student instance
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = False
            return 'Completed!'
        else:
            return

    def unenrollStudent(self, student): #Sets active status to False if student instance
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False
            return 'Completed!'
        else:
            return

    def createStudent(self, person): #Creates student instance with given details
        # YOUR CODE STARTS HERE
        return Student(person.name,person.get_ssn(),'Freshman')




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''
    def __init__(self, name, ssn, year): #Var init
        random.seed(1)
        # YOUR CODE STARTS HERE
        super().__init__(name,ssn)
        self.classCode = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()
    
    def __str__(self): #Str for student display
        # YOUR CODE STARTS HERE
        return f'Student({self.name}, {self.id}, {self.classCode})'

    __repr__ = __str__

    def __createStudentAccount(self): #create student account for student if active
        # YOUR CODE STARTS HERE
        if self.active == True:
            return StudentAccount(self)
        else:
            return


    @property
    def id(self): #Creates id through str manipulation
        # YOUR CODE STARTS HERE
        initials = ''
        for i in self.name.split(' '):
            initials += i[:1]
        initials = initials.lower()
        return f'{initials}{str(super().get_ssn())[7:]}'

    def registerSemester(self): #Registers a semesters and adds it to the amount of semesters and changes year if need be all if the student if active and has no holds
        # YOUR CODE STARTS HERE
        if self.active == True and self.hold == False:
            self.semesters.update({(len(self.semesters)+1): Semester()})
            if 4 > len(self.semesters) > 2 :
                self.classCode = 'Sophomore'
            elif 6 > len(self.semesters) > 4:
                self.classCode = 'Junior'
            elif len(self.semesters) > 6:
                self.classCode = 'Senior'
        else:
            return "Unsuccessful operation"



    def enrollCourse(self, cid, catalog): #Enrolls in course and charges account if all conditions are aligned like active and no holds
        # YOUR CODE STARTS HERE
        if self.active == False or self.hold == True:
            return "Unsuccessful operation"
        elif cid in catalog.courseOfferings:
            if self.semesters[len(self.semesters)].addCourse(catalog.courseOfferings.get(cid)) != None:
                return 'Course already enrolled'
            self.account.chargeAccount(self.account.CREDIT_PRICE*int(catalog.courseOfferings.get(cid).credits))
            return "Course added successfully"
        return 'Course not found'
        

    def dropCourse(self, cid): #Drops course and makes %50 refund if all conditions align like active and no holds
        # YOUR CODE STARTS HERE
        if self.active == False or self.hold == True:
            return "Unsuccessful operation"
        elif cid not in self.semesters[len(self.semesters)].courses:
            return 'Course not found'
        
        else:
            self.account.makePayment(float((self.account.CREDIT_PRICE)*int(self.semesters[len(self.semesters)].courses.get(cid).credits)//2))
            self.semesters[len(self.semesters)].dropCourse(self.semesters[len(self.semesters)].courses.get(cid))
            return "Course dropped successfully"
    


    def getLoan(self, amount): #Makes loan and adds it to account loan dict and makes payment to the account balance
        # YOUR CODE STARTS HERE
        if self.active == False:
            return 'Unsuccessful operation'
        elif self.semesters[len(self.semesters)].isFullTime == False:
            return "Not full-time"
        else:
            loan = Loan(amount)
            self.account.loans.update({loan.loan_id: loan})
            self.account.makePayment(amount)





class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    CREDIT_PRICE = 1000 #Declares class attr
    def __init__(self, student): #Var init
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0
        self.loans = {}


    def __str__(self): #Str for student account
        # YOUR CODE STARTS HERE
        return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'

    __repr__ = __str__


    def makePayment(self, amount): #Subtracts amount to account for a payment
        # YOUR CODE STARTS HERE
        self.balance -= amount
        return self.balance


    def chargeAccount(self, amount): #Adds amount to account for a charge
        # YOUR CODE STARTS HERE
        self.balance += amount
        return self.balance




def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    #doctest.run_docstring_examples(Student, globals(), name='HW2',verbose=True)   

if __name__ == "__main__":
    run_tests()