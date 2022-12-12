with open("test-input.txt") as testfile:
    testlines = [line.strip() for line in testfile]

with open("input.txt") as file:
    lines = [line.strip() for line in file]

dirr_and_size = {"/":0}
curr_dir = ["/"]

def change_directory(dir):
    global curr_dir
    curr_dir.append(dir)

def move_from_directory():
    global curr_dir
    del curr_dir[-1]

def cd_root():
    global curr_dir
    curr_dir = ["/"]

# process line and check if command or size
# if command, process command
# if size, add size to all directories in curr_dir
def process_line(str):
    if str[0] == '$':
        process_command(str)
    else:
        str_arr = str.split(" ")
        if str_arr[0].isdigit():
            add_size_to_directories(int(str_arr[0]))

# process command
def process_command(str):
    str_arr = str.split(" ")
    if str_arr[1] == "cd":
        process_cd(str_arr[2])

# process cd command
def process_cd(directory):
    if directory == "..":
        move_from_directory()
    elif directory == "/":
        cd_root()
    else:
        change_directory(directory)

# add given size to all directories in curr_dir
def add_size_to_directories(size):
    global dirr_and_size
    for dirr in curr_dir:
        if dirr in dirr_and_size:
            dirr_and_size[dirr] += size
        else:
            dirr_and_size[dirr] = size
        
for line in lines:
    process_line(line)

#CALC SUM FOR ALL DIRECTORIES WITH SIZE < 100000
sum = 0
for key in dirr_and_size:
    if dirr_and_size[key] < 100000:
        sum += dirr_and_size[key]

print(sum)