class BT:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
    def insert(root,newvalue):
        if root is None:
            root=BT(newvalue)
            return root
        if newvalue<root.data:
            root.leftchild=insert(root.leftchild,newvalue)
        else:
            root.rightchild=insert(root.rightchild,newvalue)

        return root
    def inorder(root):
        if root==None:
            return
        inorder(root.leftchild)
        inorder(root.rightchild)
        print(root.data)
root=insert(None,15)
insert(root,10)
insert(root,25)
insert(root,26)
insert(root,27)
insert(root,28)
insert(root,29)
print("printing values of inorder traversal")
inorder(root)
    
