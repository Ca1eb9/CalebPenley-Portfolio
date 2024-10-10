# HW 5
# CP
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.getMin
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self): #Get root of heap as it is min
        # - YOUR CODE STARTS HERE -
        if len(self) != 0:
            return self._heap[0]
        return None
    
    def _parent(self,index): #Get parent value by using formula
        # - YOUR CODE STARTS HERE -
        out = None
        try:
            out = self._heap[(index//2)-1] #Index correction used
        except:
            pass
        if index-1 == 0: #Edge case where root does not have a parent
            out=None
        return out

        

    def _leftChild(self,index): #Get left child value by using formula
        # - YOUR CODE STARTS HERE -
        out = None
        try:
            out = self._heap[(2*index)-1] #Index correction used
        except:
            pass
        return out


    def _rightChild(self,index): #Get right child value by using formula
        # - YOUR CODE STARTS HERE -
        out = None
        try:
            out = self._heap[(2*index+1)-1] #index correction used
        except:
            pass
        return out
 
      

    def insert(self,item): #Insert new node into heap while percolating up
        # - YOUR CODE STARTS HERE -
        self._heap.append(item)

        index = len(self)-1
        
        while index > 0:
            parent = ((index+1)//2)-1 #Parent index
            if self._parent(index+1) is None: #Edge case where current node is in root position and does not have parent
                index = 0
            elif self._heap[index] < self._parent(index+1): #Compare parent and switch if needed
                self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
                index = parent
            else:
                index = 0
        return

    def deleteMin(self): #Deletes root and moves last node to root and percolates down
        if len(self)==0:
            return None        
        elif len(self)==1:
            value=self._heap[0]
            self._heap=[]
            return value

        # - YOUR CODE STARTS HERE -
        ####Init
        value = self._heap[0]
        done = False
        child = None
        self._heap[0] = self._heap[len(self._heap)-1] #Switch last node and root
        self._heap.pop(len(self._heap)-1) #Remove last node
        index = 0
        ####
        while not done:
            if self._leftChild(index+1) is None and self._rightChild(index+1) is None: #No children to percolate to edgecase
                done=True

            elif self._leftChild(index+1) is None: #Only right child edgecase
                child = self._rightChild(index+1)
                child_index = 2*(index+1)

            elif self._rightChild(index+1) is None: #Only left child edgecase
                child = self._leftChild(index+1)
                child_index = 2*(index+1)-1

            elif self._leftChild(index+1) == self._rightChild(index+1): #Edge case where children are the same
                child = self._leftChild(index+1)
                child_index = 2*(index+1)-1

            elif self._leftChild(index+1) < self._rightChild(index+1): #Finding smallest child
                child = self._leftChild(index+1)
                child_index = 2*(index+1)-1

            else:
                child = self._rightChild(index+1)
                child_index = 2*(index+1)

            if child is None: #No children to percolate to without comparing child value and node
                pass

            elif child < self._heap[index]: #Compare child value and node value to percolate down
                self._heap[index],self._heap[child_index] = self._heap[child_index], self._heap[index]
                index = child_index

            else:
                done = True
        return value



class PriorityQueue:
    '''
        >>> priority_q = PriorityQueue()
        >>> priority_q.isEmpty()
        True
        >>> priority_q.peek()
        >>> priority_q.enqueue('sara',0)
        >>> priority_q
        [(0, 'sara')]
        >>> priority_q.enqueue('kyle',3)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle')]
        >>> priority_q.enqueue('harsh',1)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh')]
        >>> priority_q.enqueue('ajay',5)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay')]
        >>> priority_q.enqueue('daniel',4)
        >>> priority_q.isEmpty()
        False
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay'), (4, 'daniel')]
        >>> priority_q.enqueue('ryan',7)
        >>> priority_q
        [(0, 'sara'), (3, 'kyle'), (1, 'harsh'), (5, 'ajay'), (4, 'daniel'), (7, 'ryan')]
        >>> priority_q.dequeue()
        (0, 'sara')
        >>> priority_q.peek()
        'harsh'
        >>> priority_q
        [(1, 'harsh'), (3, 'kyle'), (7, 'ryan'), (5, 'ajay'), (4, 'daniel')]
        >>> priority_q.dequeue()
        (1, 'harsh')
        >>> len(priority_q)
        4
        >>> priority_q.dequeue()
        (3, 'kyle')
        >>> priority_q.dequeue()
        (4, 'daniel')
        >>> priority_q.dequeue()
        (5, 'ajay')
        >>> priority_q.dequeue()
        (7, 'ryan')
        >>> priority_q.dequeue()
        >>> priority_q.isEmpty()
        True
    '''

    def __init__(self):
        self._items = MinBinaryHeap()
    
    def enqueue(self, value, priority): #Insert into heap using given values
        # - YOUR CODE STARTS HERE -
        self._items.insert((priority,value))
    
    def dequeue(self): #Delete first item in queue using heap principles
        # - YOUR CODE STARTS HERE -
        return self._items.deleteMin()
    
    def peek(self): #Get value of first item in queue without popping by using len to make sure it has atleast one item
        # - YOUR CODE STARTS HERE -
        if len(self) != 0:
            return self._items._heap[0][1]
        return None
    
    def isEmpty(self): #Check if queue is empty by using len
        # - YOUR CODE STARTS HERE -
       if len(self) == 0:
            return True
       return False

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    __repr__ = __str__





class Graph:
    """
        >>> d_g1={
        ... 'A':[('B',2),('C',6),('D',7)],
        ... 'B':[('C',3),('G',12)],
        ... 'C':[('D',2),('E',3)],
        ... 'D':[('C',1),('E',2)],
        ... 'E':[('G',5)],
        ... 'F':[('D',2),('E',4)]}
        >>> my_graph = Graph(d_g1)
        >>> my_graph.addEdge('G', 'C', 4)
        >>> my_graph
        {'A': [('B', 2), ('C', 6), ('D', 7)], 'B': [('C', 3), ('G', 12)], 'C': [('D', 2), ('E', 3)], 'D': [('C', 1), ('E', 2)], 'E': [('G', 5)], 'F': [('D', 2), ('E', 4)], 'G': [('C', 4)]}
        >>> my_graph.dijkstra_table('A')   # ---> order of key,value pairs does not matter 
        {'A': 0, 'B': 2, 'C': 5, 'D': 7, 'E': 8, 'F': inf, 'G': 13}
    """
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:
            self.vertList = graph_repr

    def __str__(self):
        return str(self.vertList)

    __repr__ = __str__

    def addVertex(self, key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList

    def addEdge(self, frm, to, cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))


    def dijkstra_table(self,start): #Creates dijkstra table by checking all neighboring nodes and comparing all possible costs to see the lowest possible cost from start to each node in graph
        # - YOUR CODE STARTS HERE -
       

        ####Init
        queue = PriorityQueue()
        table = {}
        for i in self.vertList: #Define each node as inf cost
            table[i]=float('inf')
        if start in table: 
            table[start] = 0
        if start in self.vertList:
            queue.enqueue(start,0)
        ####
        while queue: #Checks all nodes before ending loop
            node = queue.dequeue()
            for item in self.vertList[node[1]]:
                
                total_cost = item[1]+table[node[1]]
                
                if table[item[0]]>total_cost: #Replace new lowest cost and add to queue for later
                    table[item[0]] = total_cost
                    
                    queue.enqueue(*item)
        return table
    

def run_tests():
    import doctest

    # Run start tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run start tests per class
    doctest.run_docstring_examples(Graph, globals(), name='HW5',verbose=True)   

if __name__ == "__main__":
    run_tests()

