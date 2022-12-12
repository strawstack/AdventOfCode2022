class QueueItem():
    def __init__(self, prev, nextRef, item):
        self.prev = prev
        self.next = nextRef
        self.item = item

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, item):
        self.size += 1
        queueItem = QueueItem(None, None, item)
        if self.head == None:
            self.head = queueItem
            self.tail = queueItem
        else:
            queueItem.next = self.head
            self.head.prev = queueItem
            self.head = queueItem

    def pop(self):
        self.size -= 1
        if self.tail == None:
            raise "Empty Queue"
        else:
            queueItem = self.tail
            self.tail = self.tail.prev
            if self.tail != None:
                self.tail.next = None
            else:
                self.head = None
            return queueItem.item
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        lst = []
        cur = self.head
        while cur != None:
            lst.append(str(cur.item))
            cur = cur.next
        return "Queue: " + ", ".join(lst)

    def queue_size(self):
        return self.size