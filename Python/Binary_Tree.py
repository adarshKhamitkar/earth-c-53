class Binary_Tree:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    def insert_left(self,data):
        if(self.left_child == None):
            self.left_child = Binary_Tree(data)
        else:
            new_node = Binary_Tree(data)
            new_node.left_child = self.left_child
            self.left_child = new_node
            
    def insert_right(self,data):
        if(self.right_child == None):
            self.right_child = Binary_Tree(data)
        else:
            new_node = Binary_Tree(data)
            new_node.right_child = self.right_child
            self.right_child = new_node
            
# Depth First Search (DFS)
    
    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
            
        print(self.data)
        
        if self.right_child:
            self.right_child.inorder()


    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
            
        if self.right_child:
            self.right_child.postorder()
            
        print(self.data)
        
    def preorder(self):
        print(self.data)
        
        if self.left_child:
            self.left_child.preorder()
            
        if self.right_child:
            self.right_child.preorder()    
    
if __name__ == "__main__":
    
    tree = Binary_Tree(4)
    
    tree.insert_left(2)
    tree.insert_right(6)
    
    tree.left_child.insert_left(1)
    tree.left_child.insert_right(3)
    
    tree.right_child.insert_left(5)
    tree.right_child.insert_right(7)
    
    print("In Order DFS")
    tree.inorder()
    
    print("Pre Order DFS")
    tree.preorder()
    
    print("Post Order DFS")
    tree.postorder()
    
