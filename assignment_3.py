# File handling with exceptions handled
import os


def create_file(file_name):
    try:
        with open(file_name, 'w') as f:
            f.write('My name is Animesh\n')
        print('File ' + file_name + ' created.')
    except IOError as e:
        print(f'Error: {e}')
    except PermissionError as e:
        print(f'Error: {e}')
    except OSError as e:
        print(f'Error: {e}')
    except EOFError as e:
        print(f'Error: {e}')
    finally:
        f.close()
        print('In finally block which always executes no matter what')


def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError as e:
        print(f'Error: {e}')
    except FileNotFoundError as e:
        print(f'Error: {e}')
    except IsADirectoryError as e:
        print(f'Error: {e}')
    except PermissionError as e:
        print(f'Error: {e}')
    except OSError as e:
        print(f'Error: {e}')
    except EOFError as e:
        print(f'Error: {e}')
    finally:
        f.close()
        print('In finally block which always executes no matter what')


def append_file(file_name, text):
    try:
        with open(file_name, 'a') as f:
            f.write(text)
        print('Text appended to file ' + file_name)
    except IOError as e:
        print(f'Error: {e}')
    except FileNotFoundError as e:
        print(f'Error: {e}')
    except IsADirectoryError as e:
        print(f'Error: {e}')
    except PermissionError as e:
        print(f'Error: {e}')
    except OSError as e:
        print(f'Error: {e}')
    except EOFError as e:
        print(f'Error: {e}')
    finally:
        f.close()
        print('In finally block which always executes no matter what')


def rename_file(file_name, new_file_name):
    try:
        os.rename(file_name, new_file_name)
        print('File renamed to ' + new_file_name)
    except IOError as e:
        print(f'Error: {e}')
    except FileNotFoundError as e:
        print(f'Error: {e}')
    except IsADirectoryError as e:
        print(f'Error: {e}')
    except PermissionError as e:
        print(f'Error: {e}')
    except OSError as e:
        print(f'Error: {e}')
    except EOFError as e:
        print(f'Error: {e}')
    finally:
        print('In finally block which always executes no matter what')


def delete_file(file_name):
    try:
        os.remove(file_name)
        print('File deleted')
    except IOError as e:
        print(f'Error: {e}')
    except FileNotFoundError as e:
        print(f'Error: {e}')
    except IsADirectoryError as e:
        print(f'Error: {e}')
    except PermissionError as e:
        print(f'Error: {e}')
    except OSError as e:
        print(f'Error: {e}')
    except EOFError as e:
        print(f'Error: {e}')
    finally:
        print('In finally block which always executes no matter what')


filename = "animesh.txt"
new_filename = "animesh_sinha.txt"
create_file(filename)
read_file(filename)
append_file(filename, "This is the text I added.\n")
read_file(filename)
rename_file(filename, new_filename)
read_file(new_filename)
delete_file(new_filename)