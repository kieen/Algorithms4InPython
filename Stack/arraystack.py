class ArrayStack:
    """implementation of a stack using array (Python List).
       
       Since in (standard) Python we can only create non-fixed-size list, 
       we dont' need to do resizing. The resizing relies on Python. 
       
       However, you can use third party library like numpy (http://www.numpy.org/)
       for more efficient array data structure. 
        
    """
    def __init__(self):
        _a=[]
        #_size=0
        #_top=-1
    def push(self, item):
        #_size++
        #_top++
        self._a.append(item)
    def pop(self):
        #_size--
        #-top--      
        "The pop() method removes and returns the last item if index is not provided."
        return self._a.pop()
    
        