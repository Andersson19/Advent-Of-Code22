# Returns the first duplicate character from first string in second string
def find_duplicate_char(first, second, third):
    print("checking:")
    print(first, second, third)
    done = False
    dup_char = ''
    for char in first:
        if done:
            break
        result_second = second.find(char)
        if result_second != -1:
            result_third = third.find(char)
            if result_third != -1:
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

f = open("input.txt")
lines = f.readlines()

sum = 0
# index 0 - 0,1,2 - +0
# index 1 , 3,4,5 - +2
# index 2 - 6,7,8 - +4
# index 3 - 9,10,11 - +6
for i in range(0, int(len(lines)/3)):
    first = lines[i + (i*2)]
    second = lines[i+1 + (i*2)]
    third = lines[i+2 + (i*2)]
    
    sum += get_priority(find_duplicate_char(first,second,third))

print(sum)