#read input file
with open("input.txt") as file:
    lines = [line.strip() for line in file]

#read test file
with open("test-input.txt") as testfile:
    testlines = [line.strip() for line in testfile]

#dictionary to store directory and size
dirr_and_size = {"/":0}

#list to store current directory
curr_dir = ["/"]

#function to change directory
def change_directory(dir):
    global curr_dir
    curr_dir.append(dir)

#function to move from directory
def move_from_directory():
    global curr_dir
    del curr_dir[-1]

#function to change directory to root
def cd_root():
    global curr_dir
    curr_dir = ["/"]

#process line and check if command or size
# if command, process command
# if size, add size to all directories in curr_dir
def process_line(str):
    if str[0] == '$':
        process_command(str)
    else:
        str_arr = str.split(" ")
        if str_arr[0].isdigit():
            add_size_to_directories(int(str_arr[0]))

#process command
def process_command(str):
    str_arr = str.split(" ")
    if str_arr[1] == "cd":
        process_cd(str_arr[2])

#process cd command
def process_cd(directory):
    if directory == "..":
        move_from_directory()
    elif directory == "/":
        cd_root()
    else:
        change_directory(directory)

#add given size to all directories in curr_dir
def add_size_to_directories(size):
    global dirr_and_size
    for dirr in curr_dir:
        if dirr in dirr_and_size:
            dirr_and_size[dirr] += size
        else:
            dirr_and_size[dirr] = size

#if TEST==True, process test lines
#if TEST==False, process input lines
TEST = False

if TEST:
    #process all test lines
    for line in testlines:
        process_line(line)
else:
    #process all input lines
    for line in lines:
        process_line(line)

#CALC SUM FOR ALL DIRECTORIES WITH SIZE < 100000
sum = 0
for key in dirr_and_size:
    if dirr_and_size[key] < 100000:
        sum += dirr_and_size[key]

#print sum
print(sum)

# Path: 7/7b.py
# Compare this snippet from 7/no_space_left_on_device.py:

