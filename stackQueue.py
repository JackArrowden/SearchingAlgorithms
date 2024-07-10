### Class FIFOQueue

class FIFOQueue:
    def __init__(self):
        self.elements = []
    
    def length(self):
        return len(self.elements)
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self, node):
        self.elements.append(node)
    
    def pop(self):
        if not self.is_empty():
            return self.elements.pop(0)
        return None

class LIFOQueue:
    def __init__(self):
        self.elements = []
    
    def length(self):
        return len(self.elements)
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self, node):
        self.elements.append(node)
    
    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        return None

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def length(self):
        return len(self.elements)
    
    def sort(self):
        self.priorityQueue.sort()
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self, node):
        self.elements.append(node)
        self.elements.sort()
        
    def pop(self):
        if not self.is_empty():
            return self.elements.pop(0)
        return None