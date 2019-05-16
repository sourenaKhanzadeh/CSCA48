class BTNode:
    def __init__(self, left=None, right=None):
        """ (BTNode, BTNode, BTNode) -> NoneType
        Initialize a new BTNode with pointers to subtrees left and right.
        """
        self.left = left
        self.right = right


def weird_version(s):
    """ (str) -> str
    Return a weird version of string s.
    """
    if len(s) < 2:
        return s
    else:
        return s[1] + weird_version(s[2:]) + s[0]


def sum_depths(root):
    return sum_depths_helper(root, 0)


def sum_depths_helper(root, n):
    """
    """

    if root:
        res = n + sum_depths_helper(root.right, n+1) + sum_depths_helper(root.left, n+1)

    else:
        res = 0

    return res

if __name__ == "__main__":
    l = BTNode(BTNode(BTNode()), BTNode(BTNode(BTNode(BTNode(BTNode(BTNode(BTNode())))))))
    x = sum_depths(l)
    print(x)
    # print(weird_version("A48WEIRD"))
    # print(weird_version("ABC12345DEF"))
