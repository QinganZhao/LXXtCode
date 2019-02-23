class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        dummy = self.head
        i = 0 
        while dummy:
            if i == index:
                return dummy.val
            i += 1
            dummy = dummy.next
        return -1
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        dummy = ListNode(val) 
        dummy.next = self.head
        self.head = dummy
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        dummy = self.head
        while dummy.next:
            dummy = dummy.next
        dummy.next = ListNode(val)

        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        dummy = self.head
        i = 0
        while dummy:
            i += 1
            if i == index:
                tmp = dummy.next
                dummy.next = ListNode(val)
                dummy.next.next = tmp
                return
            dummy = dummy.next
                
                
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        dummy = self.head
        i = 0
        if i == index:
            self.head = dummy.next
            return
        while dummy.next:
            i += 1
            if i == index:
                dummy.next = dummy.next.next
                return
            dummy = dummy.next
            

class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
