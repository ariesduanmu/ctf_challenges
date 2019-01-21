# -*- coding: utf-8 -*-
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.parent = None
        self.used = False

class Bin_Tree():
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.val:
            left = self.insert(root.left, key)
            if left:
                left.parent = root
            root.left = left
        else:
            right = self.insert(root.right, key)
            if right:
                right.parent = root
            root.right = right

        return self.balance_tree(root, key)
    
    # TODO: UNFINISHED
    def search(self, root, key):
        if root.val < key and root.left is None and root.right is None:
            return None

        if key < root.val:
            return self.search(root.left, key)
        elif key > root.val:
            return self.search(root.right, key)

    def delete(self, root, key):
        
        if key < root.val:
            left = self.delete(root.left, key)
            if left:
                left.parent = root
            root.left = left
        elif key > root.val:
            right = self.delete(root.right, key)
            if right:
                right.parent = root
            root.right = right
        else:
            if root.left and root.right:
                succ = self.findMin(root.right)
                if succ.parent.left == succ:
                    succ.parent.left = succ.right
                else:
                    succ.parent.right = succ.right
                if succ.right:
                    succ.right.parent = succ.parent

                succ.left = root.left
                if root.left:
                    root.left.parent = succ
                succ.right = root.right
                if root.right:
                    root.right.parent = succ
                return self.balance_tree(succ, key)

            else:
                if root.left:
                    return self.balance_tree(root.left, key)
                else:
                    return self.balance_tree(root.right, key)

        return self.balance_tree(root, key)

    def balance_tree(self, root, key):
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root


    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        if z:
            z.parent = y
        z.right = T2
        if T2:
            T2.parent = z

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        if z:
            z.parent = y
        z.left = T3
        if T3:
            T3.parent = z

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def findMin(self, succ):
        if succ.left:
            return self.findMin(succ.left)
        else:
            return succ

    def preOrder(self, root):
        if not root:
            return

        print(f"{root.val} ", end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

if __name__ == "__main__":
    tree = Bin_Tree()
    root = None

    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    root = tree.insert(root, 30)
    root = tree.insert(root, 40)
    root = tree.insert(root, 50)
    root = tree.insert(root, 25)
    root = tree.insert(root, 20)
    root = tree.insert(root, 30)
    root = tree.insert(root, 40)
    root = tree.insert(root, 50)
    root = tree.insert(root, 25)

    tree.preOrder(root)
    print()

    root = tree.delete(root, 40)
    root = tree.delete(root, 20)
    tree.preOrder(root)
    print()


