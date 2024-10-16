#GitHub addition with git bash

#Function developed by Brandon Young
def password_encoder(password): #password encoder that takes in 8-digit string and returns with each value shifted up
    encoded_password = ''
    for element in str(password):
        element = int(element) + 3
        if element >= 10:
            element = str(element)
            element = element[1]
        encoded_password += str(element)
    return str(encoded_password)


def main():
    while True:

        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        user_input = int(input('Please enter an option: '))

        if user_input == 1: #1. User picked encode password
            user_password = str(input('Please enter your password to encode: '))
            password_encoder(user_password)
            print('Your password has been encoded and stored!\n')

        if user_input == 2: #2. User picked decode password
            pass

        if user_input == 3: #3. User picked quit program
            break



if __name__ == "__main__":

    main()
