def inputInfo():
    name = input("Enter you name: ")
    age = input("Enter your age: ")
    address = input("Enter you address: ")
    return name, age, address

def displayOutput(name, age, address):
    print("Hi, my name is \033[4m" + name + "\033[0m. I am \033[4m" + age + "\033[0m years old and I live in \033[4m" + address + "\033[0m.")

name, age, address = inputInfo()

displayOutput(name, age, address)