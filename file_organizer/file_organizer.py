import os
import shutil
from datetime import datetime
from pathlib import Path


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"],
}


def get_category(extension):
    """Return the category name for a given file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Other"


def organize_by_type(folder_path):
    """Move files into subfolders named after their file type category."""
    folder = Path(folder_path)

    for item in folder.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            dest_folder = folder / category
            dest_folder.mkdir(exist_ok=True)

            dest_path = dest_folder / item.name
            dest_path = get_unique_path(dest_path)

            shutil.move(str(item), str(dest_path))
            print(f"Moved: {item.name} -> {category}/")


def organize_by_date(folder_path, date_format="%Y-%m"):
    """Move files into subfolders named after their last modified date."""
    folder = Path(folder_path)

    for item in folder.iterdir():
        if item.is_file():
            mod_time = os.path.getmtime(item)
            date_str = datetime.fromtimestamp(mod_time).strftime(date_format)

            dest_folder = folder / date_str
            dest_folder.mkdir(exist_ok=True)

            dest_path = dest_folder / item.name
            dest_path = get_unique_path(dest_path)

            shutil.move(str(item), str(dest_path))
            print(f"Moved: {item.name} -> {date_str}/")


def get_unique_path(dest_path):
    """Avoid overwriting files with the same name by appending a number."""
    if not dest_path.exists():
        return dest_path

    base = dest_path.stem
    ext = dest_path.suffix
    parent = dest_path.parent
    counter = 1

    while True:
        new_path = parent / f"{base}_{counter}{ext}"
        if not new_path.exists():
            return new_path
        counter += 1


if __name__ == "__main__":
    target_folder = input("Enter the folder path to organize: ").strip()

    if not os.path.isdir(target_folder):
        print("Invalid folder path.")
    else:
        mode = input("Organize by 'type' or 'date'? ").strip().lower()

        if mode == "type":
            organize_by_type(target_folder)
        elif mode == "date":
            organize_by_date(target_folder)
        else:
            print("Invalid choice. Please enter 'type' or 'date'.")

        print("Done!")
