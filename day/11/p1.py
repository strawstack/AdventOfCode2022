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

def parseMonkey(lst):
    indexStr = lst[0]
    startingItemsStr = lst[1]
    operationStr = lst[2]
    testStr = lst[3]
    ifTrueStr = lst[4]
    ifFalseStr = lst[5]

    index = int(indexStr.split(" ")[1][:-1])

    startingItems = startingItemsStr.split(": ")[1]
    startingItemsQueue = Queue()
    for value in startingItems.split(","):
        number = int(value)
        startingItemsQueue.push(number)

    operation = operationStr.split(" ")[-2:]

    try:
        operator, value = operation[0], int(operation[1])
    except:
        operator, value = operation[0], operation[1]

    test = int(testStr.split(" ")[-1])

    ifTrue = int(ifTrueStr.split(" ")[-1])

    ifFalse = int(ifFalseStr.split(" ")[-1])

    return {
        "index": index,
        "items": startingItemsQueue,
        "op": {
            "operator": operator, 
            "value": value
        },
        "test": test,
        "ifTrue": ifTrue,
        "ifFalse": ifFalse
    }

def callTest(inspectItem, value):
    return inspectItem % value == 0

def callOp(inspectItem, op):
    operator = op["operator"]
    value = op["value"]

    if value == "old":
        value = inspectItem

    if operator == "+":
        return inspectItem + value

    elif operator == "*":
        return inspectItem * value

def sol(lines):
    lines = lines.split("\n\n")

    lines = [x.split("\n") for x in lines]

    monkeys = []
    for line in lines:
        monkeys.append(
            parseMonkey(line)
        )
    
    if False:
        for m in monkeys:
            print(m)

    ROUNDS = 20
    NUM_MONKEYS = len(monkeys)
    
    track_inspect = [0] * NUM_MONKEYS

    for r in range(ROUNDS):
        for i in range(NUM_MONKEYS):
            
            mky = monkeys[i]
            
            for j in range(mky["items"].queue_size()):

                track_inspect[i] += 1

                inspectItem = mky["items"].pop()
                inspectItem = callOp(inspectItem, mky["op"])
                inspectItem = inspectItem // 3
                t, f = mky["ifTrue"], mky["ifFalse"]
                sendTo = t if callTest(inspectItem, mky["test"]) else f
                
                monkeys[sendTo]["items"].push(inspectItem)

    track_inspect = list(reversed(sorted(track_inspect)))[:2]

    return track_inspect[0] * track_inspect[1]

def main():
    
    lines = open("input.txt").read().strip()
    #lines = [x[:-1] for x in open("input.txt").readlines()]
    
    ans = sol(lines)

    return ans

# cp p1.py p2.py
ans = main()
print(ans)