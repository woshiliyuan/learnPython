# coding=utf-8
from typing import List


# ------------------   二叉树 start         -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None


# 层序遍历构建二叉树
def init__binary_tree(data: List):
    if not data:
        return None

    root = TreeNode(data[0])
    queue, index = [root], 1

    while index < len(data):
        node = queue.pop(0)
        for dir in ['left', 'right']:
            next_node = None
            if index < len(data) and data[index] is not None:
                next_node = TreeNode(data[index])
                queue.append(next_node)
            index += 1
            setattr(node, dir, next_node)
    return root


def visit_tree_pre(root: TreeNode):
    def visit(node: TreeNode):
        if node is None:
            return

        answer.append(node.val)
        visit(node.left)
        visit(node.right)

    answer = []
    visit(root)
    return answer


def levelOrder(root: TreeNode) -> List:
    answer, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            answer.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            answer.append(None)
    # 去掉尾巴的连续None
    for i in range(len(answer) - 1, -1, -1):
        if answer[i] is None:
            answer.pop()
        else:
            break
    return answer



def get_node(root: TreeNode, value) -> TreeNode:
    def visit(node: TreeNode):
        nonlocal value_node
        if node is None or value_node:
            return
        if node.val == value:
            value_node = node
            return

        visit(node.left)
        visit(node.right)

    value_node = None
    visit(root)
    return value_node

# ------------------   二叉树 end         -------------------------------


# --------------       正常树  start      ---------------------------
class Node:
    # 为什么这么构造函数就会错呢，假设有n个节点，所有节点的children都是n个；百思不得其解呀
    # def __init__(self, val=None, children=[]):
    #     self.val = val
    #     self.children = children
        # print("init", len(children), children)

    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = []


def init_tree(values: List):
    if not values:
        return None

    root = Node(values[0])
    queue, index = [root], 1

    node = None
    while index < len(values):
        if values[index] is None:
            node = queue.pop(0)
        else:
            son_node = Node(values[index])
            node.children.append(son_node)
            queue.append(son_node)
        index += 1

    return root

# --------------       正常多叉树 end        ---------------------------



if __name__ == "__main__":
    values = [1, None, 0, 3]
    root = init__binary_tree(values)
    print(visit_tree_pre(root))
    print(get_node(root, 3).val)

    # values = [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, 10, None, None, 11]
    # root = init__binary_tree(values)
    # equals_array(visit_tree_pre(root), [1, 2, 4, 8, 9, 5, 3, 6, 10, 7, 11])
    #
    # values = [1, 2, 3, 4, None, None, 5, None, 6, 7, None, 8, None, 9]
    # root = init__binary_tree(values)
    # equals_array(visit_tree_pre(root), [1, 2, 4, 6, 8, 3, 5, 7, 9])




