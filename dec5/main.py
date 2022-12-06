import re

# [N] [G]                     [Q]    
# [H] [B]         [B] [R]     [H]    
# [S] [N]     [Q] [M] [T]     [Z]    
# [J] [T]     [R] [V] [H]     [R] [S]
# [F] [Q]     [W] [T] [V] [J] [V] [M]
# [W] [P] [V] [S] [F] [B] [Q] [J] [H]
# [T] [R] [Q] [B] [D] [D] [B] [N] [N]
# [D] [H] [L] [N] [N] [M] [D] [D] [B]
#  1   2   3   4   5   6   7   8   9 

START = [
    ['D', 'T', 'W', 'F', 'J', 'S', 'H', 'N'],
    ['H', 'R', 'P', 'Q', 'T', 'N', 'B', 'G'],
    ['L', 'Q', 'V'],
    ['N', 'B', 'S', 'W', 'R', 'Q'],
    ['N', 'D', 'F', 'T', 'V', 'M', 'B'],
    ['M', 'D', 'B', 'V', 'H', 'T', 'R'],
    ['D', 'B', 'Q', 'J'],
    ['D', 'N', 'J', 'V', 'R', 'Z', 'H', 'Q'],
    ['B', 'N', 'H', 'M', 'S']
]

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# START = [
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
# ]



def main():
    file = open('dec5/data.txt', 'r')
    lines = file.readlines()

    for line in lines:
        print("NEW STEP")
        cleaned = line.rstrip('\n')
        steps = re.findall('([0-9]+)', cleaned)
        # print(steps)
        
        move = int(steps[0])
        fro = int(steps[1])
        to = int(steps[2])

        from_list = START[fro - 1].copy()
        to_list = START[to - 1].copy()
        start_at = len(from_list) - move
        print('variables: ', move, from_list, to_list, start_at)

        # original_from_array
        # data_from_old
        DATA_TO_MOVE = from_list[start_at:len(from_list)]
        # new_from_array
        NEW_FROM_STACK = list(from_list[0:start_at])
        print('NEW_FROM_STACK:', NEW_FROM_STACK)

        # old_to_array
        # new_to_array
        NEW_TO_STACK = to_list + DATA_TO_MOVE
        print('NEW_TO_STACK', NEW_TO_STACK)
        print('DATA_TO_MOVE:', DATA_TO_MOVE)

        # assign old array
        START[fro - 1] = NEW_FROM_STACK
        # assign new array
        START[to - 1] = NEW_TO_STACK

        print(START)
        print("*************************")
        

    string = ''
    for stack in START:
        string += stack[-1]
    print(string)

if __name__ == '__main__':
    main()

    # BNTQBRJQS
    # BNHQBRJQS
    # DHLNNMDDB
    # GRTSWNJHH