# How to use
To launch the script type python tree.py in terminal
This will return two types of trees.

## Method explanation

Node class takes two parametres: value and depth. If depth is not specified it's default value is zero.
To add nodes to already existing nodes use *node_name*.add(*left_node*,*right_node*). 
Default value of left and right node is *None*.
Depth of the added nodes will be calculed by adding 1 to their "mother" node's depth value.

BinaryTree class takes an object of Node class as root.
It can return either a "one sided tree" by using *tree_name*.print_tree() method or binary tree using *tree_name*.print_tree_facultatif() method.