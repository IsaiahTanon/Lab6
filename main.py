# Isaiah Tanon
def encode(password):
    x = str(password)
    final_list = []
    for i in range(len(x)):
        y = int(x[i])
        final_list += [str(y + 3)]
    global encoded_password
    encoded_password = ''.join(final_list)
    return 'Your password has been encoded and stored!'

# Stephany Jimenez
def decode(password):
    return ''.join([str((int(num) - 3) ) for num in password])

def main():
    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit')
        choice = input('Please enter an option:')
        if choice == '1':
            print(encode(input('Please enter your password to encode:')))
            continue
        if choice == '2':
            print('The encoded password is' + encoded_password +
                  ', and the original password is' + decode(encoded_password) + '.')
        else:
            break


main()

