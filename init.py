from handlers import TerminalHandlers
import sys

def index():
    path = 'C:/'
    handlers = TerminalHandlers(path=path)

    while True:
        path = handlers.terminal.path
        command = input(f'{path}>').split()

        if len(command) == 1:
            command.append(None)

        match command:
            case 'dir' as command, *args:
                handlers.scan_dir()

            case 'cd' as command, dir:
                dir = formatingUnderScores(dir)
                handlers.change_dir(dir=dir)

            case 'mkdir' | 'md' as command, name:
                name = formatingUnderScores(name)
                if name == None:
                    print('You haven\'t typed name for thin function')
                    sys.exit(1)
                handlers.create_dir(name=name)
            
            case 'echo' as command, name:
                name = formatingUnderScores(name)
                if name == None:
                    print('You haven\'t typed name for thin function')
                    sys.exit(1)
                handlers.create_txt(name=name)
            
            case 'rename' as command, *args:
                if len(args) != 2:
                    print('Incorrect number of arguments for this command\nYour command should look like this: rename "old_name"""new_name')
                    sys.exit(1)
                args[0] = formatingUnderScores(args[0])
                args[1] = formatingUnderScores(args[1])
                handlers.rename_file(old_name=args[0], new_name=args[1])
            
            case 'remove' as command, name:
                name = formatingUnderScores(name)
                if name == None:
                    print('You haven\'t typed name for this function')
                    sys.exit(1)
                handlers.remove(name=name)

            case 'read' as command, name:
                name = formatingUnderScores(name)
                if name == None:
                    print('You haven\'t typed name for this function')
                    sys.exit(1)
                handlers.read(name=name)
            
            case _:
                print('Invalid command')
            

def formatingUnderScores(name: str) -> str:
        return name.replace('_', ' ')