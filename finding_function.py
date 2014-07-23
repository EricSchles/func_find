import random


class Node:
    def __init__(self,item,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right
    def __str__(self):
        return repr(self.item)

def traverse(node):
    if node.left != None:
        traverse(node.left)
    print node
    if node.right != None:
        traverse(node.right)

def add(a,b):
    return a+b

def mult(a,b):
    return a*b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def generate_primitives():
    list_of_primitives[add,mult,sub,div,'x','y',0,1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
    return list_of_primitives


def func_create(root,size,list_of_primitives):
    counter = 0
    curr = root
    for i in xrange(size):
        left_item = list_of_primitives[random.randint(0,len(list_of_primitives))]
        right_item = list_of_primitives[random.randint(0,len(list_of_primitives))]
        curr_left = Node(left_item,None,None)
        curr_right = Node(right_item,None,None)
        curr.left = curr_left
        curr.right = curr_right
        if counter % 2 == 0:
            curr = curr.left
        else:
            curr = curr.right
        counter += 1
    return root


if __name__ == '__main__':
    list_of_primitives = generate_primitives()
    root = Node(0,None,None)
    root = func_create(node,len(list_of_primitives),list_of_primitives)
    traverse(root)
