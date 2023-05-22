class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
    def __repr__(self):
        return f"<Node data: {self.data}>"
    
class LinkedList:
    def __init__(self):
        self.__head = None
    
    def isempty(self):
        return self.__head == None
        
    def size(self):
        current = self.__head
        length = 0
        
        while current:
            length += 1
            current = current.next_node
            
        return length
    
    def add(self, data):
        assert isinstance(data, Node) == False, "Inserted data shouldn't be a Node"
        new_node = Node(data)
        new_node.next_node = self.__head
        self.__head = new_node
    
            
    def __repr__(self):
        current = self.__head
        nodes = []
        
        while current:
            if current == self.__head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node == None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(str(current.data))
            current = current.next_node
        
        return ' -> '. join(nodes)
    
    def search(self, key):
        current = self.__head
        
        while current:
            if current.data == key:
                return current
            current = current.next_node
        return None
    
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        else:
            new_node = Node(data)
            
            current = self.__head
            position = index
        
            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new_node
            new_node.next_node = next_node
            
    def remove(self, key):
        current = self.__head
        previous = None
        found = False
        
        while current and not found:
            if current.data == key and current is self.__head:
                found = True
                self.__head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current
    
    def node_at_index(self, index):
        if index == 0:
            return self.__head
        else:
            current = self.__head
            position = 0
            
            while position < index:
                current = current.next_node
                position += 1
                
            return current
                