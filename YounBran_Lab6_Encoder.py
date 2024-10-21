#Simple program that encodes and decodes strings of digits of length 8

#Function developed by Brandon Young
def password_encoder(password): #Password encoder that takes in 8-digit string and returns with each value shifted up 3
    encoded_password = ''
    for element in str(password):
        element = int(element) + 3
        if element >= 10:
            element = str(element)
            element = element[1]
        encoded_password += str(element)
    return encoded_password


def password_decoder(encoded_password): #Password decoder that takes in 8-digit string and returns with each value shifted down 3
    decoded_password = ''

    for element in encoded_password:
        decoded_password += str(int(element) - 3)

    return decoded_password


def main():
    user_password = '00000000'
    encoded_password = '00000000'
    while True:

        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        user_input = int(input('Please enter an option: '))

        if user_input == 1: #1.User picked encode password

            user_password = str(input('Please enter your password to encode: '))
            if len(user_password) == 8:
                encoded_password = password_encoder(user_password)
                print('Your password has been encoded and stored!\n')
            else:
                print('Password must be of length 8')

        if user_input == 2: #2.User picked decode password

            password_decoder(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {user_password}\n')

        if user_input == 3: #3.User picked quit program

            break



if __name__ == "__main__":

    main()
