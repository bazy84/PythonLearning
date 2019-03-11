import sys

def python_version():
    if sys.version_info.major == 3:
        print("\nYou sir, are running Python 3!")
    else:
        print("\nYou sir, are living in the past!")
        exit()


def main():
    python_version()

if __name__ == "__main__":
    main()