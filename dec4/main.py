
def get_start_stop(n):
    split = n.split('-')
    cleaned = map(lambda x: int(x), split)
    return list(cleaned)

def main():
    file = open('dec4/data.txt', 'r')
    lines = file.readlines()

    total = 0
    for line in lines:
        clean = line.rstrip('\n')
        assignments = clean.split(',')
        cleaned = list(map(get_start_stop, assignments))
        x = range(cleaned[0][0], cleaned[0][1]+1)
        y = range(cleaned[1][0], cleaned[1][1]+1)
        print(x, y)
        xs = set(x)
        ys = set(y)
        print(xs.intersection(ys))
        if not not len(xs.intersection(y)):
            total += 1

        # 2-4,6-8
        # 2-3,4-5
        # 5-7,7-9
        # 2-8,3-7
        # 6-6,4-6
        # 2-6,4-8

        # if grp1[0] >= grp2[0] or grp1[1] <= grp2[1]:
        #     total += 1
        # elif grp2[0] >= grp1[0] or grp2[1] <= grp1[1]:
        #     total += 1

    print(total)

    file.close()

if __name__ == '__main__':
    main()