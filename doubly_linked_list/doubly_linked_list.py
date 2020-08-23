"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create a new node
        new_node = ListNode(value)
        #if there is no node in the LinkedList
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.prev = None
            self.next = None   
        else:  
            new_node.prev = None
            new_node.next = self.head
            self.head = new_node
            new_node.next.prev = new_node
        self.length += 1    

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        del_value = None
        #if there is no node return None
        if self.length == 0:
            return None
        #if there is only one node
        elif self.head == self.tail:
            del_value = self.head.value
            self.head = None
            self.tail = None
        else:
            current = self.head
            self.head = current.next
            current.next.prev = None
            del_value = current.value
        self.length -= 1
        return del_value     
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        #if there is no node at all
        if self.head == None or self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

    