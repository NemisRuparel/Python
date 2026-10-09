# implementing simple square function to learn how to write unit tests in Python
def main():
    print("Square:", square_faulty(5))
    print("Square:", square(5))

def square_faulty(x):
    return x + x

def square(x):
    return x * x

if __name__ == "__main__":
    main()