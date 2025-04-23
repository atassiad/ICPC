def problem1():
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def survey_tree(root):
        if not root:
            return []
        
        res = []
        if root.left:
            res.extend(survey_tree(root.left))
        
        if root.right:
            res.extend(survey_tree(root.right))
        
        res.append(root.val)
        return res
        



    magnolia = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")), TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

    print(survey_tree(magnolia))

def problem2():
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def sum_inventory(inventory):
        if not inventory:
            return 0
        
        res_value = 0
        if inventory.left:
            res_value += sum_inventory(inventory.left)
        
        if inventory.right:
            res_value += sum_inventory(inventory.right)
        
        res_value += inventory.val
        return res_value


    inventory = TreeNode(40, 
                        TreeNode(5, TreeNode(20)),
                                TreeNode(10, TreeNode(1), TreeNode(30)))

    print(sum_inventory(inventory))
problem2()

def problem3():
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def count_old_growth(root, threshold):
        if not root:
            return 0
        
        rolling_sum = 0

        if root.left:
            rolling_sum += count_old_growth(root.left, threshold)
        
        if root.right:
            rolling_sum += count_old_growth(root.right, threshold)
        
        if (root.val > threshold):
            rolling_sum += 1

        return rolling_sum


    forest = TreeNode(100, 
                    TreeNode(1200, TreeNode(20)),
                            TreeNode(1500, TreeNode(700), TreeNode(2600)))

    print(count_old_growth(forest, 1000))

def problem4():
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def is_identical(root1, root2):
        if not root1 and not root2:
            return True
        
        bool1 = True
        bool2 = True

        if root1.left and root2.left:
            bool1 = is_identical(root1.left, root2.left)
        elif root1.left or root2.left:
            return False

        if root1.right and root2.right:
            bool2 = is_identical(root1.right, root2.right)
        elif root1.right or root2.right:
            return False

        if (root1.val == root2.val):
            return bool1 and bool2
        return False
    
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    root3 = TreeNode(1, TreeNode(2))
    root4 = TreeNode(1, None, TreeNode(2))

    print(is_identical(root1, root2))
    print(is_identical(root3, root4))

problem4()