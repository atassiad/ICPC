from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
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



def problem1():
    def sort_plants(collection):
        # Inorder traversal, recursivelly, that should get us our values in sorted order
        return_list = []

        def help_sort_plants(ptr):
            if (not ptr):
                return
            
            
            help_sort_plants(ptr.left)

            return_list.append((ptr.key, ptr.val))

            help_sort_plants(ptr.right)

            return
        help_sort_plants(collection)
        return return_list

    values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
    collection = build_tree(values)

    print(sort_plants(collection))

def problem2():
    def find_flower(inventory, name):
        # Do normal binary search down tree
        pass
    values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
    garden = build_tree(values)

    print(find_flower(garden, "Lilac"))  
    print(find_flower(garden, "Sunflower")) 
problem2()