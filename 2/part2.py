# A is rock
# B is paper
# C is scissor 
# 
# X is LOSS
# Y is DRAW
# Z is WIN

def calc_points_for_round(opp_choice, result):
    pts = 0
    my_choice = ""
    match opp_choice:
        case "A": # ROCK
            if result == "Z":   # WIN
                pts += 6
                my_choice = "paper"
            elif result == "Y": # DRAW
                pts += 3
                my_choice = "rock"
            else:               # LOSS
                my_choice = "scissor"
        case "B": #PAPER
            if result == "Z":   # WIN
                pts += 6
                my_choice = "scissor"
            elif result == "Y": # DRAW
                pts += 3
                my_choice = "paper"
            else:
                my_choice = "rock" # LOSS
        case "C": #SCISSOR
            if result == "Z":
                pts += 6
                my_choice = "rock"
            elif result == "Y":
                pts += 3
                my_choice = "scissor"
            else:
                my_choice = "paper"

    match my_choice:
        case "rock":
            pts += 1
        case "paper":
            pts += 2
        case "scissor":
            pts += 3

    return pts

f = open("input.txt")

lines = f.readlines()

score = 0
for line in lines:
    score += calc_points_for_round(line[0], line[2])

print(score)
