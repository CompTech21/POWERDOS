import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    clear_screen()
    print('Please enter your login information:')
    username = input('Username: ')
    password = input('Password: ')
    os.makedirs('data', exist_ok=True)
    with open('data/users.txt', 'a') as file:
        file.write(f'{username},{password}\n')
    print('Login successful!')
    time.sleep(2)
    starting()

def main():
    os.system('color 17')
    clear_screen()
    print('Welcome to PowerDOS setup')
    print('------------------------')
    print('')
    while True:
        choice = input('To continue, type "yes". To exit, type "exit the setup": ')
        if choice == 'yes':
            select_disk()
            break
        elif choice == 'exit the setup':
            exit_setup()
            break
        else:
            print('\033[91mInvalid choice. Please try again.\033[0m')
            input('Press Enter to continue...')
            clear_screen()

def select_disk():
    clear_screen()
    while True:
        choice = input('Please choose the disk (C/D): ')
        if choice.lower() == 'c' or choice.lower() == 'd':
            login()
            break
        else:
            print('\033[91mInvalid choice. Please try again.\033[0m')
            input('Press Enter to continue...')
            clear_screen()

def starting():
    clear_screen()
    print('Starting POWERDOS...')
    time.sleep(2)
    os.system('python system.py')

def exit_setup():
    clear_screen()
    print('Exiting setup...')
    time.sleep(2)

if __name__ == '__main__':
    main()
