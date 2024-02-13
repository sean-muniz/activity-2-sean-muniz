def decorate(func):
    def wrapper(line):
        func(line)
        numbers = line.split()
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i])
        print(numbers)
        print(len(numbers))
        print(sum(numbers)/len(numbers))
        print(max(numbers))
    return wrapper;

@decorate
def process_line(line):
    print("Here are the stats for this line: ")

def printStats(t):
    try: 
        with open(t, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines)):
                print("----------")
                print("Line: " + str(i + 1))
                print("----------")
                process_line(lines[i])
                print("----------\n")
    except FileNotFoundError: 
        print("Could not find file.")

printStats("numbers.txt")
