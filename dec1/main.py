

def main():
    # read in file
    file = open('dec1/data.txt', 'r')
    lines = file.readlines()

    highest_counts = [0, 0, 0]

    # parse through lines
    current_elf = 0
    for line in lines:
        # if new line
        if str(line) == '\n':
            current_elf = 0

        # if number
        else:
            calories = int(line)
            print('calories:' + str(calories))
            current_elf += calories

        # for index in range(1, len(highest_counts)):
        #     insertion_index = index - 1
        #     while insertion_index >= 0 and highest_counts[insertion_index] > current_elf:
        #         highest_counts[insertion_index + 1] = highest_counts[insertion_index]
        #         insertion_index -= 1
        #     highest_counts[insertion_index + 1] = current_elf

        if current_elf > highest_counts[2]:
            highest_counts[0] = highest_counts[1]
            highest_counts[1] = highest_counts[2]
            highest_counts[2] = current_elf
        elif current_elf > highest_counts[1]:
            highest_counts[0] = highest_counts[1]
            highest_counts[1] = current_elf
        elif current_elf > highest_counts[0]:
            highest_counts[0] = current_elf

        print('current_elf:' + str(current_elf))
    
    print(highest_counts)
    print(sum(highest_counts))

    file.close()

if __name__ == "__main__":
    main()