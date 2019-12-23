class Node(object):
    """the node of binary tree"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    """binary tree"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)       # 构造节点
        if self.root is None:   # 特殊情况，如果根节点就是None，则直接将新节点挂载到根节点上
            self.root = node
            return

        # 使用广度优先遍历，也叫层次遍历找到None节点以供插入
        queue = [self.root]     # 1.构造空队列，并先将根节点加入

        # 2.如果节点不为None，则append入队列，如果为None，则直接将新节点挂上
        while True:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            queue.append(cur_node.rchild)

    def breadth_first_search(self):
        """
        广度优先遍历，也叫层次遍历
        :return: res of search
        """
        # 定义一个队列，把根节点先加入
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """
        前序遍历
        :param node: 待遍历树的根节点
        :return: 遍历的结果
        """
        if node == None:
            return
        print(node.elem, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """
        中序遍历
        :param node: 待遍历树的根节点
        :return: 遍历的结果
        """
        if node == None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=' ')
        self.inorder(node.rchild)

    def post_order(self, node):
        """
        后序遍历
        :param node: 待遍历树的根节点
        :return: 遍历的结果
        """
        if node == None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem, end=' ')


if __name__ == "__main__":
    tree = BinaryTree()
    for i in range(10):
        tree.add(i)
    tree.breadth_first_search()

    print()
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.post_order(tree.root)




















