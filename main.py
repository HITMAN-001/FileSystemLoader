import FileSystemLoader
import os


class main:
    def __init__(self):
        """
        Initilize the main function.
        """
        self.root_path = None
        self.max_depth = None
        self.lower_bound = None
        self.upper_bound = None
        self.number_of_files = None

    def set_root_path(self):
        """
        Get the root path where the directoey structure will be created
        """
        path = input(
            "Enter the root_path (In which the Directories will be loaded): ")
        self.root_path = os.path.join("c:\\BillionFileDirectory", path)

    def set_max_depth(self):
        """
        Get the max depth of the directory structure
        """
        self.max_depth = int(input("Enter the amx_depth like 3/4/5... : "))

    def set_lower_bound(self):
        """
        Get the lowest size of the files that you want in the directories.
        """
        self.lower_bound = int(
            input("Enter the lower bound size in integer (5000 ~ 1kb): "))

    def set_upper_bound(self):
        """
        Get the highest size of the file that you want to in the directories.
        """
        self.upper_bound = int(
            input("Enter the upper bound size in integer (10000000 ~ 1mb): "))

    def set_number_of_files_per_directory(self):
        """
        Get the highest size of the file that you want to in the directories.
        """
        self.number_of_files = int(
            input("Enter the number of files per directory: "))

    def run(self):
        """
        This is the function that you can use to run the File System Loader.
        """
        fs = FileSystemLoader.FileSystemLoader(
            root_path=self.root_path, max_depth=self.max_depth, lower_bound=self.lower_bound,
            upper_bound=self.upper_bound, number_of_files_per_dir=self.number_of_files)
        fs.create_directory_structure_and_file()
    
    def get_root_path(self):
        return self.root_path

    def get_max_depth(self):
        return self.max_depth
    
    def get_lower_bound(self):
        return self.lower_bound
    
    def get_upper_bound(self):
        return self.upper_bound
    
    def get_number_of_files_per_directory(self):
        return self.number_of_files
    
"""
if __name__ == "__main__":
    main = main()
    main.get_root_path()
    main.get_lower_bound()
    main.get_upper_bound()
    main.get_max_depth()
    main.get_number_of_files_per_directory()
    main.run()
"""