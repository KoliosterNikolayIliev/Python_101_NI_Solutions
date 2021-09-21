import json


def fetch_users():
    with open('users.json', 'r') as f:
        users = json.loads(f.read())

        return users


def list_users():
    users = fetch_users()
    print(users)


def create_user():
    first_name = input('First name: ')
    last_name = input('Last name: ')

    users = fetch_users()
    users.append({'first_name': first_name, 'last_name': last_name})

    with open('users.json', 'w') as f:
        f.write(json.dumps(users))


def help():
    help_text = '''
    Avalable commands:
        - "create" or "c" - Create user
        - "list" or "l" - List users
        - "exit" or "e" - Exit
        - "help" or "h" - show current dialog
    '''
    print(help_text)


def unknown_command(command: str):
    print(f'Unknown command: {command}')


def main():
    while True:
        command = input('Enter command: ')

        if command in ['h', 'help']:
            help()

        elif command in ['l', 'list']:
            list_users()

        elif command in ['c', 'create']:
            create_user()

        elif command in ['e', 'exit']:
            break

        else:
            unknown_command(command)


if __name__ == '__main__':
    main()
