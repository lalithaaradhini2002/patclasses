class newNode:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
        self.hd=0
    def topview(root):
        if(root==None):
            return
        q=[]
        m=dict()
        hd=0
        root.hd=hd
        q.append(root)
        while (len(q)):
            root=q[0]
            hd=root.hd
            if hd not in m:
                m[hd]=root.data
            if(root.left):
                root.left.hd=hd-1
                q.append(root.left)
            if(root.right):
                root.right.hd=hd+1
                q.append(root.right)
            q.pop()
        for i in sorted(m):
            print(m[i],end=" ")
if __name__=='__main__':
    root=newNode(1)
    root.left=newNode(2)
    root.right=newNode(3)
    root.left.right=newNode(4)
    root.left.right.right=newNode(5)
    root.left.right.right.right=newNode(6)
    print("The top view of thr tree is:")
    topview(root)
    #this is a python code
    
            
        
    
