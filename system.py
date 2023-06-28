import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    os.system('color 17')
    clear_screen()
    print('Welcome to POWERDOS')
    print('-------------------')
    print('Please log in to continue')
    print('')
    while True:
        username = input('Username: ')
        password = input('Password: ')
        if check_login(username, password):
            break
        else:
            print('\033[91mInvalid username or password. Please try again.\033[0m')
            input('Press Enter to continue...')
            clear_screen()
            os.system('color 17')

    print(f'\033[93mWelcome back, {username}!\033[0m')
    print('Type "help" to see a list of commands.')
    print('')
    input('Press Enter to continue...')
    clear_screen()
    os.system('color 17')

    while True:
        command = input(f'{username}@powerdos:~$ ')
        if command == 'help':
            print('Commands:')
            print('---------')
            print('dir - list files and directories')
            print('cd - change directory (in developing)')
            print('calc - open calculator')
            print('echo - print a message')
            print('exit - exit the command prompt')
            print('')
        elif command == 'dir':
            print('Files:')
            print('------')
            print('config.sys')
            print('command.com')
            print('')
            print('Directories:')
            print('------------')
            print('power42')
            print('program files')
            print('')
        elif command == 'cd':
            print('Changing directory...')
            print('')
        elif command == 'echo':
            message = input('Enter a message: ')
            print(message)
            print('')
        elif command == 'exit':
            clear_screen()
            break
        elif command == 'sudo hack powerdos':
            print(f'\033[91mYou can`t do that because you need root permissions!\033[0m')
            print('')
        elif command == 'calc':
            while True:
                expression = input('Enter an expression or "x" to exit: ')
                if expression.lower() == 'x':
                    break
                try:
                    result = eval(expression)
                    print(f'Result: {result}')
                except ZeroDivisionError:
                    print('Error: Division by zero')
                except:
                    print('Error: Invalid expression')
            input('Press Enter to continue...')
            clear_screen()
        else:
            print(f'\033[91mInvalid command: {command}\033[0m')
            print('Type "help" to see a list of commands.')
            print('')
        input('Press Enter to continue...')
        clear_screen()
        os.system('color 17')


def check_login(username, password):
    with open('data/users.txt', 'r') as f:
        for line in f:
            if line.strip() == f'{username},{password}':
                return True
    return False

if __name__ == '__main__':
    main()
