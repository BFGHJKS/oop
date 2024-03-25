import os
import time


class File:
    def __init__(self, filename, created_time, updated_time):
        self.filename = filename
        self.created_time = created_time
        self.updated_time = updated_time

    def info(self):
        raise NotImplementedError("Subclass must implement abstract method")


class TextFile(File):
    def __init__(self, filename, created_time, updated_time, line_count, word_count, char_count):
        super().__init__(filename, created_time, updated_time)
        self.line_count = line_count
        self.word_count = word_count
        self.char_count = char_count

    def info(self):
        print(f"File: {self.filename}")
        print(f"Created Time: {self.created_time}")
        print(f"Updated Time: {self.updated_time}")
        print(f"Line Count: {self.line_count}")
        print(f"Word Count: {self.word_count}")
        print(f"Character Count: {self.char_count}")


class ImageFile(File):
    def __init__(self, filename, created_time, updated_time, image_size):
        super().__init__(filename, created_time, updated_time)
        self.image_size = image_size

    def info(self):
        print(f"File: {self.filename}")
        print(f"Created Time: {self.created_time}")
        print(f"Updated Time: {self.updated_time}")
        print(f"Image Size: {self.image_size}")


class ProgramFile(File):
    def __init__(self, filename, created_time, updated_time, line_count, class_count, method_count):
        super().__init__(filename, created_time, updated_time)
        self.line_count = line_count
        self.class_count = class_count
        self.method_count = method_count

    def info(self):
        print(f"File: {self.filename}")
        print(f"Created Time: {self.created_time}")
        print(f"Updated Time: {self.updated_time}")
        print(f"Line Count: {self.line_count}")
        print(f"Class Count: {self.class_count}")
        print(f"Method Count: {self.method_count}")


class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = time.time()
        self.files = {}  # Dictionary to store file objects

    def update_snapshot(self):
        self.snapshot_time = time.time()

    def commit(self):
        self.update_snapshot()
        print("Snapshot updated.")

    def scan_folder(self):
        self.files = {}
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                file_info = os.stat(file_path)
                created_time = time.ctime(file_info.st_ctime)
                updated_time = time.ctime(file_info.st_mtime)
                if filename.endswith('.txt'):
                    with open(file_path, 'r') as file:
                        line_count = sum(1 for line in file)
                        file.seek(0)
                        word_count = sum(len(line.split()) for line in file)
                        file.seek(0)
                        char_count = sum(len(line) for line in file)
                    file_obj = TextFile(filename, created_time, updated_time, line_count, word_count, char_count)
                elif filename.endswith(('.png', '.jpg')):
                    file_obj = ImageFile(filename, created_time, updated_time, "unknown")
                elif filename.endswith(('.py', '.java')):
                    with open(file_path, 'r') as file:
                        line_count = sum(1 for line in file)
                        file.seek(0)
                        class_count = sum(1 for line in file if line.strip().startswith("class "))
                        file.seek(0)
                        method_count = sum(1 for line in file if line.strip().startswith("def "))
                    file_obj = ProgramFile(filename, created_time, updated_time, line_count, class_count, method_count)
                else:
                    file_obj = File(filename, created_time, updated_time)
                self.files[filename] = file_obj

    def info(self, filename):
        if filename in self.files:
            self.files[filename].info()
        else:
            print("File not found.")

    def status(self):
        print("Status:")
        current_time = time.time()
        for filename, file_obj in self.files.items():
            if file_obj.updated_time > self.snapshot_time:
                print(f"{filename} - changed")
            else:
                print(f"{filename} - not changed")

def main():
    folder_path = "path/to/your/folder"
    monitor = FolderMonitor(folder_path)
    
    while True:
        print("\nActions:")
        print("1. commit")
        print("2. info <filename>")
        print("3. status")
        print("4. exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            monitor.commit()
        elif choice.startswith("info"):
            _, filename = choice.split(maxsplit=1)
            monitor.info(filename)
        elif choice == "3":
            monitor.status()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
