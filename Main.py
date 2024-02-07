def main():
    #running loop if file isn't found
    while True:
        #using try/except to make sure file is found
        user_file = input("Enter the file you want to open: ")
        try:
            open(user_file, "r")
            menu_display(user_file)
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
            continue
def menu_display(user_file):
    #Starting loop on main menu
    while True:
        #running loop until person types "exit"
        print()
        print("COMMAND MENU")
        print("view - View a contact")
        print("add - Add a contact")
        print("del - Delete a contact")
        print("exit - Exit the program")
        print()
        choice = input("Command: ")
        #calling function to what user chooses
        if choice == "view":
            read_and_print(user_file)
        elif choice == "add":
            add_contact(user_file)
        elif choice == "del":
            delete_contact(user_file)
        elif choice == "exit":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue


def read_and_print(user_file):
    #opening file to read.
    i = 0
    lines = open(user_file, "r")
    for line in lines:
        i += 1
        line = line.strip()
        #casing "i" as a string for compiler
        print(str(i) + ". " + line)
    #closing file
    lines.close()


def add_contact(user_file):
    #asking user for input
    print()
    add_name = input("Name: ")
    add_email = input("Email: ")
    add_phone = input("Phone: ")
    #appending file information
    add_new_contact = open(user_file, "a")
    add_new_contact.write(add_name + ", " + add_email + ", " + add_phone + "\n")
    add_new_contact.close()
    print(add_name + " was added")
    print()


def delete_contact(user_file):
    #calling read_and_print function for display
    read_and_print(user_file)
    print()
    #saving user choice in int format
    del_contact = int(input("Enter the number of the contact you want to delete: "))
    i = 0
    #creating new string variable
    new_line = " "
    lines = open(user_file, "r")
    for line in lines:
        i += 1
        line = line.strip()
        #checking if i is equal to the user number choice. if not saving that line to new string variable
        if i != del_contact:
            new_line += line + "\n"
    #overwriting file with new information from string variable
    open(user_file, "w").write(new_line)
    lines.close()
    print(del_contact, "was removed")
    print()


main()
