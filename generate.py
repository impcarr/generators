import random

def book():
    print()
    print(random.choice(open("books.txt").read().splitlines()))

def conversation():
    #I know this can generate someone talking to themself. This is intended behavior.
    first_conversant = random.choice(open("characters.txt").read().splitlines())
    second_conversant = random.choice(open("characters.txt").read().splitlines())
    first_mood = random.choice(open("moods.txt").read().splitlines())
    second_mood = random.choice(open("moods.txt").read().splitlines())
    print((f"\nYou see {first_conversant} and {second_conversant} having a conversation. {first_conversant} looks {first_mood} and {second_conversant} looks {second_mood}.")
)


def other():
    print("Not yet implemented, moron")




def main():
    while True:
        x = input('\nPress 1 to generate a book, 2 to generate a conversation, or 3 to generate something else. \nType \'done\' to exit \n')
        if x == '1':
            book()
        if x == '2':
            conversation()
        if x == '3':
            other()
        if x.lower() == 'done':
            break


if __name__ == "__main__":
    main()