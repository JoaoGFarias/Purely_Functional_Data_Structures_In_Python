import abc
import copy

class Node:
    """Abstract data type for tree node"""
    @abc.abstractmethod
    def __init__(self):
        return

    @abc.abstractmethod
    def isEmpty(self):
        return
    
    @abc.abstractmethod
    def insert(self,val):
        return

    @abc.abstractmethod
    def member(self,val):
        return

class EmptyNode(Node):

    def isEmpty(self):
        return True

    def insert(self,val):
        return Elem(EmptyNode(),val,EmptyNode()) #Node with left and right None
    
    def member(self,val):
        return False

class Elem(Node):

    def __init__(self,left,val,right):
        self.val = val
        self.left = left
        self.right = right
        pass

    def isEmpty(self):
        return False

    def insert(self,val):
        if self.val > val:
            return Elem(self.left.insert(val),copy.deepcopy(self.val),self.right) #The right branch is shared
        elif self.val < val:
            return Elem(self.left,copy.deepcopy(self.val),self.right.insert(val)) 
        else:
            return self

    def member(self,val):
        if self.val > val:
            return self.left.member(val)
        elif self.val < val:
            return self.right.member(val)
        else:
            return True

def listTree(): #A tree, but actually is a list starting with 1, the tree root, till 9, the rightmost node
    tree = EmptyNode()
    for i in range(1,10):
        tree = tree.insert(i)
    assert tree.val == 1
    assert tree.right.val == 2
    return tree

def test():
    #Asserting tree properties
    tree = listTree()
    newTree = tree.insert(-1)
    assert newTree.left.val == -1
    assert newTree.member(5)
    assert not newTree.member(90)
    assert not tree.member(-1) and newTree.member(-1) #The old tree a not modified

    #Asserting persistence
    tree = EmptyNode().insert([1]).insert([2]).insert([0])
    newTree = tree.insert([50]) #Here, the insert function creates new nodes during the recursion
    assert tree.val == newTree.val
    assert not id(newTree.val) == id(tree.val)
    pass

if __name__ == "__main__":
    test()
