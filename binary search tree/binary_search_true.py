# https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-2-binary-search-nodes-traversals-and-balancing


class nodeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def parse_tuple_to_node(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = nodeNode(data[1])
        node.left = parse_tuple_to_node(data[0])
        node.right = parse_tuple_to_node(data[2])
    elif data is None:
        node = None
    else:
        node = nodeNode(data)
    return node


def parse_node_to_tuple(node):
    if node and (node.right or node.left):
        return (parse_node_to_tuple(node.left), node.key, parse_node_to_tuple(node.right))
    elif node is None:
        data = None
    else:
        data = node.key
    return data


def display_node(node, space="\t", level=0):
    if node is None:
        print(space*level)
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    print("\t")
    display_node(node.right, space, level+1)
    print(space*level + str(node.key))
    display_node(node.left, space, level+1)


def hight_of_node(node):
    if node is None:
        return 0
    else:
        return 1+max(hight_of_node(node.left), hight_of_node(node.right))


def size_of_node(node):
    if node is None:
        return 0
    else:
        return 1+size_of_node(node.left)+size_of_node(node.right)


def max_depth(node):
    if node == None:
        return 0
    else:
        return max(max_depth(node.left)+1, max_depth(node.right)+1)


def min_depth(node):
    if node == None:
        return 0
    else:
        return min(max_depth(node.left)+1, max_depth(node.right)+1)


def travelse_in_order(node):
    if node is None:
        return []
    else:
        return travelse_in_order(node.left)+[node.key]+travelse_in_order(node.right)


def travelse_pre_order(node):
    if node is None:
        return []

    else:
        return [node.key]+travelse_pre_order(node.left)+travelse_pre_order(node.right)


def travelse_post_order(node):
    if node is None:
        return []
    else:
        return travelse_post_order(node.left)+travelse_post_order(node.right)+[node.key]


node_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
# node_tuple = (((None, 3, None), 4, (None, 5, None)),
#               6, ((None, 7, None), 8, (None, 9, None)))
node = parse_tuple_to_node(node_tuple)
print(min_depth(node))


"""
Binary Search Tree (BST)
A binary search tree or BST is a binary tree that satisfies the following conditions:

The left subtree of any node only contains nodes with keys less than the node's key
The right subtree of any node only contains nodes with keys greater than the node's key
It follows from the above conditions that every subtree of a binary search tree must also be a binary search tree.

QUESTION 8: Write a function to check if a binary tree is a binary search tree (BST).

QUESTION 9: Write a function to find the maximum key in a binary tree.

QUESTION 10: Write a function to find the minimum key in a binary tree.

Here's a function that covers all of the above:
"""


def remove_none(nums):
    return [num for num in nums if num is not None]


def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_left, min_left, max_left = is_bst(node.left)
    is_bst_right, min_right, max_right = is_bst(node.right)

    is_bst_node = (is_bst_left and is_bst_right and (
        max_left is None or max_left < node.key) and (min_right is None or min_right > node.key))

    min_key = min(remove_none([min_left, node.key, min_right]))
    max_key = max(remove_none([max_left, node.key, max_right]))
    return is_bst_node, min_key, max_key


print(is_bst(node))

"""                     QUESTION
QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

Insert the profile information for a new user.
Find the profile information of a user, given their username
Update the profile information of a user, given their usrname
List all the users of the platform, sorted by username
You can assume that usernames are unique.

"""


class User:
    def __init__(self, username, email, name):
        self.username = username
        self.email = email
        self.name = name

    # string  represnation in list or tuble
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    # string  represnation
    def __str__(self):
        return self.__repr__()


class BSTUser:
    def __init__(self, username, value=None):
        self.username = username
        self.left = None
        self.right = None
        self.value = value
        self.parent = None
        # string  represnation in list or tuble
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.value.name, self.value.email)

    # string  represnation
    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username >= user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        if not len(self.users):
            return -1
        # linear search
        # for user in self.users:
        #     if user.username == username:
        #         return user
        # binary search
        low_index, high_index = 0, len(self.users)-1
        while low_index <= high_index:
            middle_index = (low_index+high_index)//2
            if self.users[middle_index].username == username:
                return self.users[middle_index]
            elif self.users[middle_index].username > username:
                high_index = middle_index - 1
            elif self.users[middle_index].username < username:
                low_index = middle_index + 1
        return -1

    def update(self, user):
        if not len(self.users):
            return -1
        # linear search
        # for user in self.users:
        #     if user.username == username:
        #         return user
        # binary search
        low_index, high_index = 0, len(self.users)-1
        while low_index <= high_index:
            middle_index = (low_index+high_index)//2
            if self.users[middle_index].username == user.username:
                self.users[middle_index].name = user.name
                self.users[middle_index].email = user.email
                return self.users[middle_index]
            elif self.users[middle_index].username > user.username:
                high_index = middle_index - 1
            elif self.users[middle_index].username < user.username:
                low_index = middle_index + 1
        return -1

    def list_all(self):
        return self.users



user_1 = User('aakash', 'Aakash Rai', 'aakash@example.com')
user_2 = User('biraj', 'Biraj Das', 'biraj@example.com')
user_3 = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
user_4 = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
user_5 = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
user_6 = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
user_7 = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [
    user_1,
    user_2,
    user_3,
    user_4,
    user_5,
    user_6,
    user_7,
]
database = UserDatabase()

for user in users:
    database.insert(user)


class BSTDatabase:
    def insert(self,node,username,user):
        if node is None:
            node = BSTUser(username,user)
        elif node.username < username:
            node.left = self.insert(node.left,username,user)
            node.left.parent = node
        elif node.username > username :
            node.right = self.insert(node.right,username,user)
            node.right.parent = node
        return node
    def find(self,node,username):
        if node is None:
            return None 
        elif node.username == username:
            return node 
        elif node.username > username:
            return self.find(node.left,username)
        elif node.username < username:
            return self.find(node.right,username)
    def update(self,node,user):
        user = self.find(node,user.username)
        if user is None:
            return None 
        else:
            user.value = user
            return user

    def list_all(self,node):
        if node is None:
                return []
        return self.list_all(node.left) + [(node.username, node.value)] + self.list_all(node.right)
    



database = BSTDatabase()
root = database.insert(None,user_1.username,user_1)
users = [
    user_2,
    user_3,
    user_4,
    user_5,
    user_6,
    user_7,
]
for user in users :
    database.insert(root,user.username,user)

def display_node_users(node, space="\t", level=0):
    if node is None:
        print(space*level)
        return
    if node.left is None and node.right is None:
        print(space*level + str(node.username))
        return
    print("\t")
    display_node_users(node.right, space, level+1)
    print(space*level + str(node.username))
    display_node_users(node.left, space, level+1)

display_node_users(root)