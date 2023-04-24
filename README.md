[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/L0P4fZaj)

# Documentation:
This Modular Code makes use of a classical "Tree" template and a "Binary Tree" template to add the feature of BinarySearch, which turns the original Binary Tree into a sorted version of itself, where:
1) The value of the left child of any node is lesser than the value of the node itself
2) The value of the right child of any node is greater than the value of the node itself

Binary Search Trees allow for quicker searching of node value than the standard Binary Trees, which means, by extension, that insertion and deletion are quicker as well.

In order to turn a BinaryTree into a BinarySearchTree, this code uses the following logic:
1) Perform an in-order (TraverseLeft, VisitNode, TraverseRight) traversal of the binary tree and store the values of the visited nodes in a list
2) Sort the list
3) Take the sorted list and use it to build a new (sorted) binary search tree :))






# Assignment:

Write a program that converts a binary tree into a binary search tree. I will not tell you the steps for how to do this, you will need to figure out the algorithm. However, here are some hints:

* What is the main difference between a binary search tree and a binary tree?
* What could be the middle step between a binary tree and a binary search tree?

You should start with a regular binary tree, using the code from the Binary Tree Assignment. Create a tree and then convert it to a binary search tree.
* Make your code *modular*!
* Respect code blocks and line spaces, naming conventions.
* Document (but do not leave comments)
* Do exactly what is asked. There will be no points for *Above and Beyond* this assignment.
* List your group's members in the header of the main file.
