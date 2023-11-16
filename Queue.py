class Queue:
    def __init__(self):
        self.queue = list()

    def add(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        else:
            return False
        
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")
    
AQueue = Queue()
AQueue.add("Mon")
AQueue.add("Tue")
AQueue.add("Wed")
print(AQueue.remove())
print(AQueue.remove())