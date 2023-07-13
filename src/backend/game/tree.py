class TreeNode:

    def __init__(self, value, content):
        self.left = None
        self.right = None
        self.content = content
        self.value = value

    def tree(self, value, content):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value=value, content=content)
                self.left.content = content
            else:
                self.left.tree(value=value, content=content)
                print(self.value, self.content)
        else:
            if self.right is None:
                self.right = TreeNode(value=value, content=content)
                self.right.content = content
            else:
                self.right.tree(value=value, content=content)