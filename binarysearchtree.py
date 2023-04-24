# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Juan Brasdefer 225936, Fabian Pawelczyk 226921
"""
from mlbt import MutableLinkedBinaryTree

class MutableLinkedBinarySearchTree(MutableLinkedBinaryTree):
    
    def __init__(self):
        super().__init__()
        
    def add(self, value):
        """Add a new value to the binary search tree."""
        if self.is_empty():
            self.add_root(value)
        else:
            self._subtree_add(self.root(), value)
            
    def _subtree_add(self, p, value):
        """Add a new value to the subtree rooted at Position p."""
        if value < p.element():
            if self.left(p) is None:
                self.add_left(p, value)
            else:
                self._subtree_add(self.left(p), value)
        else:
            if self.right(p) is None:
                self.add_right(p, value)
            else:
                self._subtree_add(self.right(p), value)
                
                
def convert_to_bst(lbt):
    # Create a new binary search tree instance
    bst = MutableLinkedBinarySearchTree()

    # Iterate over the positions in the mutable linked tree and add each element to the binary search tree
    for position in lbt.inorder():
        bst.add(position.element())

    return bst