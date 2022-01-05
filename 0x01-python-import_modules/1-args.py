#!/usr/bin/python3
import sys
elements = len(sys.argv)
if elements == 1:
    print("0 arguments.".format(elements))
elif elements == 2:
    print("{} argument:".format(elements - 1))
    print("{}: {}".format(elements - 1, sys.argv[elements - 1]))
else:
    print("{} arguments:".format(elements - 1))
    for i in range(1, elements):
        print("{}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    import sys
