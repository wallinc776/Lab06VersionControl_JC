# Takes an exclusively numeric string and returns a string with digit shifted up by 3.
def encode(password):
    encoded_string = ""
    for char in password:
        # If conditions accounts for numbers that would have two digits if not handled differently.
        if(char == '7'):
            encoded_string += '0'
        elif(char == '8'):
            encoded_string += '1'
        elif(char == '9'):
            encoded_string += '2'
        else:
            encoded_string += str(int(char) + 3)
    return encoded_string


# Temp function to define "decode" on line 30
def decode(encoded_password):


def main():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    menu_choice = int(input("Please enter an option: "))
    while(menu_choice != 3):
        if(menu_choice == 1):
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif(menu_choice == 2):
            print(decode(encoded_password))
            print()
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu_choice = int(input("Please enter an option: "))


if __name__ == '__main__':
    main()