import sys
import shutil
import os
import time

def backup(source_dir, dest_dir):
    try:
        # Create destination directory if not exists
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Backup files from source directory to destination directory
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                source_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, os.path.relpath(source_file, source_dir))
                shutil.copy2(source_file, dest_file)

        print("Backup completed successfully.")
    except Exception as e:
        print(f"Error occurred during backup: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup_script.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup(source_directory, destination_directory)
