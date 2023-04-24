# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:16:50 2023

@author: Juan Brasdefer 225936, Fabian Pawelczyk 226921
"""

#this is a copy-paste of the old binarytree.py with some added flare :))
#more explanation can be found in the README file


from treetemplate import Tree
from abc import ABC, abstractmethod

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""
    
    @abstractmethod
    def left(self, p):
        """Return a Position representing p's left child.
        
        Return None if p does not have a left child.
        """
        pass
    
    @abstractmethod
    def right(self, p):
        """Return a Position representing p's right child.
        
        Return None if p does not have a right child.
        """
        pass
    
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
            
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        
        if self.right(p) is not None:
            yield self.right(p)









    #Below is the new code for binary search tree
    def inorder_traversal(self, p):
        """Perform an in-order traversal of the subtree rooted at Position p."""
        if p is not None:
            for value in self.inorder_traversal(self.left(p)):
                yield value
            yield p.element()
            for value in self.inorder_traversal(self.right(p)):
                yield value
                


    def build_bst(self, values):
        """Build a binary search tree using the given list of values."""
        values = sorted(values)
        mid = len(values) // 2
        root = self._add_root(values[mid])
        self._build_bst(root, values[:mid])
        self._build_bst(root, values[mid + 1:])
        return root
    


    def _build_bst(self, parent, values):
        """Recursively build a binary search tree using the given list of values."""
        if not values:
            return
        mid = len(values) // 2
        child = self._add_left(parent, values[mid])
        self._build_bst(child, values[:mid])
        self._build_bst(child, values[mid + 1:])