class MinStack:
    # @param x, an integer
    # @return an integer
   
    def __init__(self):
        self.data=[]
        self.mindata=[]
        
    def push(self, x):
        self.data.append(x)
        if len(self.mindata)==0:
            self.mindata.append(x)
        elif x<=self.mindata[-1]:
            self.mindata.append(x)
            
        
        
    # @return nothing
    def pop(self):
        if self.isEmpty():
            raise("stack is empty")
        
        if self.data.pop()==self.mindata[-1]:
            self.mindata.pop()
        

    # @return an integer
    def top(self):
        if self.isEmpty():
            raise("stack is empty")     
        return self.data[-1]
        

    # @return an integer
    def getMin(self):
        return self.mindata[-1]
        
    def isEmpty(self):
        return len(self.data)==0


