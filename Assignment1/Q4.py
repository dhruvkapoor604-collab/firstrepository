import os
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        # Check if source directory exists
        if not os.path.isdir(source_dir):
            print(f"❌ Source directory does not exist → {source_dir}")
            return

        # Check if destination directory exists
        if not os.path.isdir(dest_dir):
            print(f"❌ Destination directory does not exist → {dest_dir}")
            return

        files_copied = 0

        # Loop through files in source
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            if os.path.isfile(source_path):

                # If file already exists → add timestamp
                if os.path.exists(dest_path):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_{timestamp}{ext}"
                    dest_path = os.path.join(dest_dir, new_filename)

                shutil.copy2(source_path, dest_path)
                print(f"✔ Copied: {filename}")
                files_copied += 1

        if files_copied == 0:
            print("\n⚠ No files found in source folder.")
        else:
            print("\n🎉 Backup completed successfully!")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


# ---- Input from user ----
source = input("Enter Source Directory Path: ").strip().replace("\\", "/")
dest = input("Enter Destination Directory Path: ").strip().replace("\\", "/")

backup_files(source, dest)
