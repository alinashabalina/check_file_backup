from utils import File

with File("some_path/check_file_backup/files_to_change", "some_path/check_file_backup/backup",
          "file_to_change.py") as file:
    file.open("file_to_change.py", "a")
    file.write("some data to write")
