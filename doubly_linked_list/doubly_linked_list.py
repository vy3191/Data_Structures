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
        #if there is no node at all
        del_value = None
        if self.head == None or self.tail == None:
            return None
        elif self.head == self.tail:
            del_value = self.head.value
            self.head = None
            self.tail = None
        else:
            del_value = self.tail.value
            previous_node = self.tail.prev
            self.tail = previous_node
            self.tail.next = None
        self.length -= 1
        return del_value
                
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #if there is no node at all
        if self.length == 0:
            return None
        else:
            self.delete(node)
            self.add_to_head(node.value)
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length ==0:
            return None
        else:
            self.delete(node)    
            self.add_to_tail(node.value)
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # self.length -= 1
        print(f"line 126 {node.value}")
        if self.length == 0:
            print("There are no nodes in the linked list")
            return None
        elif self.length ==1 and self.head.value !=node.value:
            return None    
        elif self.head.value == node.value and self.tail.value == node.value:
            self.head = None
            self.tail = None
            self.length -= 1
            return node.value 
        elif self.head.value == node.value and self.tail.value != node.value:
            del_val = self.remove_from_head()    
            # self.length -= 1
            return del_val
        elif self.tail.value == node.value and self.head.value != node.value:
            del_val = self.remove_from_tail()
            # self.length -= 1
            return del_val
        else:
            previous_node = node.prev  
            print(f"previous Node 146{previous_node}") 
            previous_node.next = node.next
            next_node = node.next
            print('next-node line 149{n}')
            next_node.prev = previous_node
            self.length -= 1
            node.prev = None
            node.next = None
            return node.value 
            # node.prev.next = node.next
            # node.next.prev = node.prev
            self.length -= 1
            return node
      

       

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if there are no nodes at all
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head.value    
        else:
            max = self.head.value
            current = self.head
            while current:
                if max < current.value:
                    max = current.value
                current = current.next      
        return max          

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            if current is self.head:
                nodes.append(f"[Head:{current.value}]")
                current = current.next
            elif current is self.tail:
                nodes.append(f"[Tail:{current.value}]")
                current = current.next
            else:
                nodes.append(f"[{current.value}]")
                current = current.next
        return '-->'.join(nodes)         


    