class Folder:
    def __init__(self, name):
        self.name = name
        self.subfolders = [] #list of subfolders (folder objects)
        self.files = [] #list of the file names (strings)

    def add_file(self, file):
        self.files.append(file)
        print('File added')

    def add_subfolder(self, subfolder_name):
        if subfolder_name in [folder.name for folder in self.subfolders]:
            print(f'Subfolder "{subfolder_name}" already exists.')
        else:
            new_subfolder = Folder(subfolder_name)
            self.subfolders.append(new_subfolder)
            print(f'Subfolder "{subfolder_name}" added to folder "{self.name}.')


    def __count_files(self):
        #count files and subfolders in the current folder and its subfolders
        file_count = len(self.files) #files in current folder
        subfolder_count = len(self.subfolders) #count subfolders in current folder

        #recursively count files and subfolders in each subfolder
        for subfolder in self.subfolders:
            file_count += subfolder.__count_files() #recursively add the files in subfolders
        return file_count + subfolder_count

    def __len__(self):
        #total items in this folder: files + subfolders
        return self.__count_files()

    def __eq__(self, other):
        if isinstance(other, Folder):
            return self.name == other.name #if other is a folder instance
        elif isinstance(other, str):
            return self.name == other #if other is a string
        return False

    def __str__(self, level=0):
        indent = "  " * level #level represents depth of folder in the hierarchy
        #" " * level creates a string of spaces for indentation
        result = f"{indent}Folder: {self.name}\n"
        for file in self.files:
            result += f"{indent} File: {file}\n"
        for subfolder in self.subfolders:
            result += subfolder.__str__(level + 1) #for each subfolder, it calls the __str__ method recursively, increasing the level by 1
        return result


#interativte menu
class FileManager:
    def __init__(self):
        self.root_folder = Folder("Root Folder") #Always starts with this root folder
        self.current_folder = self.root_folder

    def select_folder(self, folder_name):
        if folder_name == "Root Folder": #special check for navigating back to root folder
            self.current_folder = self.root_folder
            print(f'Now inside folder: {self.current_folder.name}')
            return
        #check if the folder exists in the current folder's subfolders
        for subfolder in self.current_folder.subfolders:
            if subfolder.__eq__(folder_name): #use the __eq__ method
                self.current_folder = subfolder #update the current folder
                print(f'Now inside folder: {self.current_folder.name}')
                return
        print('No subfolder with that name found in the current folder.')

    def start(self):
        while True:
            print("--Menu--")
            print(f"--Current Folder: {self.current_folder.name}--")
            print("1. Add File")
            print("2. Add Subfolder")
            print("3. Select subfolder")
            print("4. Print Folder")
            print("5. Print objects in Folder")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                file_name = input("Enter file name: ")
                self.current_folder.add_file(file_name)
            elif choice == "2":
                subfolder_name = input("Enter subfolder name: ")
                self.current_folder.add_subfolder(subfolder_name)
            elif choice == "3":
                subfolder_name = input("Enter subfolder name to navigate to: ")
                selected_subfolder = self.select_folder(subfolder_name) #call select_folder()
                if selected_subfolder:
                    self.current_folder = selected_subfolder
                    print(f'Now inside folder: {self.current_folder.name}')
            elif choice == "4":
                print(self.root_folder) #prints all files and subfolders inside root folder
            elif choice == "5":
                print(f"Total objects in Root folder: {len(self.root_folder)}")
            elif choice == "6":
                print('Exiting program')
                break
            else:
                print('Invalid choice. Please try again.')


#start program
if __name__ == "__main__":
    file_manager = FileManager()
    file_manager.start()











