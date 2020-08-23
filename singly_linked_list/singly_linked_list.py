class Node:
  # An object for storing a single node in a linked list
  def __init__(self, value, next_node=None):
    self.value = value  # data stored in the node
    self.next_node = next_node  # Reference to next node in the linked list

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, new_next_node):
    self.next_node = new_next_node

  def __repr__(self):
    return f"<Node value: {self.value}>"

class LinkedList:
  # A linear data structure that stores values in nodes
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail
    self.length = 0
  def is_list_empty(self):
    return self.head == None
  def find_size(self):
    current = self.head   # O(1)
    count = 0
    while current:
      count += 1
      current = current.next_node
    return count  

  def add_to_head(self,value):
    # if there is no node at all
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
      self.head.next_node = None
    else:
      new_node.set_next_node(self.head)  
      self.head = new_node
    self.length +=1

  def add_to_tail(self,value):
    new_node = Node(value)
    if self.head is None:    #  O(1)
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next_node(new_node)  #  O(1)
      self.tail = new_node      
    self.length += 1  

  def remove_head(self):
    # say if there are no node at all in the list
    deleted_value = None
    if self.head is None:
      return None
    elif self.head == self.tail:
      deleted_value = self.head.get_value()
      self.head = None
      self.tail = None
      self.length -= 1
    # if there are more than one node
    else:
      deleted_value = self.head.get_value()
      self.head = self.head.get_next_node()
      self.length -= 1
    return deleted_value  

  def remove_tail(self):
    # if there are no nodes to remove
    if self.tail is None:
      return None
    elif self.head == self.tail:
      deleted_value = self.tail.value
      print(f"line81{deleted_value}")
      self.head = None
      self.tail = None
      self.length -= 1
      return deleted_value
    else:
      current = self.head
      while current.next_node is not self.tail:
        print(current.value)
        current = current.next_node
      print(f"value before tail is: {current.value}")  
      deleted_value = self.tail.value
      self.tail = current
      current.next_node = None  
      self.length -=1   

    return deleted_value

  def remove_at_index(self,index):
    #if index value greater than/equal to the size of the LinkedList
    if index >= self.length:
      return None
    # if there is only one node in the linked list
    if self.head == self.tail or (self.length == 1 and index ==0):
      target = self.head
      self.head = None
      self.target = None
      self.length -= 1
      return target.value
    
    current = self.head     
    for i in range(index-1):
      current = current.next_node
    target = current.next_node
    current.next_node = target.next_node
    target.next_node = None  
    self.length -= 1
    return target.value

  def insert_at_index(self,index,value):
    #if there is no index
    if not index:
      return None
    #if there is no value
    if not value:
      return None
    #if there are no nodes in the linked list
    if self.length == 0:
      self.head = Node(value)
      self.tail = Node(value)  
    # #if index is zero
    # if index == 0:
    #   self.add_to_head(value)
    # if index == self.length:
    #   self.add_to_tail(value)
    #anywhere in the LinkedList
    previous = self.head
    new_node = Node(value)
    for i in range(index-1):
      previous = previous.next_node
    target = previous.next_node
    previous.next_node = new_node
    new_node.next_node = target
    self.length += 1       

  def search(self,key):
    current = self.head
    while current:
      if current.value == key:
        return current
      else:
        current = current.next_node
    return None        

  def __repr__(self):
    current = self.head
    nodes = []
    while current:
      if current is self.head:
        nodes.append(f"[Head: {current.value}]") 
        current = current.next_node
      elif current.next_node is None:
        nodes.append(f"[Tail: {current.value}]")
        current = current.next_node 
      else:
        nodes.append(f"[{current.value}]")  
        current = current.next_node
    return '-->'.join(nodes)    
      





