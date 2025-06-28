import os
def display_directories_files(user):
    home_items = os.listdir(f'/Users/{user}')
    home_content = {"files": [], "directories": []}
    home_paths = [os.path.join(f'/Users/{user}', item) for item in home_items]

    for path in home_paths:
        if os.path.isdir(path):
            home_content ['directories'].append(path)
        if  os.path.isfile(path):
            home_content['files'].append(path)
    return home_content

print(display_directories_files("adambulenda"))