import sys
class _Node:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        '''
        Initialises Root node to None.
        '''
        self.root = None



    def createTree(self, node):
        '''
        Recursively adds node to the tree using Postorder traversing pattern.
        That means, it will first ask to add all the left childs of root
        and then right child of the most recently added node.
        '''
        position = input(
            f"Add node on the Left of {node.element} ? [y/n]: ")
        if position == 'y':
            nodeData = input("Enter data for node: ")
            curr = _Node(nodeData)
            node.left = curr
            self.createTree(curr)
     
        position = input(
            f"Add node on the Right of {node.element} ? [y/n]: ")
        if position == 'y':
            nodeData = input("Enter data for node: ")
            curr = _Node(nodeData)
            node.right = curr
            self.createTree(curr)
     
    def createRoot(self):
        '''
        Function to create Root node.
        '''
        rootData = input("Enter data for Root: ")
        self.root = _Node(rootData)
        self.createTree(self.root)
 
    def inorder(self, tree_root):
        '''
        Function for Inorder Traversal.
        '''
        if tree_root:
            self.inorder(tree_root.left)
            print(tree_root.element, " ")
            self.inorder(tree_root.right)

    def preorder(self, tree_root):
        '''
        Function for Preorder Traversal.
        '''
        if tree_root:
            print(tree_root.element, " ")
            self.preorder(tree_root.left)
            self.preorder(tree_root.right)

    def postorder(self, tree_root):
        '''
        Function for Postorder Traversal.
        '''
        if tree_root:
            self.postorder(tree_root.left)
            self.postorder(tree_root.right)
            print(tree_root.element, " ")


    def height(self, tree_root):
        '''
        Utility function to calculate height of the tree.
        '''
        if tree_root:
            x = self.height(tree_root.left)
            y = self.height(tree_root.right)

            if x > y:
                return x + 1
            else:
                return y + 1

        return 0

###############################################################################


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Create Tree', 'Inorder', 'Preorder',
                    'Postorder',
                    'Height', 'Exit']

    print("\nMENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice = int(input("Enter choice: "))
    return choice


def switch_case(choice):
    '''
    Switch Case for operations
    '''
    if choice == 1:
        bt.createRoot()

    elif choice == 2:
        print("Inorder Traversal:")
        bt.inorder(bt.root)

    elif choice == 3:
        print("Preorder Traversal:")
        bt.preorder(bt.root)

    elif choice == 4:
        print("Postorder Traversal:")
        bt.postorder(bt.root)
    
    elif choice == 5:
        print("Height: ", bt.height(bt.root) - 1)

    else:
        sys.exit()
###############################################################################


if __name__ == '__main__':
    bt = BinaryTree()
    while True:
        choice = options()
        switch_case(choice)
