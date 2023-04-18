characters = []

while True:
    name = input("Enter character name (press enter to stop adding characters): ")
    if not name:
        break
    health = int(input("Enter character health: "))
    gender = input("Enter character gender (M/F): ")
    age = int(input("Enter character age: "))
    character = {'name': name, 'health': health, 'gender': gender, 'age': age}
    characters.append(character)


def readAllCharacters(characters):
    for character in characters:
        print(f"Name: {character['name']}")

def findCharacter(characters):
        character_name = input("Enter character name to view stats (press enter to exit): ")
        for character in characters:
            if character['name'] == character_name:
                print(f"Name: {character['name']}")
                print(f"Health: {character['health']}")
                print(f"Gender: {character['gender']}")
                print(f"Age: {character['age']}")
                break
        else:
            print("Character not found.")


def removeCharacter(characters):
    while True:
        option = input("Enter 'remove' to remove a character or 'find' to find a character (press enter to exit): ")
        if not option:
            break
            if option == "remove":
                name = input("Enter character name to remove: ")
            for character in characters:
                if character['name'] == name:
                    characters.remove(character)
                    print(f"{name} removed from the list.")
                    break
            else:
                print("Character not found.")
        elif option == "find":
            findCharacter(characters)
        else:
            print("Invalid option.")


readAllCharacters(characters)
findCharacter(characters)
removeCharacter(characters)
