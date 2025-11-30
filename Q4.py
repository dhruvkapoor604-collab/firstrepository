import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        if not os.path.isdir(source_dir):
            print(f"Error: Source directory does not exist → {source_dir}")
            return

        if not os.path.isdir(dest_dir):
            print(f"Error: Destination directory does not exist → {dest_dir}")
            return

        for file_name in os.listdir(source_dir):
            source_path = os.path.join(source_dir, file_name)
            dest_path = os.path.join(dest_dir, file_name)

            # Only copy if it's a file
            if os.path.isfile(source_path):

                # If file already exists → rename with timestamp
                if os.path.exists(dest_path):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name, ext = os.path.splitext(file_name)
                    new_file_name = f"{name}_{timestamp}{ext}"
                    dest_path = os.path.join(dest_dir, new_file_name)

                shutil.copy2(source_path, dest_path)
                print(f"Copied: {file_name}")

        print("\nBackup completed successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python backup.py "source_directory" "destination_directory"')
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    backup_files(source, destination)
