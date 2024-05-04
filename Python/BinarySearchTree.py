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
