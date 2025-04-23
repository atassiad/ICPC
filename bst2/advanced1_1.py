from collections import deque

def problem1():
    class Puff():
        def __init__(self, flavor, left=None, right=None):
            self.val = flavor
            self.left = left
            self.right = right

    def listify_design(design):
        if (not design):
            return []

        #queue of nodes
        nodeQueue = deque()
        nodeQueue.append(design)

        #answer list 
        returnList = []

        while (nodeQueue):
            #queuecopy
            subList = []
            queueLen = len(nodeQueue)
            #exhaust copy queue
            for i in range(queueLen):
                curNode = nodeQueue.popleft()
                if (curNode.left):
                    nodeQueue.append(curNode.left)
                if (curNode.right):
                    nodeQueue.append(curNode.right)
                subList.extend([curNode.val])
            
            #add to returnlist
            returnList.append(subList)
        
        return returnList




    croquembouche = Puff("Vanilla", 
                        Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                        Puff("Strawberry"))
    croquembouche1 = Puff("Vanilla")
    croquembouche2 = Puff("Vanilla", 
                        Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                        Puff("Strawberry", Puff("Grass"), Puff("Whole Wheat")))
    print(listify_design(croquembouche))
    print(listify_design(croquembouche1))
    print(listify_design(croquembouche2))

def problem2():
    class TreeNode():
        def __init__(self, flavor, left=None, right=None):
            self.val = flavor
            self.left = left
            self.right = right

    def build_tree(values):
        if not values:
            return None

        def get_key_value(item):
            if isinstance(item, tuple):
                return item[0], item[1]
            else:
                return None, item

        key, value = get_key_value(values[0])
        root = TreeNode(value, key)
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if index < len(values) and values[index] is not None:
                left_key, left_value = get_key_value(values[index])
                node.left = TreeNode(left_value, left_key)
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index] is not None:
                right_key, right_value = get_key_value(values[index])
                node.right = TreeNode(right_value, right_key)
                queue.append(node.right)
            index += 1

        return root

    def zigzag_icing_order(cupcakes):
        if (not cupcakes):
            return []
        
        #setup queue
        queue = deque()
        queue.append(cupcakes)

        #Setup bool and result
        orderBool = False
        res = []
        while (queue):
            queueLen = len(queue)

            print(res)
            subList = deque()
            for i in range(queueLen):
                curNode = queue.popleft()
                if (curNode.left):
                    subList.appendleft(curNode.left)
                if (curNode.right):
                    subList.appendleft(curNode.right) 
                
                res.append(curNode.val)

            if (subList):
                queue.extend(subList)
            orderBool = 1 - orderBool

        return res
        # hazelnut, redvelvet, strawberry
        #Chocolate
        # Vanilla, Lemon
        # Vanilla, Hazelnut, Red Velvet

    flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
    cupcakes = build_tree(flavors)
    print(zigzag_icing_order(cupcakes))
problem2()