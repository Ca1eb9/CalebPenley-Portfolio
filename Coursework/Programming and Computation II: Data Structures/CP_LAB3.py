d# LAB3
#Caleb Penley
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node: # You are not allowed to modify this class
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
        >>> sub1, sub2 = x.split()
        >>> sub1
        Head:Node(-7.5)
        Tail:Node(4)
        List:-7.5 -> 1 -> 3 -> 4
        >>> sub2
        Head:Node(5)
        Tail:Node(9.78)
        List:5 -> 8.76 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.add(1)
        >>> x.intersection(sub1)
        Head:Node(-7.5)
        Tail:Node(4)
        List:-7.5 -> 1 -> 3 -> 4
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self): #Checks if list is empty
        return self.head == None

    def __len__(self): #Returns length of list
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value): #Adds new node to linked list
        # --- YOUR CODE STARTS HERE
        newNode = Node(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            
            prev = self.head
            current = prev.next
            if prev.value > value: #Checks is the added value is less than the very first value in the list
                self.head = newNode
                newNode.next = prev
            else:
                while current is not None and current.value < newNode.value:
                    current = current.next
                    prev = prev.next
                if current is not None: #if there is a value in the list that is more than current value
                    newNode.next = current
                    prev.next = newNode
                else: #Define value as new biggest in list
                    self.tail = newNode
                    prev.next = newNode
                
                


    def split(self): #Splits a linked list
        # --- YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        else:
            leng = self.__len__()
            current = self.head
            new_list1 = SortedLinkedList()
            new_list2 = SortedLinkedList()
            for node in range((self.__len__())): #Iterate through all nodes in list

                    if node < leng/2:
                        # First half, always add to new_list1
                        new_list1.add(current.value)
                    elif leng % 2 == 0 and node >= leng/2 or leng % 2 != 0 and node > leng/2:
                        #Second half, conditionally add to new_list2 based on odd or even length
                        new_list2.add(current.value)
                    current = current.next
        return new_list1,new_list2
            




    def removeDuplicates(self): #removes duplicates from linked list
        # --- YOUR CODE STARTS HERE
        prev = self.head
        current = prev.next
        if float(prev.value) == float(current.value): #checks if first value is equal to current value and removes it if it is
            self.head = current
        while current and current.next:
            if float(current.next.value) == float(current.value): #Checks if next value is equal to current value, if it is then set new previous next to next value instead of current
                prev.next = current.next
                current = current.next
            else: #to check current value with next value again for edge cases of more than 2 duplicates
                current = current.next
                prev = prev.next
        
    

    def intersection(self, other): #creates new list with maatching elements from two lists
        # --- YOUR CODE STARTS HERE
        current1 = self.head
        current2 = other.head
        new_list = SortedLinkedList()
        while current1 and current2:  #iterate while both lists have elements
            if float(current1.value) == float(current2.value):
                # If values are equal, add to the new list
                new_list.add(current1.value)
                current1 = current1.next
                current2 = current2.next
            elif float(current1.value) < float(current2.value):
                # If the current value in list1 is smaller, move in list 1
                current1 = current1.next
            else:
                #Move in list 2
                current2 = current2.next
        new_list.removeDuplicates()
        return new_list






def run_tests():
    import doctest
    doctest.testmod(verbose=True)
    
if __name__ == "__main__":
    run_tests()
