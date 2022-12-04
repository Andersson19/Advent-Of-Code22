f = open("input.txt")

lines = f.readlines()

def is_contained(src, trg):
    src_split = src.split("-")
    src_bottom = int(src_split[0])
    src_top = int(src_split[1])

    trg_split = trg.split("-")
    trg_bottom = int(trg_split[0])
    trg_top = int(trg_split[1])

    if src_top < trg_bottom:
        return False
    elif src_bottom > trg_top:
        return False

    return True

def solve(lines):
    counter = 0
    for line in lines:
        ranges = line.split(",")
        
        #pick out ranges
        first = ranges[0]
        second = ranges[1]

        #check if range is contained
        if is_contained(first, second):
            counter += 1
    print(counter)
        
solve(lines)
        