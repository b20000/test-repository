
class BinaryTree(object):
    
    def __init__(self):
        pass
    
    def BinaryTree(self,r):
        return [r, [], []]
    
    def insertLeft(self,root,newBranch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1,[newBranch,t,[]])
        else:
            root.insert(1,[newBranch, [], []])
        return root

    def insertRight(self,root,newBranch):
        t = root.pop(2)
        if len(t) > 1:
            root.insert(2,[newBranch,[],t])
        else:
            root.insert(2,[newBranch,[],[]])
        return root

    def getRootVal(self,root):
        return root[0]

    def setRootVal(slef,root,newVal):
        root[0] = newVal

    def getLeftChild(self,root):
        return root[1]

    def getRightChild(self,root):
        return root[2]
    
if __name__ == '__main__':
    
    pass