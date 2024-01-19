if __name__ == "__main__":
        import sys

        value = len(sys.argv) - 1
        if value == 0:
            print("0 arguments.")
        elif value == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(value))
        for i in range(value):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
