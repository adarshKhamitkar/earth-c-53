class BinarySearchTree:
    
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    def insert_data(self,data):
        if data <= self.data and self.left_child:
            self.left_child.insert_data(data)
        elif data<= self.data:
            self.left_child = BinarySearchTree(data)
        elif data > self.data and self.right_child:
            self.right_child.insert_data(data)
        else:
            self.right_child = BinarySearchTree(data)
            
    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.data)
        
        if self.right_child:
            self.right_child.in_order()


    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
            
        if self.right_child:
            self.right_child.post_order()
            
        print(self.data)
        
        
    def pre_order(self):
        print(self.data)
        
        if self.left_child:
            self.left_child.pre_order()
            
        if self.right_child:
            self.right_child.pre_order()
            
    def find_node(self,data,iteration=0):
        if(data < self.data and self.left_child):
            iteration+=1
            self.left_child.find_node(data,iteration)
        elif(data > self.data and self.right_child):
            iteration+=1
            self.right_child.find_node(data,iteration)
        elif(data == self.data):
            print(f"{data} found after {iteration} iterations")
        else:
            print(f"{data} is not a member of this tree")
            
            
if __name__ == "__main__":
    
    bst = BinarySearchTree(50)
    bst.insert_data(4)
    bst.insert_data(21)
    bst.insert_data(76)
    bst.insert_data(100)
    bst.insert_data(32)
    bst.insert_data(52)
    bst.insert_data(64)
    
    print("In Order")
    bst.in_order()
    print("Pre Order")
    bst.pre_order()
    print("Post Order")
    bst.post_order()
    
    bst.find_node(50)
    bst.find_node(64)
    bst.find_node(100)
    bst.find_node(4)
    bst.find_node(32)
    bst.find_node(21)
    bst.find_node(75)

##################### Output #####################
# In Order
# 4
# 21
# 32
# 50
# 52
# 64
# 76
# 100
# Pre Order
# 50
# 4
# 21
# 32
# 76
# 52
# 64
# 100
# Post Order
# 32
# 21
# 4
# 64
# 52
# 100
# 76
# 50
# 50 found after 0 iterations
# 64 found after 3 iterations
# 100 found after 2 iterations
# 4 found after 1 iterations
# 32 found after 3 iterations
# 21 found after 2 iterations
# 75 is not a member of this tree
