
def main():
    file = open('dec6/data.txt', 'r')
    lines = file.readlines()

    for line in lines:
        packet = line.rstrip('\n')
        marker_window_size = 4

        i = 0
        marker = ''
        while i < len(packet) - 3 and len(marker) != marker_window_size:
            start = i
            end = min(i + marker_window_size, len(packet))
            marker = set(packet[start:end])
            print('-'*start + packet[start:end] + '-'*(len(packet)-end), len(marker) == marker_window_size, end)
            i += 1

    file.close()

if __name__ == '__main__':
    main()