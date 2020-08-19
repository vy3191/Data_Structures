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
    return f"<Node: {self.value}"

class Linked_List:
  # A linear data structure that stores values in nodes
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail
    self.length = 0
  def is_list_empty(self):
    return self.head == None
  def find_length(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.next_node
    return count  
  def add_to_head(self,value):
    # if there is no node at all
    node = Node(self,value)
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      node.set_next_node(self.head)  


