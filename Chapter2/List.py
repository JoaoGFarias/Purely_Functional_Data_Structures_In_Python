import copy

def head(list):
    return list[0]
def tail(list):
    return list[1:]


def concat(list1,list2):
    if list1 == []:
        return list2
    else:
        return [copy.deepcopy(head(list1))] + (concat(tail(list1),list2))
    

def update(list,pos,value):
    if list == []:
        raise IndexError
    if pos == 0:
        return [value] + tail(list)
    else:
        return [copy.deepcopy(head(list))] + (update(tail(list),pos-1,value))
    
def test():
    class TestClass:
        pass

    testObj1 = TestClass()
    testObj1.u = TestClass()
    testObj2 = TestClass()
    testObj2.i = TestClass()
    
    list = concat([testObj1],[testObj2])
    assert id(testObj1) != id(list[0]) #Asserting that the objects are not the same
    assert id(testObj1.u) != id(list[0].u) #Asserting that the attributes were copied

    oldList = [testObj1,15,80]
    newList = update(oldList,1,99)
    assert id(oldList) != id(newList) #Asserting that the lists are not the same
    assert oldList[0] == testObj1 #Asserting that old list were not modified
    assert newList[1] == 99 #Asserting correct update

if __name__ == "__main__":
    test()
    pass
