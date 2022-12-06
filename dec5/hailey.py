
def main():
    print('test')

if __name__ == '__main__':
    main()

    data = []
    delimiter = ''

    with open ('data05.txt') as file:
        for line in file.readlines():
            element = []
            for token in line.strip().split(delimiter):
                element.append(token)
                data.append(element)

                stacks = [['']], 

                I came, half way tried, and gave up. k bye 
                - Hailey 