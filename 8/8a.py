#open input.txt
with open("input.txt") as file:
    lines = [line.strip() for line in file]

#open test-input.txt
with open("test.txt") as testfile:
    testlines = [line.strip() for line in testfile]

#create object Tree with attributes:
#   height: the height of the tree
#   coordinates: the coordinates of the tree
#   visible: True if the tree is visible, False otherwise
#   forest = the forest where the tree is located
#   left_heigth: the height of the tree on the left
#   right_height: the height of the tree on the right
#   top_height: the height of the tree on the top
#   bottom_height: the height of the tree on the bottom
#   left_visible: True if the tree on the left is visible, False otherwise
#   right_visible: True if the tree on the right is visible, False otherwise
#   top_visible: True if the tree on the top is visible, False otherwise
#   bottom_visible: True if the tree on the bottom is visible, False otherwise
class Tree:
    def __init__(self, height, coordinates, forest):
        self.height = height
        self.coordinates = coordinates
        self.visible = False
        self.forest = forest
        self.left_height = 0
        self.right_height = 0
        self.top_height = 0
        self.bottom_height = 0
        self.left_visible = True if coordinates[1] == 0 else None
        self.right_visible = True if coordinates[1] == self.forest.cols - 1 else None
        self.top_visible = True if coordinates[0] == 0 else None
        self.bottom_visible = True if coordinates[0] == self.forest.rows - 1 else None

    #get height of the tree
    def get_height(self):
        return self.height
    
    def __str__(self):
        return "Tree at " + str(self.coordinates) + " with height " + str(self.height)

#class Forest with attributes:
#   trees: 2d list of Tree objects, initally empty
#   rows: the number of rows in the matrix
#   cols: the number of columns in the matrix
class Forest:
    def __init__(self, rows, cols):
        self.trees = []
        self.rows = rows
        self.cols = cols

    def __str__(self):
        return "Forest with " + str(self.rows) + " rows and " + str(self.cols) + " columns"

    #function set the forest
    def set_forest(self, trees):
        self.trees = trees

    #function to set the height of the trees on the left, right, top and bottom
    def set_heights(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if j != 0:
                    self.trees[i][j].left_height = self.trees[i][j-1].height
                if j != self.cols - 1:
                    self.trees[i][j].right_height = self.trees[i][j+1].height
                if i != 0:
                    self.trees[i][j].top_height = self.trees[i-1][j].height
                if i != self.rows - 1:
                    self.trees[i][j].bottom_height = self.trees[i+1][j].height

    #recursive function to check for each tree in forest if it is visible from any direction
    #  if the direction visibility is True, then check if height of tree is larger than the height of the tree in that direction, if so, set visible to true for that tree
    #  if any direction visibility is None, then return recursive call to that direction
    def check_tree(self, tree):
        if tree.left_visible == True:
            if tree.height > tree.left_height:
                #print statement that tree is visible from that direction
                print("Tree at " + str(tree.coordinates) + " with height " + str(tree.height) + " is visible from the left")
                tree.left_visible = True
            else:
                tree.left_visible = False
        elif tree.left_visible == None:
            print("left is None! checking left tree..")
            self.check_tree(self.trees[tree.coordinates[0]][tree.coordinates[1] - 1])
            if tree.height > tree.left_height:
                #print statement that tree is visible from that direction
                print("Tree at " + str(tree.coordinates) + " with height " + str(tree.height) + " is visible from the left")
                tree.left_visible = True
            else:
                tree.left_visible = False

        if tree.right_visible == True:
            if tree.height > tree.right_height:
                #print statement that tree is visible from that direction
                print("Tree at " + str(tree.coordinates) + " with height " + str(tree.height) + " is visible from the right")
                tree.right_visible = True
            else:
                tree.right_visible = False
        elif tree.right_visible == None:
            print("right is None! checking right tree..")
            self.check_tree(self.trees[tree.coordinates[0]][tree.coordinates[1] + 1])
            if tree.height > tree.right_height:
                #print statement that tree is visible from that direction
                print("Tree at " + str(tree.coordinates) + " with height " + str(tree.height) + " is visible from the right")
                tree.right_visible = True
            else:
                tree.right_visible = False

        if tree.top_visible == True:
            if tree.height > tree.top_height:
                #print statement that tree is visible from that direction
                print("Tree at " + str(tree.coordinates) + " with height " + str(tree.height) + " is visible from the top")
                tree.top_visible = True
            else:
                tree.top_visible = False
        elif tree.top_visible == None:
            print("top is None! checking top tree..")
            self.check_tree(self.trees[tree.coordinates[0] - 1][tree.coordinates[1]])
            if tree.height > tree.top_height:
                #print statement that tree is visible from that direction
                print("Tree at " + str(tree.coordinates) + " with height " + str(tree.height) + " is visible from the top")
                tree.top_visible = True
            else:
                tree.top_visible = False

        if tree.bottom_visible == True:
            if tree.height > tree.bottom_height:
                #print statement that tree is visible from that direction
                print("Tree at " + str(tree.coordinates) + " with height " + str(tree.height) + " is visible from the bottom")
                tree.bottom_visible = True
            else:
                tree.bottom_visible = False
        elif tree.bottom_visible == None:
            print("bottom is None! checking bottom tree..")
            self.check_tree(self.trees[tree.coordinates[0] + 1][tree.coordinates[1]])
            if tree.height > tree.bottom_height:
                #print statement that tree is visible from that direction
                print("Tree at " + str(tree.coordinates) + " with height " + str(tree.height) + " is visible from the bottom")
                tree.bottom_visible = True
            else:
                tree.bottom_visible = False

    def set_visibility(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.check_tree(self.trees[i][j])


    #function to check all trees and if they are visible from any of the 4 directions and print if they are visible from that direction
    #only need to check inner trees
    def check_visibility(self):
        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                if self.trees[i][j].left_visible or self.trees[i][j].right_visible or self.trees[i][j].top_visible or self.trees[i][j].bottom_visible:
                    self.trees[i][j].visible = True
                    if self.trees[i][j].left_visible == True:
                        print("Tree at " + str(self.trees[i][j].coordinates) + " with height " + str(self.trees[i][j].height) +" is visible from the left")
                    if self.trees[i][j].right_visible == True:
                        print("Tree at " + str(self.trees[i][j].coordinates) + " with height " + str(self.trees[i][j].height) + " is visible from the right")
                    if self.trees[i][j].top_visible == True :
                        print("Tree at " + str(self.trees[i][j].coordinates) + " with height " + str(self.trees[i][j].height) + " is visible from the top")
                    if self.trees[i][j].bottom_visible == True:
                        print("Tree at " + str(self.trees[i][j].coordinates) + " with height " + str(self.trees[i][j].height) + " is visible from the bottom")

    
                

    #function to count the number of visible trees
    def count_visible(self):
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.trees[i][j].visible:
                    count += 1
        return count

    #function to print the forest in a matrix with the height of each tree
    def print_forest(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.trees[i][j].height, end = " ")
            print()

#function to create an object Forest from a list of strings
def create_forest(lines):
    rows = len(lines)
    cols = len(lines[0])
    forest = Forest(rows, cols)
    trees = []
    i = 0
    for line in lines:
        trees.append([])
        for j in range(cols):
            trees[i].append(Tree(int(line[j]), (i, j), forest))
        i += 1
    forest.set_forest(trees)
    forest.set_heights()
    forest.print_forest()
    forest.set_visibility()
    return forest

test_forest = create_forest(testlines)


