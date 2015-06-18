'''
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit of how you deserialize or serialize a binary tree, you only need to make sure you can serialize a binary tree to a string and deserialize this string to the original structure.

Have you met this question in a real interview? Yes
Example
An example of testdata: Binary tree {3,9,20,#,#,15,7}, denote the following structure:

  3
 / \
9  20
  /  \
 15   7
Our data serialization use bfs traversal. This is just for when you got wrong answer and want to debug the input.

You can use other method to do serializaiton and deserialization.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:

    def __init__(self):
        self.index = 0
    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        result = []
        if not root: return 
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node != -1:
                result.append(str(node.val))
                
                if node.right:
                    stack.append(node.right)
                elif not node.right:
                    stack.append(-1)
                    
                if node.left:
                    stack.append(node.left)
                elif not node.left:
                    stack.append(-1)
            else:
                result.append(str(node))
        
        return result
        
    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        if not data: return None
        return self.deserialize_helper(data)

    def deserialize_helper(self, data):
        if data[self.index] == '-1':
            return None

        value = int(data[self.index])
        node = TreeNode(value)
        self.index += 1
        node.left = self.deserialize_helper(data)
        self.index += 1
        node.right = self.deserialize_helper(data)
        return node
            
        
        
        
        
        
        
