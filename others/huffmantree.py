# -*- coding: utf-8 -*-
from collections import Counter

class BinaryTreeNode():
    def __init__(self, value = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def isLeaf(self):
        return self.left is None and self.right is None

class HuffmanTreeNode(BinaryTreeNode):
    def __init__(self, weight, value = None, left=None, right=None):
        BinaryTreeNode.__init__(self, value, left, right)
        self.weight = weight

    def compareTo(other_node):
        return self.weight - other_node.weight
  
def buildTrie(data):
    '''
    Build Huffman Tree
    '''
    c = Counter(data)
    s = sorted([[c[k], HuffmanTreeNode(c[k], k)] for k in c], key=lambda x:x[0])
    while len(s) > 1:
        wl, nl = s[0]
        wr, nr = s[1]
        s = s[2:] + [[wl+wr, HuffmanTreeNode(wl+wr, None, nl, nr)]]
        s.sort(key=lambda x:x[0])
    return s[0][1]

def build_info(root):
    '''
    Get Huffman Tree code to string
    Example:
        {'A': '0', 
         '!': '100', 
         'B': '101', 
         'R': '110', 
         'C': '1110', 
         'D': '1111'}

    Args:
        root: Huffman Tree root
    '''
    builder = {}
    build_code(builder, root, "")
    return builder

def build_code(builder, node, s):
    if node.isLeaf:
        builder[node.value] = s
        return
    build_code(builder, node.left, s+"0")
    build_code(builder, node.right, s+"1")


def expand(root, data):
    '''
    Expand compressed data
    Args:
        root: Huffman Tree root
        data: data to be compressed
    '''
    result = ""
    i = 0
    while i < len(data):
        n = root
        while not n.isLeaf:
            if data[i] == "1":
                n = n.right
            else:
                n = n.left
            i += 1
        result += n.value
    return result

def compress(data):
    '''
    Compress data
    Args:
        root: Huffman Tree root
        data: data to be compressed
    '''
    root = buildTrie(data)
    builder = build_info(root)
    return "".join(builder[d] for d in data), root

def main():
    text  = "it was the age of foolishness"
    print(f"[*] Input: {text}")
    print(f"[*] Before compress: {len(text)*8} bits")
    print(f"compressing...")   
    # Compress Data
    compressed, root = compress(text)
    # Expand Data
    expanded = expand(root, compressed)
    
    print(f"[*] Output: {compressed}")
    print(f"[*] After compress: {len(compressed)} bits")
    print(f"[*] Compress rate: {int(len(compressed) / (len(text)*8) * 100)}%")
    # print(text == expanded)

if __name__ == "__main__":
    main()

