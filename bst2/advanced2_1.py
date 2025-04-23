from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


def problem1():
    class TreeNode:
        def __init__(self, flavor, left=None, right=None):
            self.val = flavor
            self.left = left
            self.right = right

    def build_cookie_tree(descriptions):
        # use dictionary to reference tree nodes
        # if third param is 1, put on left, if 0 put on right
        # if descriptions is empty return None

        if not descriptions:
            return None
        
        #Create dictionary to reference nodes
        cookies = dict()

        #iterate through descriptions
        for description in descriptions:
            childNode = TreeNode(description[1])
            cookies[description[1]] = childNode

            if description[0] in cookies:
                curNode = cookies[description[0]]
                if (description[2] == 1):
                    curNode.left = childNode
                else:
                    curNode.right = childNode
            else:
                curNode = TreeNode(description[0])
                cookies[description[0]] = curNode
                if (description[2] == 1):
                    curNode.left = childNode
                else:
                    curNode.right = childNode
        
        return cookies[descriptions[0][0]]

    descriptions1 = [
        ["Chocolate Chip", "Peanut Butter", 1],
        ["Chocolate Chip", "Oatmeal Raisin", 0],
        ["Peanut Butter", "Sugar", 1]
    ]

    descriptions2 = [
        ["Ginger Snap", "Snickerdoodle", 0],
        ["Ginger Snap", "Shortbread", 1]
    ]

    # Using print_tree() function included at top of page
    print_tree(build_cookie_tree(descriptions1))
    print_tree(build_cookie_tree(descriptions2))

def problem2():
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def most_popular_cookie_combo(root):
        #postorder traversal, propogate values up tree
        # add to a frequency map for each count
        # if none return 0
        
        # check if root exists
        return_list = []
        total_freq = dict()

        if not root:
            return return_list
        
        def helper(root):
            pass


    """
        5
        / \
        2  -3
    """
    cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))

    """
        5
        / \
        2  -5
    """
    cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

    print(most_popular_cookie_combo(cookies1))  
    print(most_popular_cookie_combo(cookies2))  
problem2()