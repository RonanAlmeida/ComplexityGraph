"""
Functions for getting lists of files and folders (directories) in Python 3.4+

Functions:

    get_filenames(dir='.', pattern='*')

    get_subdirectories(dir='.')

R. Linley
2019-09-29
"""

import pathlib, os


def get_filenames (dir='.', pattern='*'):
    """Returns a list of filenames from the directory specified by dir,
    matching pattern, which may include wildcards.

    Parameters:

        dir (str, default '.'): The directory from which filenames should be
            extracted. (The default, '.', is the current directory/folder.)
            Prints an error message and returns an empty list if dir is not
            reachable for any reason (e.g., it doesn't exitst).

        pattern (str, default '*'): E.g., '*.txt', the template used for
            deciding which filenames to include in the returned list.
            (The default, '*', matches all files.)
    """
    try:
        if dir != '.':
            os.chdir(dir);
        return [str(p) for p in pathlib.Path('.').glob(pattern) if p.is_file()]
    except OSError:
            print ('Error: Directory',dir,'not accessible.')
            return []

def get_subdirectories (dir='.'):
    """Returns a list of subdirectories of the directory specified by dir.

    Parameter:

        dir (str, default '.'): The directory from which subdirectories should
            be extracted. (The default, '.', is the current
            subdirectory/folder.)
            Prints an error message and returns an empty list if dir is not
            reachable for any reason (e.g., it doesn't exitst).
    """
    try:
        if dir != '.':
            os.chdir(dir);
        return [str(p) for p in pathlib.Path('.').iterdir() if not p.is_file()]
    except OSError:
        print ('Error: Directory',dir,'not accessible.')
        return []

def main():
    """Test code for module."""
    print('All files in current directory:',end='\n\t')
    print('\n\t'.join(get_filenames()))
    print('\nAll text files in current directory:',end='\n\t')
    print('\n\t'.join(get_filenames(pattern='*.txt')))
    print('\nAll Python files in current directory:',end='\n\t')
    print('\n\t'.join(get_filenames(pattern='*.py')))
    print('\nThis should fail (bogus directory):',end='\n\t')
    print('\n\t'.join(get_filenames('fubar','*.py')))

    print('All subdirectories of the current directory:',end='\n\t')
    print('\n\t'.join(get_subdirectories()))
    print('\nAll subdirectories of the parent directory:',end='\n\t')
    print('\n\t'.join(get_subdirectories('..')))
    print('\nAll subdirectories of the root directory:',end='\n\t')
    print('\n\t'.join(get_subdirectories('/'))) # of root directory

    print('\nAll files in the root directory:',end='\n\t')
    print('\n\t'.join(get_filenames()))

if __name__ == '__main__':
    main()

