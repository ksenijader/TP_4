'''Creating a binary tree'''
# encoding : utf8
class BinaryTree():
    '''Creating class binary tree'''
    def __init__(self):
        '''Defining initial class parametr: root'''
        self.root=None
    def print_tree(self):
        '''Method allowing to build one-sided tree according to node depths'''
        print(self.root.display_node())
    def print_tree_facultatif(self):
        '''Method allowing to build two-sided tree according to node depths'''
        print(self.root.display_node_facultatif())

class Node():
    '''Creating class node'''
    def __init__(self, value):
        '''Defining initial class parametrs: node value and depth.
        Creating empty variables for left and right branches'''
        self.value=value
        self.right= None
        self.left= None
        self.depth= 0

    def add(self, left = None, right = None):
        '''Method allowing to add left or right branch to existing node'''
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        '''Method allowing to update depth of branches'''
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    def display_node(self):
        '''Method allowing to create a one-sided display of the tree'''
        #in varibale "retour" stock information about the node
        retour = str(self)
        #if right branch exists
        if self.right:
            #add to variable "retour" line break
            retour +="\n"
            #add number of tabulation that is equal to nodes depth and repeat the function
            retour +=int(self.right.depth)*"\t" + self.right.display_node()
        #if left branch exists
        if self.left:
            #add to variable "retour" line break
            retour += "\n"
            #add number of tabulation that is equal to nodes depth and repeat the function
            retour +=int(self.left.depth)*"\t" + self.left.display_node()
        return retour

    def display_node_facultatif(self):
        '''Method allowing to create a two-sided display of the tree'''
        #Create an empty str "retour"
        retour =""
        #if both left and right branch exists
        if self.left and self.right:
            #find the max depth of left branch
            max_depth_left=self.left.get_max_depth(0)
            #if the depth of the node is equal to zero(tree root)
            if self.depth==0:
                #shift the node by as many tabulations as the length of left branch
                retour = int(max_depth_left)*"\t"+ str(self)
            retour += "\n"
            #add the number of tabulations which is one smaller than depth of the left branch
            #and separate by two tabulations with the right branch, repeat the function
            retour +=((int(self.left.depth)-1)*"\t" +str(self.left)+
            self.left.display_node_facultatif()
            + 2*"\t"+str(self.right) + self.right.display_node_facultatif())
            retour += "\n"

        else:
            #if right branch exists
            if self.right:
                #and the depth of the current node is 0
                if self.depth==0:
                    #return current node
                    retour=str(self)
                retour += "\n"
                #add number of tabulation that is equal to nodes depth and repeat the function
                retour +=(int(self.right.depth)*"\t" +str(self.right)+
                self.right.display_node_facultatif())
            if self.left:
                if self.depth==0:
                    retour=str(self)
                retour += "\n"
                #add number of tabulation that is bigger by one to nodes
                #depth and repeat the function
                retour +=((int(self.left.depth)+1)*"\t" +str(self.left)+
                self.left.display_node_facultatif())

        return retour



    def __str__(self):
        '''Module defining character string'''
        return str(self.value) + "/" + str(self.depth)

    def is_leaf(self):
        '''Module returning leaf value'''
        #return self.left == None and self.right == None
        return not(self.left or self.right)

    def get_max_depth(self,max_depth=0):
        '''Module finding branches depth'''
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            return max_depth
        # je suis le node d'un arbre

        if self.right:
            max_depth = self.right.get_max_depth(max_depth)

        if self.left:
            max_depth = self.left.get_max_depth(max_depth)
        return max_depth

if __name__=="__main__":
    node1 = Node(0)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node3.add(node4)
    node1.add(node2, node3)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node5.add(node6, node7)
    node4.add(node5)
    node8 = Node(8)
    node7.add(node8)

    tree1=BinaryTree()
    tree1.root=node1
    tree1.print_tree()
    print("\n***********************************************************\n")
    tree1.print_tree_facultatif()
