#open input.txt
with open("input.txt") as file:
    lines = [line.strip() for line in file]

#open test-input.txt
with open("test.txt") as testfile:
    testlines = [line.strip() for line in testfile]

#create test_matrix as 2d array with rows = len(testlines) and cols = len(testlines[0])
test_matrix = [[0 for x in range(len(testlines[0]))] for y in range(len(testlines))]

#create test_matrix as 2d array with rows = len(testlines) and cols = len(testlines[0])
matrix = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]

#store input from testfile into test_matrix
for i in range(len(testlines)):
    for j in range(len(testlines[0])):
        test_matrix[i][j] = testlines[i][j]

#store input from file into matrix
for i in range(len(lines)):
    for j in range(len(lines)):
        matrix[i][j] = lines[i][j]

#number of items in the first column of test_matrix
test_sum = len(test_matrix[0])
#added with the number of items in the first row of test_matrix
test_sum += len(test_matrix)
#and added with the number of items in the last column of test_matrix
test_sum += len(test_matrix[0])
#and added with the number of items in the last row of test_matrix
test_sum += len(test_matrix)
#and remove for items counted twice (the corners of the matrix)
test_sum -= 4

#number of items in the first column of matrix
sum = len(matrix[0])
#added with the number of items in the first row of matrix
sum += len(matrix)
#and added with the number of items in the last column of matrix
sum += len(matrix[0])
#and added with the number of items in the last row of matrix
sum += len(matrix)
#and remove for items counted twice (the corners of the matrix)
sum -= 4

#print the result
print(test_sum)

#print the result
print(sum)




