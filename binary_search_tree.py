# Import the BinaryTree package.
from BinaryTree import BinaryTree, _Node


class BST:
    def __init__(self):
        '''
        Initialises the root to None and creates instance of Binary Tree modules,
        from the BinaryTree.py file.
        '''
        self.root = None
        self.BT = BinaryTree()

    def insertion_iterative(self, e):
        '''
        Inserts an item into the BST using Iterative Approach
        '''
        temp = None
        tree_root = self.root
        while tree_root:
            temp = tree_root
            if e < tree_root.element:
                tree_root = tree_root.left
            else:
                tree_root = tree_root.right

        if self.root:
            if e < temp.element:
                temp.left = _Node(e)
            else:
                temp.right = _Node(e)
        else:
            self.root = _Node(e)

   
    def search_iterative(self, key):
        '''
        Searches for an item in the BST using Iterative Approach
        '''
        tree_root = self.root
        while tree_root:
            if key == tree_root.element:
                return True
            elif key < tree_root.element:
                tree_root = tree_root.left
            elif key > tree_root.element:
                tree_root = tree_root.right
        return False

   

    def delete(self, key):
        '''
        Deletes an item in the BST
        p  -- reference to the node we want to delete
        pp -- reference to parent node of p
        s  -- reference to the largest element in the left subtree
        ps -- reference to the node we want to delete (temporary)
              later it becomes parent to s node
        c  -- reference to the child node
        '''
        p = self.root
        pp = None

        # Finding the Node we want to delete
        while p and p.element != key:
            pp = p
            if key < p.element:
                p = p.left
            else:
                p = p.right

        # If the Node doesn't exist in the tree.
        if not p:
            return False

        # If the Node has both left and right sub tree.
        if p.left and p.right:
            s = p.left
            ps = p
            # Finds the largest element in the left subtree
            while s.right:
                ps = s
                s = s.right
            p.element = s.element
            p = s
            pp = ps

        # If the node has atmost one child i.e. left child or right child
        # or no child (lead node)
        c = None
        if p.left:
            c = p.left
        else:
            c = p.right

        if p == self.root:
            self.root = None
        else:
            if p == pp.left:
                pp.left = c
            else:
                pp.right = c

        return True

    def inorder(self):
        self.BT.inorder(self.root)


def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Add an item (Iterative)', 'Add multiple items (Iterative)',
                    'Search (Iterative)', 'Delete',
                    'Display BST (Inorder)', 'Exit']
    print("\nMENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')
    choice = int(input("Enter choice: "))
    return choice


def switch_case(choice):
    '''
    Switch Case for operations
    '''
    # os.system('cls')
    if choice == 1:
        elem = int(input("Enter an item: "))
        bst.insertion_iterative(elem)

    elif choice == 2:
        A = list(map(int, input("Enter numbers: ").split()))
        for elem in A:
            bst.insertion_iterative(elem)

    elif choice == 3:
        elem = int(input("Enter an item to search: "))
        print("Found item.") if bst.search_iterative(
            elem) else print("Item does not exist.")

    elif choice == 4:
        elem = int(input("Enter an item to delete: "))
        print("Item Deleted.") if bst.delete(
            elem) else print("Item doesn't exist.")

    elif choice == 5:
        print("Inorder Traversal:")
        bst.inorder()

    elif choice == 6:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    bst = BST()
    while True:
        choice = options()
        switch_case(choice)