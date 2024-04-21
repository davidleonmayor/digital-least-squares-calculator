def imputName() -> str:
    return input("Enter your name: ")

def toGreeter() -> str:
    name = imputName()
    return "Hello, " + name + "!"

if __name__ == "__main__":
    print(toGreeter())
