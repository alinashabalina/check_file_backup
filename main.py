from utils import File

with File("/Users/alinashabalina/check_file_backup/files_to_change", "/Users/alinashabalina"
                                                                     "/check_file_backup/backup",
          "lala.py", "string") as file:
    print("ready")
