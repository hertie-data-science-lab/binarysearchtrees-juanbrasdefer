# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Juan Brasdefer 225936, Fabian Pawelczyk 226921
"""

from mlbt import MutableLinkedBinaryTree

lbt = MutableLinkedBinaryTree()

print(len(lbt))
print(lbt.root())

lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)


# Inorder Traversal
print("Inorder Traversal lbt:")
for node in lbt.inorder():
    print(node.element(), end=" ")
print()



from binarysearchtree import convert_to_bst

bst = convert_to_bst(lbt)

# Inorder Traversal
print("Inorder Traversal sbt:")
for node in bst.inorder():
    print(node.element(), end=" ")
print()





