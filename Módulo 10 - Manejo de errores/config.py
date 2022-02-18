def main():
    # try:
    #     open('config.txt')
    # except FileNotFoundError:
    #     print("Couldn't find the config.txt file!")
    # salida = Couldn't find the config.txt file!
 
    # try:
    #     configuration = open('config.txt')
    # except FileNotFoundError:
    #     print("Couldn't find the config.txt file!")  
    # # NO marca que es un folder (se creó el folder como config.txt), marca que no tiene permisos
    # salida = PermissionError: [Errno 13] Permission denied: 'config.txt'
 
    # try:
    #     configuration = open('config.txt')
    # except Exception:
    #     print("Couldn't find the config.txt file!")
    # salida = Couldn't find the config.txt file!

    # try:
    #     configuration = open('config.txt')
    # except FileNotFoundError:
    #     print("Couldn't find the config.txt file!")
    # except IsADirectoryError:
    #     print("Found config.txt but it is a directory, couldn't read it")
    # # NO marca que es un folder (se creó el folder como config.txt), marca que no tiene permisos
    # salida con folder config.txt = PermissionError: [Errno 13] Permission denied: 'config.txt'
    # salida sin folder (ni archivo) config.txt = Couldn't find the config.txt file!

    # try:
    #     configuration = open('config.txt')
    # except FileNotFoundError:
    #     print("Couldn't find the config.txt file!")
    # except IsADirectoryError:
    #     print("Found config.txt but it is a directory, couldn't read it")
    # except (BlockingIOError, TimeoutError):
    #     print("Filesystem under heavy load, can't complete reading configuration file") 
    # salida con folder = PermissionError: [Errno 13] Permission denied: 'config.txt'
    # salida sin folder ni archivo = Couldn't find the config.txt file!

    # try:
    #     configuration = open('config.txt')
    # except FileNotFoundError:
    #     print("Couldn't find the config.txt file!")
    # except IsADirectoryError:
    #     print("Found config.txt but it is a directory, couldn't read it")
    # except (BlockingIOError, TimeoutError):
    #     print("Filesystem under heavy load, can't complete reading configuration file")
    # except PermissionError:
    #     print("Permission denied")
    # salida con folder = Permission denied
    # salida sin folder ni archivo = Couldn't find the config.txt file!

    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")
    # salida sin folder ni archivo = Couldn't find the config.txt file!
    # salida con folder = Found config.txt but couldn't read it

if __name__ == '__main__':
    main()