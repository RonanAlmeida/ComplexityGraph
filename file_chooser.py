"""
A module to allow text-based navigation of directories and the selection of
a filename. The intention is to make it possible to navigate a file system
to select a file fairly easily without resort to a graphical user interface.

Function:
    get_filename(prompt='Choose a file by number:',dir='.', pattern='*')

R. Linley
2019-09-30
"""

from menu import *
from files_and_directories import *
import os


def get_file_path_and_name(prompt='Choose a file by number:',
                           dir='.',
                           pattern='*',
                           allow_cd=False):
    """Provides navigation by numbered menu of a file system. Returns a tuple
    consisting of a path and a file on that path, if one is selected by the
    user, or None if the user chooses
    to exit.

    Parameters:

        prompt (str, default 'Choose a file by number:'): The title appearing
            at the top of the file-choice menu.

        dir (str, default '.' - the current directory): The starting point
            directory navigation.

        pattern (str, default '*' - match all filenames): Filename filter
            (accepts wildcards).

        allow_cd (Boolean, default False): Allow or disallow directory changes.

    Returned values:

        If a file is chosen by the user, a tuple of two strs consisting of
        the path to the file and the file name (i.e., (<path>, <filename>)).

        Otherwise, returns None (implying the user has chosen to exit the
        menu).
            
    """
    while True:
        filenames = get_filenames(dir, pattern)
        if allow_cd:
            print('Current directory is\n' + os.getcwd())
            print()
        print('Showing ' + str(len(filenames)) + \
              ' files matching pattern "' + pattern + '".')
        menu_choices = filenames
        if allow_cd:  # change directory allowed?
            menu_choices += ['<<Change directory>>']  # Yes, add this choice.
        menu_choice = do_menu(prompt, menu_choices)
        print()
        if allow_cd and (menu_choice == len(filenames)):
            dir_names = get_subdirectories(dir)
            print('Current directory is\n' + os.getcwd())
            dir_menu_choice = do_menu('Choose a directory by number:', \
                                      dir_names + ['^^Go up a directory^^'])
            print()
            if dir_menu_choice == len(dir_names) + 1:
                os.chdir('..')
            elif dir_menu_choice != None:
                os.chdir(dir_names[dir_menu_choice - 1])
        elif menu_choice == None:
            return None
        else:
            return os.getcwd(), filenames[menu_choice - 1]  # (path, filename)


def main():
    """Test function for file_chooser module."""
    file_path = get_file_path_and_name(pattern='*.csv')
    if file_path != None:
        print('Path:', file_path[0])
        print('File:', file_path[1])
        print('Both:', os.path.join(file_path[0], file_path[1]))
    print()
    # Repeat, allowing change of directory
    file_path = get_file_path_and_name(pattern='*.csv', allow_cd=True)
    if file_path != None:
        print('Path:', file_path[0])
        print('File:', file_path[1])
        print('Both:', os.path.join(file_path[0], file_path[1]))
    print('Done test.')


if __name__ == '__main__':
    main()
