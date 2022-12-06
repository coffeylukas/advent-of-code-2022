# points
# rock = 1
# paper = 2
# scissors = 3

# won = 6
# draw = 3
# lost = 0

# For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
#     1   2   3   opp
# 1   2   3   4
# 2   3   4   5
# 3   4   5   6
# you

#     X     Y     Z   opp
# A   draw  win   lose
# B   lose  draw  win
# C   win   lose  draw
# you

# x lose
# y draw
# z win

def find_answer(opp, result):
    if result == 'Y':
        return opp
    elif result == 'Z':
        if opp == 1:
            return 2
        if opp == 2:
            return 3
        if opp == 3:
            return 1
    elif result == 'X':
        if opp == 1:
            return 3
        if opp == 2:
            return 1
        if opp == 3:
            return 2

def convert(x):
    if x == 'A':
        return 1 # rock
    elif x == 'B':
        return 2 # paper
    elif x == 'C':
        return 3 # scissors
    else:
        raise ValueError('Not a valid answer')

def play_game(p1, result):
    opp = convert(p1)
    you = find_answer(opp, result)

    win, draw, loss = 6, 3, 0

    if opp == you:
        return draw + you
    elif opp == 1:
        if you == 2:
            return win + you
        if you == 3:
            return loss + you
    elif opp == 2:
        if you == 1:
            return loss + you
        if you == 3:
            return win + you
    elif opp == 3:
        if you == 1:
            return win + you
        if you == 2:
            return loss + you


def main():
    file = open('dec2/data.txt', 'r')

    lines = file.readlines()
    
    # run script
    running_score = 0
    for round in lines:
        if not round == '\n':
            result = round.split(' ')
            opponent = result[0].rstrip('\n')
            end = result[1].rstrip('\n')
            
            # print(opponent, you)
            your_score = play_game(opponent, end)
            running_score = running_score + your_score
            print(running_score)

    # close file
    file.close()

if __name__ == "__main__":
    main()