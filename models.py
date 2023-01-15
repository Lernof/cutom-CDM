import os

class Console:

    def __init__(self, path: str) -> None:
        self.path = path

    #dir or ls
    def scandir(self) -> None:
        with os.scandir(self.path) as entries:
            for entry in entries:
                name = entry.name.replace(' ', '_')
                if os.path.isdir(entry):
                    print('<DIR> ', name)
                else: print(f'\t\t{name}')
    
    #chdir or cd
    def change_dir(self, path: str) -> None:
        self.path = os.path.abspath(os.path.join(self.path, path))
        return os.path.abspath(os.path.join(self.path, path))

    #mkdir of md
    def create_dir(self, name: str) -> None:
        os.mkdir(os.path.join(self.path, name))

    #echo - makes txt file
    def create_txt(self, name: str) -> None:
        with open(os.path.join(self.path, name), 'w') as file:
            file.write(input('write text in file: '))

    #rename
    def rename_file(self, old_name: str, new_name: str) -> None:
        os.rename(os.path.join(self.path, old_name), os.path.join(self.path, new_name))
    
    #remove
    def remove(self, name: str) -> None:
        if name.endswith('.txt'):
            os.remove(os.path.join(self.path, name))
        else: os.rmdir(os.path.join(self.path, name))

    def read(self, name: str) -> None:
        with open(os.path.join(self.path, name), 'r') as file:
            print(file.read())
