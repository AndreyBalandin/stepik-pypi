import sys

from max_finder import max_finder
from sum_finder import sum_finder

def main():
    op = sys.argv[1]

    if op == "max":
        print(max_finder(*sys.argv[2:]))
    elif op == "sum":
        print(sum_finder(*sys.argv[2:]))


if __name__ == "__main__":
    main()
