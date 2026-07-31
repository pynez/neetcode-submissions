class LinkedList:
    # we create a Node class to hold values.
    class Node:
        def __init__(self, val, nextNode):
            self.value = val
            self.nextNode = nextNode

        def val(self):
            return self.value

        def getNext(self):
            return self.nextNode

        def setNext(self, other):
            self.nextNode = other

    #LinkedList class methods
    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        #list is empty. nothing to get!
        if self.length == 0:
            return -1
        if ((index < 0) or (index > self.length)):
            # index out of bounds
            return -1
        currNode = self.head
        for i in range(self.length):
            if i == index:
                return currNode.val()
            currNode = currNode.getNext()
        

    def insertHead(self, val: int) -> None:
        newNode = self.Node(val, self.head)
        self.head = newNode
        self.length += 1

    def insertTail(self, val: int) -> None:
        currNode = self.head
        while (not (currNode.getNext() == None)):
            currNode = currNode.getNext
        newNode = self.Node(val, None)
        currNode.setNext(newNode)
        self.length += 1

    def remove(self, index: int) -> bool:
        if ((index < 0) or (index > self.length)):
            return False

        #edge case: index == 0
        if index == 0:
            self.head = self.head.getNext()
            self.length -= 1
            return True
        prevNode = self.head
        for i in range(index-1):
            prevNode = prevNode.getNext
        prevNode.setNext(prevNode.getNext().getNext())
        self.length -= 1
        return True
        


    def getValues(self) -> List[int]:
        currNode = self.head
        out = []
        for i in range(self.length):
            out.append(currNode.val())
            currNode = currNode.getNext()

        return out

        
