f = open("input.txt")

lines = f.readlines()

def test_data():
    return lines[1] + lines[2] + lines[3] + lines[4] + lines[5]

def is_fully_contained(src, trg):

    src_split = src.split("-")
    src_bottom = int(src_split[0])
    src_top = int(src_split[1])

    trg_split = trg.split("-")
    trg_bottom = int(trg_split[0])
    trg_top = int(trg_split[1])

    if src_bottom >= trg_bottom and src_top <= trg_top:
        return True
    else:
        return False

def solve(lines):
    print("size of data:", len(lines))
    counter = 0
    for line in lines:
        ranges = line.split(",")
        
        #pick out ranges
        first = ranges[0]
        second = ranges[1]

        #check if first range is fully contained in second
        if is_fully_contained(first, second):
            counter += 1
        elif is_fully_contained(second, first):
            counter += 1
    print(counter)
        
solve(lines)
        