def person():
    print("Not yet implemented")
import random

def location():
    print("Not yet implemented")

def other():
    x = input("Press 1 to generate the title of a book\n")
    if x == '1':
        print()
        print(random.choice(open("books.txt").readlines()))




def main():
    while True:
        x = input('Press 1 to generate a person\'s name, 2 to generate a town or other location, or 3 to generate something else. \nType \'done\' to exit \n')
        if x == '1':
            person()
        if x == '2':
            location()
        if x == '3':
            other()
        if x.lower() == 'done':
            break


if __name__ == "__main__":
    main()