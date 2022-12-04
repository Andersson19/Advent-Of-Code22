f = open("input.txt")

lines = f.readlines()

calories_list = []
tmp = 0

for line in lines:
    if line != '\n':
        tmp += int(line)
    else:
        calories_list.append(int(tmp))
        tmp = 0

top_three = sorted(calories_list, reverse=True)[:3]
print(sum(top_three))