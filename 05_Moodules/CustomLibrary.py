import sys

def main():
    print(hello(sys.argv[1]))
    print(goodbye(sys.argv[1]))

def hello(name):
    return f"Hello, {name}!"

def goodbye(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    main()