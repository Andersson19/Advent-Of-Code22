f = open("input.txt")
lines = f.readline()

def has_fourteen_distinct_chars(str):
    list = []

    for char in str:
        if char not in list:
            list.append(char)

    return len(str) == len(list)

for i in range(0,len(lines)-4):
    list = []
    list.append(lines[i])

    if has_fourteen_distinct_chars(lines[i:i+14]):
        print(i+14+1)