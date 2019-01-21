from typing import NamedTuple
from collections import deque

class CornerPoint(NamedTuple):
    """
    namedtuple representing the top left corner of each
    BinTree object.
    """
    x: int
    y: int


class Item(NamedTuple):
    """
    namedtuple representing objects added to BinTree.
    """
    width: int
    height: int


class BinTree:
    """
    Each BinTree instance has two children (left and bottom)
    and width (int), height (int), and occupied (bool) properties.
    """
    def __init__(self, dims: tuple = (4, 8)) -> None:
        self.corner = CornerPoint(0, 0)
        self.dims = dims
        self.occupied = False
        self.parent = None
        self.right = None
        self.bottom = None
        if not self.occupied:
            self.largest_child = tuple(self.dims)
        else:
            self.largest_child = None


    def _check_dim(item_dim: int, bin_dim: int) -> bool:
        """
        Checks if the item will fit the bin in the specified
        dimension.
        """
        pass


    def insert(self, item: Item) -> bool:
        """
        Recursive item insertion
        Takes an Item namedtuple
        Inserts recursively as a side-effect
        Returns True or False if Item fit in bin
        """
        if not self.occupied and item.width <= self.dims[0] and item.height <= self.dims[1]:
            if self.dims[1] - item.height > 0:
                self.bottom = BinTree(dims=[self.dims[0], self.dims[1]-item.height])
                self.bottom.parent = self
            if self.dims[0] - item.width > 0:
                self.right = BinTree(dims=[self.dims[0]-item.width, item.height])
                self.right.parent = self
            self.dims = (item.width, item.height)
            self.occupied = item
            if self.right:
                self.right.corner = CornerPoint(self.dims[0] + self.corner.x, self.corner.y)
            if self.bottom:
                self.bottom.corner = CornerPoint(self.corner.x, self.dims[1] + self.corner.y)
            self.calc_largest_child()
            return True
        else:
            if (self.right and self.right.largest_child[0] >= item.width and
                    self.right.largest_child[1] >= item.height):
                self.right.insert(item)
            elif (self.bottom and self.bottom.largest_child[0] >= item.width and
                  self.bottom.largest_child[1] >= item.height):
                self.bottom.insert(item)
            else:
                return False


    def calc_largest_child(self) -> None:
        """
        Updates self.largest_child for each node recursively
        back to the root node
        """
        choices = []
        if not self.occupied:
            choices.append(self.dims)
        else:
            choices.append((0, 0))
        if self.right:
            choices.append(self.right.largest_child)
        else:
            choices.append((0, 0))
        if self.bottom:
            choices.append(self.bottom.largest_child)
        else:
            choices.append((0, 0))
        self.largest_child = max(choices, key=lambda t: t[0]*t[1])

        if self.parent:
            self.parent.calc_largest_child()


def bin_stats(root: BinTree) -> dict:
    """
    Returns a dictionary with compiled stats on the bin tree
    """
    stats = {
                'width': 0,
                'height': 0,
                'area': 0,
                'efficiency': 1.0,
                'items': [],
            }

    stack = deque([root])
    while stack:
        node = stack.popleft()
        stats['width'] += node.dims[0]
        if node.right:
            stack.append(node.right)

    stack = deque([root])
    while stack:
        node = stack.popleft()
        stats['height'] += node.dims[1]
        if node.bottom:
            stack.append(node.bottom)

    stats['area'] = stats['width'] * stats['height']

    stack = deque([root])
    occupied = 0
    while stack:
        node = stack.popleft()
        if node.occupied:
            stats['items'].append((node.corner, node.occupied))
            occupied += node.dims[0]*node.dims[1]

        if node.right:
            stack.append(node.right)
        if node.bottom:
            stack.append(node.bottom)
    stats['efficiency'] = occupied / stats['area']
    return stats