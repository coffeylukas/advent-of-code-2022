import string

priorities = string.ascii_letters
print(priorities)

def main():
    file = open('dec3/data.txt', 'r')
    lines = file.readlines()
    N = 3

    groups = [lines[n:n+N] for n in range(0, len(lines), N)]
    
    total_count = 0
    for group in groups:
        l1 = group[0].rstrip('\n')
        l2 = group[1].rstrip('\n')
        l3 = group[2].rstrip('\n')
        
        common = None
        for letter in l1:
            if letter in l2 and letter in l3:
                common = letter
        
        priority = string.ascii_letters.index(common) + 1
        total_count += priority
        

        print(l1, l2, l3, common, priority)
    print(total_count)

if __name__ == "__main__":
    main()