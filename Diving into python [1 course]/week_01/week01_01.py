import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = 0
        for i in sys.argv[1]:
            res += int(i)
        print(res)
