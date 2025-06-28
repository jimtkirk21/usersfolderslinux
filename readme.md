User Home Directory Lister
Description
This Python script provides a simple utility to list the files and subdirectories within a specified user's home directory. It categorizes the contents into separate lists for files and directories, offering a quick overview of the top-level structure.

Features
Directory Listing: Scans a specified user's home directory.

Categorization: Separates items into lists of files and directories.

Path Generation: Provides full paths for each identified item.

Technologies Used
Python 3.x

os module: Standard Python library for interacting with the operating system, including file system operations.

Setup & Installation
To set up and run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/your-username/user-home-directory-lister.git
cd user-home-directory-lister

(Replace your-username with your actual GitHub username)

No external Python libraries are required beyond the standard library.

Usage
To run the script:

Open the list_home_content.py file.

Modify the print(display_directories_files("adambulenda")) line at the bottom of the script to replace "adambulenda" with the actual username of the home directory you wish to inspect.

Important Note: This script accesses a user's home directory. Ensure you have the necessary permissions to read the contents of the specified directory. On multi-user systems, you might need elevated privileges or only be able to access your own home directory.

Execute the Python script:

python list_home_content.py

Console Output: The script will print a dictionary containing two lists: one for files and one for directories found directly within the specified user's home folder.

Project Structure
user-home-directory-lister/
├── list_home_content.py
├── README.md
└── .gitignore

Supporting Files
list_home_content.py
This is the main Python script containing the display_directories_files function and the execution call.

import os

def display_directories_files(user):
    # Construct the path to the user's home directory
    # This assumes a Unix-like system where /Users/user is the home directory structure.
    # For Windows, this path might need to be adjusted (e.g., using os.path.expanduser('~'))
    # or passed as a direct path argument.
    home_path = f'/Users/{user}'
    
    # List all items (files and directories) in the specified home directory
    home_items = os.listdir(home_path)
    
    # Initialize a dictionary to store categorized content
    home_content = {"files": [], "directories": []}
    
    # Create full paths for each item
    home_paths = [os.path.join(home_path, item) for item in home_items]

    # Iterate through the full paths and categorize them
    for path in home_paths:
        if os.path.isdir(path):
            home_content['directories'].append(path)
        # Check if it's a file. Note: os.path.isfile will return False for directories and symlinks to directories.
        if os.path.isfile(path):
            home_content['files'].append(path)
    return home_content

# Example usage: Replace "adambulenda" with the actual username of the home directory you want to list.
print(display_directories_files("adambulenda"))

requirements.txt
This project does not require any external Python libraries beyond the standard library modules (os). Therefore, the requirements.txt file would be empty or not needed for this specific script.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.