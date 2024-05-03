def input_error(func):
    def inner(*args, **kwargs):
        help_message = "Or enter 'help' for the instructions."
        value_error_message = ("Make sure you follow the 'add username phone' or 'change username phone' template.\n"
                               f"For example, 'add Bob 0123456789'or 'change Bob 0123456789'.\n{help_message}")
        index_error_value = ("Make sure you follow the 'phone username' template to display a contact's info.\n"
                             f"For example, 'phone Bob'.\n{help_message}")
        general_error_message = ("Seems like you've provided an invalid command.\n"
                                 f"{help_message}")
        try:
            return func(*args, **kwargs)
        except ValueError:
            return value_error_message
        except IndexError:
            return index_error_value
        except KeyError:
            return general_error_message
        except TypeError:
            return general_error_message
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "The contact has been added successfully."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "The contact has been changed successfully."
    else:
        return f"{name} is not in the contacts."


@input_error
def display_contact(args, contacts):
    name = args[0]
    if name in contacts:
        phone = contacts.get(name)
        return f"Name {name}. Phone {phone}."
    else:
        return f"{name} was not found."


@input_error
def display_all_contacts(contacts):
    contacts_list = ""
    for key in contacts.keys():
        if key:
            contacts_list += f"Name: {key}. Phone: {contacts[key]}\n"
        else:
            break
    return contacts_list


def main():
    contacts = {}
    instruction = ("Please use the instruction below:\n"
                   "'add \x1B[3mphone username\x1B[0m' to add a new contact. "
                   "E.g. 'add Bob 0123456789'\n"
                   "'change \x1B[3mphone username\x1B[0m' to update an existing contact (phone). "
                   "E.g. 'change Bob 0987654321'\n"
                   "'phone \x1B[3musername\x1B[0m' to display a contact's info. E.g. 'phone Bob'\n"
                   "'all' to display all contacts\n")
    print("Welcome to the assistant manager! My name is Alex.")
    user_name = input("What's your name?\n").capitalize()
    print(f"Nice to meet you, {user_name}!\n\n{instruction}")

    while True:
        user_input = input("Please enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["exit", "close"]:
            print(f"Good bye, {user_name}!")
            break
        elif command in ["hello", "hi", "nice to meet you"]:
            print(f"How can I help you {user_name}?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(display_contact(args, contacts))
        elif command == "all":
            print(display_all_contacts(contacts))
        elif command == "help":
            print(f"{instruction}")
        else:
            print("Sorry, I didn't quite catch you. Seems like you've provided an invalid command.\n"
                  "Enter 'help' for the instructions.")


if __name__ == '__main__':
    main()