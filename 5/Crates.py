def test_data():
    data = []
    data.append("    [D]    ")
    data.append("[N] [C]    ")
    data.append("[Z] [M] [P]")
    data.append(" 1   2   3 ")

    data.append("move 1 from 2 to 1")
    data.append("move 3 from 1 to 3")
    data.append("move 2 from 2 to 1")
    data.append("move 1 from 1 to 2")

    return data, 3

f=open("input.txt")
lines=f.readlines()

test_lines, test_cols = test_data()

stacks = [[] for _ in range(0,9)]
test_stacks = [[] for _ in range(0,test_cols)]

#read crate structure
for line in lines[0:8]:
   for i in range(0,len(line),4):
       if (line[i+1] != " "):
           stacks[(int) (i/4)].insert(0,line[i+1])

#read test crate structure
for line in test_lines[0:test_cols]:
   for i in range(0,len(line),4):
       if (line[i+1] != " "):
           test_stacks[(int) (i/4)].insert(0,line[i+1])

#Move crate according to instruction
def moveCrate(str, curr_stack):
    arr = str.split(" ")
    amount = int(arr[1])
    fromCrate = int(arr[3])
    toCrate = arr[5]
    toCrate = int(toCrate[0:1]) #remove '\n'
    print("instruction: ", str)
    print("fromCrate before move: ", curr_stack[fromCrate-1])
    print("toCrate before move:", curr_stack[toCrate-1])
    
    #MOVE CRATE ONE BY ONE
    #for i in range(0,amount):
    #    curr_stack[toCrate-1].append(curr_stack[fromCrate-1].pop())

    #MOVE CRATE IN BLOCK
    slice_length = abs(amount - len(curr_stack[fromCrate-1]))
    block_to_move = curr_stack[fromCrate-1][slice_length:]
    curr_stack[fromCrate-1] = curr_stack[fromCrate-1][0:slice_length]
    curr_stack[toCrate-1] = curr_stack[toCrate-1] + block_to_move
    

    print("fromCrate after move: ", curr_stack[fromCrate-1])
    print("toCrate after move:", curr_stack[toCrate-1])


for line in lines[10:]:
    moveCrate(line,stacks)

for stack in stacks:
    print(stack.pop())

#testing
#for line in test_lines[test_cols+1:]:
#    moveCrate(line, test_stacks)


#for stack in test_stacks:
#    print(stack)



    