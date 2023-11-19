import os
import random
import string

# Custom exception to handle missing path


class NoPathProvided(Exception):
    """
    Custom Exception to ask user to provide the path and space for the directory.
    """

    def __init__(
            self, message="Please provide the path for Folder and File creation !!") -> None:
        self.message = message
        super().__init__(self.message)


class FileSystemLoader:
    def __init__(self, root_path=None, max_depth=3, lower_bound=100,
                 upper_bound=10000, number_of_files_per_dir=10):
        # Initialize the root path and maximum depth
        self.root_path = root_path
        self.max_depth = max_depth
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.number_of_files_per_dir = number_of_files_per_dir

    def make_directories(self, i=1):
        """
        Faster method to create directory structure but does not consider depth and
        naive approach for the solution
        The code spans from iteration to iteration to generate the file system till the level 5.

        :returns: None
        """
        if self.root_path is None:
            raise NoPathProvided

        self.path = self.root_path
        for i in range(1, 11):
            # Create first-level directories
            subdir = os.path.join(f"{self.path}\\Dir_{i}")
            os.mkdir(subdir)
            self.create_files(self.number_of_files_per_dir, subdir)

            for j in range(1, 11):
                # Create second-level directories
                subdir = os.path.join(f"{self.path}\\Dir_{i}\\Dir_{i}_{j}")
                os.mkdir(subdir)
                self.create_files(self.number_of_files_per_dir, subdir)

                for k in range(1, 11):
                    # Create third-level directories
                    subdir = os.path.join(
                        f"{self.path}\\Dir_{i}\\Dir_{i}_{j}\\Dir_{i}_{j}_{k}")
                    os.mkdir(subdir)
                    self.create_files(self.number_of_files_per_dir, subdir)

                    for m in range(1, 11):
                        # Create fourth-level directories
                        subdir = os.path.join(
                            f"{self.path}\\Dir_{i}\\Dir_{i}_{j}\\Dir_{i}_{j}_{k}\\Dir_{i}_{j}_{k}_{m}")
                        os.mkdir(subdir)
                        self.create_files(self.number_of_files_per_dir, subdir)

    def create_directory_structure_and_file(self, path=None, depth=1):
        """
        Recursive method for creating the file structure; considers n depth,
        differs in naming slightly

        :param string path: Path where the file system should be generated
        :param int depth: initial depth of the file system

        :returns: None


        """
        if path is None and self.root_path is None:
            raise NoPathProvided

        if path is None:
            path = self.root_path

        if depth >= self.max_depth:
            return

        for i in range(1, 11):  # Create 10 subdirectories at each level
            subdirectory_name = f"Dir_{depth}_{i}"
            subdirectory_path = os.path.join(path, subdirectory_name)

            # Create the subdirectory
            os.makedirs(subdirectory_path)
            # Create files within subdirectories
            self.create_files(self.number_of_files_per_dir, subdirectory_path)

            # Recursively create subdirectories at the next level
            self.create_directory_structure_and_file(
                subdirectory_path, depth + 1)

    def create_files(self, num_files, directory_path):
        """
        Create random files within a directory. No Need to call separately
        as this is automatically called when creating sub directories recursively.
        :param int num_files: Number of files per directory
        :param int depth: Depth of dirctory

        :returns: None

        """
        for i in range(num_files):
            file_name = f"file_{i}.txt"
            file_path = os.path.join(directory_path, file_name)
            file_size = random.randint(self.lower_bound, self.upper_bound)

            # Generate random text content
            content = ''.join(
                random.choices(
                    string.ascii_letters +
                    string.digits,
                    k=file_size))

            # Write the content to the file
            with open(file_path, 'w') as file:
                file.write(content)
