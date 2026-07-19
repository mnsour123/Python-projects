# File Organizer

A simple Python script that organizes files in a folder either by **file type** (Images, Documents, Videos, etc.) or by **last modified date** (grouped into `YYYY-MM` folders).

## Requirements

- Python 3.6+
- No external libraries needed (uses only the standard library)

## Usage

1. Save the script as `file_organizer.py`
2. Run it from your terminal:

   ```bash
   python file_organizer.py
   ```

3. When prompted:
   - Enter the full path of the folder you want to organize
   - Choose whether to organize by `type` or `date`

### Example

```
Enter the folder path to organize: C:\Users\You\Downloads
Organize by 'type' or 'date'? type
Moved: report.pdf -> Documents/
Moved: photo.png -> Images/
Moved: song.mp3 -> Audio/
Done!
```

## How It Works

### Organize by Type

Files are sorted into subfolders based on their extension:

| Category      | Extensions                                    |
| ------------- | --------------------------------------------- |
| Images        | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp    |
| Documents     | .pdf, .doc, .docx, .txt, .odt, .rtf           |
| Spreadsheets  | .xls, .xlsx, .csv                             |
| Presentations | .ppt, .pptx                                   |
| Videos        | .mp4, .mov, .avi, .mkv, .webm                 |
| Audio         | .mp3, .wav, .flac, .aac                       |
| Archives      | .zip, .rar, .7z, .tar, .gz                    |
| Code          | .py, .js, .html, .css, .java, .cpp, .c, .json |
| Other         | anything not listed above                     |

You can edit the `FILE_CATEGORIES` dictionary at the top of the script to add, remove, or change extensions and categories.

### Organize by Date

Files are grouped into folders named by their **last modified date**, formatted as `YYYY-MM` (e.g. `2026-07`).

To change the date grouping, edit the `date_format` parameter in the `organize_by_date()` function:

- `"%Y-%m"` → Monthly folders (default), e.g. `2026-07`
- `"%Y-%m-%d"` → Daily folders, e.g. `2026-07-19`
- `"%Y"` → Yearly folders, e.g. `2026`

## Notes

- If a file with the same name already exists in the destination folder, the script automatically renames it (e.g. `photo_1.jpg`) instead of overwriting it.
- The script only processes files in the top-level folder — it does **not** look inside subfolders.
- Files are **moved**, not copied. Make a backup first if you want to be safe.

## Possible Improvements

- Add a `--recursive` flag to process subfolders too
- Use file creation date instead of modified date
- Add command-line arguments so it can run without prompts (e.g. `python file_organizer.py --path ./Downloads --mode type`)
