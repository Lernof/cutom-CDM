from models import Console
import os

class TerminalHandlers:
    def __init__(self, path) -> None:
        # self.path = path
        self.dirs = self.scdir(path)
        self.terminal = Console(path)
        self.files = self.scan_files(path)

    #Uses for set self.dirs
    def scdir(self, path) -> None:
        with os.scandir(path) as entries:
            return [e.name for e in entries if os.path.isdir(e)]

    #Uses for set self.files
    def scan_files(self, path):
        with os.scandir(path) as entries:
            return [e.name for e in entries if e.name.endswith('.txt')]

    #Uses to show dirs in terminal
    def scan_dir(self):
        self.terminal.scandir()

    def change_dir(self, dir: str) -> None:
        if dir not in self.dirs and dir != '..':
            print('There is no such directory')
            return None
        self.terminal.change_dir(dir)
        self.files = self.scan_files(self.terminal.path)
        self.dirs = self.scdir(self.terminal.path)

    
    def create_dir(self, name:str) -> None:
        if name in self.dirs:
            check = input('File is already exist, do you wanna replace it? Y/N: ').lower()
            if check == 'y':
                self.terminal.remove(name=name)
                self.terminal.create_dir(name=name)
                return None
            if check == 'n':
                return None
        self.terminal.create_dir(name=name)
        self.dirs = self.scdir(self.terminal.path)
    
    def create_txt(self, name:str) -> None:
        if name in self.files:
            check = input('File is already exist, do you wanna replace it? Y/N: ').lower()
            if check == 'y':
                self.terminal.remove(name=name)
                self.terminal.create_txt(name=name)
                return None
            if check == 'n':
                return None
        self.terminal.create_txt(name=name)
        self.files = self.scan_files(self.terminal.path)
    
    def rename_file(self, old_name:str, new_name:str) -> None:
        if old_name not in self.files and old_name not in self.dirs:
           print(self.files) 
           print('These is no such file')
           return None
        if new_name in self.files:
            print('File with this name is already exist')
            return None
        self.terminal.rename_file(old_name=old_name, new_name=new_name)
        self.dirs = self.scdir(self.terminal.path)
        self.files = self.scan_files(self.terminal.path)
    
    def remove(self, name:str) -> None:
        if name not in self.dirs and name not in self.files:
            print('There is no such file with this name')
            return None
        self.terminal.remove(name=name)
        self.dirs = self.scdir(self.terminal.path)
        self.files = self.scan_files(self.terminal.path)

    def read(self, name:str) -> None:
        if name not in self.files:
            print('There is no such file')
            return None
        self.terminal.read(name=name)