# -*- coding: utf-8 -*-
from collections import Counter

class BinaryTreeNode():
    def __init__(self, value = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class HuffmanTreeNode(BinaryTreeNode):
    def __init__(self, weight, value = None, left=None, right=None):
        BinaryTreeNode.__init__(self, value, left, right)
        self.weight = weight

class HuffmanTree():
    def __init__(self, root = None):
        self.root = root

    def parse(self, c):
        s = sorted([[c[k], HuffmanTreeNode(c[k], k)] for k in c], key=lambda x:x[0])

        while len(s) > 1:
            wl, nl = s[0]
            wr, nr = s[1]
            s = s[2:] + [[wl+wr, HuffmanTreeNode(wl+wr, None, nl, nr)]]
            s.sort(key=lambda x:x[0])
        self.root = s[0][1]


def main(context):
    c = Counter(context)
    tree = HuffmanTree()
    tree.parse(c)

if __name__ == "__main__":
    main("aaabbbcdef")

