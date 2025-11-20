import os
import re

def get_script_directory():
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    return script_directory


directory = get_script_directory()
extension = '.' + input('Enter rom extension ')
as_m3u_folder = input('Add .m3u to the folder name? Y/n ')

files = os.listdir(directory)
files = list(filter( lambda x: x.split('.')[-1] == extension[1:], files ))
hash = {}

for file in files:
    key = file.split(extension)[0]
    key = re.sub(r'\s*\([^)]*\)', '', key)
    
    if key in hash:
        hash[key].append(file)
    else:
        hash[key] = [file]

for key in hash:
    folder_name = f'{key}.m3u'

    if as_m3u_folder.lower() == 'n':
        folder_name = key

    os.mkdir(f'{directory}/{folder_name}')
    
    # write m3u file
    with open(f"{directory}/{folder_name}/{key}.m3u", "w") as file:
        for f in hash[key]:
            file.write(f'{f}\n')
            
    # move roms inside folder
    for f in hash[key]:
        os.rename(f'{directory}/{f}', f'{directory}/{folder_name}/{f}')
    