def main():
    print('Menu\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit')
    choice = input('Please enter an option:')
    if choice == '1':
        x = str(input('Please enter your password to encode:'))
        final_list = []
        for i in range(len(x)):
            y = int(x[i])
            final_list += [str(y + 3)]
        encoded_password = ''.join(final_list)
        return 'Your password has been encoded and stored!'

print(main())

