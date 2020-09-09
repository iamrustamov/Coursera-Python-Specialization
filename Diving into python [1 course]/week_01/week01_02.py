import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
        for i in range(1, count + 1):
            white_space = ' ' * (count - i)
            sharps = '#' * i
            print(white_space + sharps)
