class btn:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
def insert(root,newvalue):
        if root is None:
            root=btn(newvalue)
            return root
        if newvalue<root.data:
            root.leftchild=insert(root.lefchild,newvalue)
        else:
            root.right=insert(root.right,newvalue)
        return root
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
root=insert(None,14)
insert(root,10)
insert(root,15)
insert(root,16)
insert(root,17)
insert(root,18)
print("inorder traversal")
inorder(root)

        
        
