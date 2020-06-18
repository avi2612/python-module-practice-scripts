# program to move to another directory with exception handling

import os

def main():
    print(f"Current directory is {os.getcwd()}")
    path=input("Enter required directory path to move to ")
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("directory path not exists")
    except NotADirectoryError:
        print("given path is file path")
    except PermissionError:
        print("You don't have permission, to access this directory")
    else:
        print("new directory is", os.getcwd())
    finally:
        print("I Hope !!!, this script will works")

if __name__ == "__main__":
    main()