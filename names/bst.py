class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # Insert the given value into the tree
    def insert(self, value):
        # if inserting we must already have a root
        if self.value == None:
            #print("No root")
            return None
        # if value is < self.value go left, make a new tree if empty, otherwise
        # keep goung recurse
        elif value < self.value:
            if self.left == None:
                print(f"No left node inserting {value}")
                self.left = BinarySearchTree(value)
            else:
                print(f"{value} is less than {self.value}, moving left")
                self.left.insert(value)
        # if >= then go right make a new tree if empty otherwise
        # keep going recurse
        elif value >= self.value:
            if self.right == None:
                print(f"No right node inserting {value}")
                self.right = BinarySearchTree(value)
            else:
                print(f"{value} is greater or equal to {self.value}, moving right")
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            print(f"{self.value} equals {target}")
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                print(f"{target} is < {self.value}, moving left")
                return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else:
                print(f"{target} is > {self.value}, moving right")
                return self.right.contains(target)
        else:
            print(f"{target} not found")
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            #print(f"Moving right to {self.right.value}")
            return self.right.get_max()
        else:
            #print(f"Max value found {self.value}")
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value != None:
            #print(self.value)
            cb(self.value)
            if self.right != None:
                self.right.for_each(cb)
            if self.left != None:
                self.left.for_each(cb)
