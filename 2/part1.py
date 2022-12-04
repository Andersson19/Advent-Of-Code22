def calc_points_for_round(opp_choice, my_choice):
    pts = 0
    match opp_choice:
        case "A":
            if my_choice == "Y":
                pts += 6
            elif my_choice == "X":
                pts += 3
        case "B":
            if my_choice == "Z":
                pts += 6
            elif my_choice == "Y":
                pts += 3
        case "C":
            if my_choice == "X":
                pts += 6
            elif my_choice == "Z":
                pts += 3

    match my_choice:
        case "X":
            pts += 1
        case "Y":
            pts += 2
        case "Z":
            pts += 3

    return pts

f = open("input.txt")

lines = f.readlines()

score = 0
for line in lines:
    score += calc_points_for_round(line[0], line[2])

print(score)
