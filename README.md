# FileSorterByType

    FileSorterByType is a Python script that organizes files from a source folder into different destination folders based on their types (audio, video, images, etc.), simplifying file management.

## Usage

1. **Clone the Repository:**
    git clone https://github.com/LeoCYLam/FileSorterByType.git

2. **Navigate to the Project Directory:**
    cd FileSorterByType

3. **Configure Source and Destination Folders:**
    Open the script (`file_sorter.py`) and fill in the following variables:

    ```python
    source_folder = "path/to/your/source/folder"
    dest_folder_audio = "path/to/your/audio/destination"
    dest_folder_video = "path/to/your/video/destination"
    dest_folder_image = "path/to/your/image/destination"
    dest_folder_other = "path/to/your/other/destination"

4. **Run the Script:**
    python file_sorter.py

    The script will scan the source folder, categorize files, and move them to their respective destination folders.

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! If you find issues or have suggestions for improvements, feel free to [open an issue](https://github.com/LeoCYLam/FileSorterByType/issues) or [submit a pull request](https://github.com/LeoCYLam/FileSorterByType/pulls).

## License

This project is licensed under the [MIT License](LICENSE).
