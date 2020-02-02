"""This is the menu module.

This module contains one function for presenting a text menu to a user and
getting a keyboard-entered choice from that menu:

- do_menu()

Author: R. Linley
Date: 2019-01-06
"""

def do_menu (title, choices):
    """Displays a text menu of choices and returns the user's choice. Loops on
    invalid choices. All but the last choice are customizeable and are numbered
    1, 2, and so on. The last choice is always "X. Exit." For example:

        Choose one:

        1. Do something
        2. Do something else
        3. Do some other thing

        X. Exit

        Your choice: 

    Parameters:

    - title, a title for the menu meant to indicate its purpose or an
      instruction for its use. (In the example above, 'Choose one' is
      the value of title.)

    - choices, a list of strings representing the menu choices. These are
      presented in order of occurrence in the list. As numbers are generated
      automatically, these should not appear in the list. (In the example
      above, ['Do something', 'Do something else', 'Do some other thing']
      is the value of choices.)

    Returned value:

    - An integer representing the user's choice if the user selects a numbered
      choice, None if the user selects 'x' or 'X' to exit.
      
    """
    while True:
        print('\n' + title + '\n')
        for choice_num in range(len(choices)):
            print(str(choice_num + 1) + '. ' + choices[choice_num])
        print('\nX. Exit')
        print()
        choice = input("Your choice: ")
        try:
            choice = int(choice)
            if (choice > 0 and choice <= len(choices)):
                return choice
        except ValueError:
            pass
        if choice in ['x','X']:
            return None
        print('\nInvalid choice. Try again.')

if __name__ == '__main__':
    # Test code
    m = ['This', 'That', 'The other thing', 'Something else, again']
    while True:
        c = do_menu('Test Menu',m)
        if c is None:
            break
        print('\nValid choice:', c)
    
    
