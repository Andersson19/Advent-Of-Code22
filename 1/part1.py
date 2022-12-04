f = open("input.txt")

lines = f.readlines()

max = 0
tmp = 0
for line in lines:
    if line != '\n':
        tmp += int(line)
    else:
        if tmp > max:
            max = tmp
        tmp = 0
        
print(max)
