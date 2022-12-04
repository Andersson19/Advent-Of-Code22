f = open("input.txt")
lines = f.readlines()

# Returns the first duplicate character from first string in second string
def find_duplicate_char(first, second):
    done = False
    dup_char = ''
    while not done:
        for char in first:
            if second.find(char) != -1:
                dup_char = char
                done = True
    print("returning dup_char:", dup_char)
    return dup_char

# Returns the priority for the duplicate_character
# 1 - 26 for a - z
# 27 - 52 for A - Z
def get_priority(character):
    if character.islower():
        return ord(character)-96
    else:
        return ord(character)-38


sum = 0
for line in lines:
    length = len(line)
    first_half = slice(0, length//2)
    second_half = slice(length//2, len(line))
    print("first:", line[first_half], " - second:", line[second_half])

    sum += get_priority(find_duplicate_char(line[first_half], line[second_half]))

print(sum)