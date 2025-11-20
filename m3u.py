import os
import re

extension = '.' + input('enter file extension ')
as_m3u_folder = input('As .m3u folder? Y/n ')

files = list(filter( lambda x: x.split('.')[-1] == extension[1:], os.listdir('.')))

hash = {}

for file in files:
    key = file.split(extension)[0]
    key = re.sub(r'\s*\([^)]*\)', '', key)
    
    if key in hash:
        hash[key].append(file)
    else:
        hash[key] = [file]
        
print(hash)

for key in hash:
    folder_name = f'{key}.m3u'

    if as_m3u_folder.lower() == 'n':
        folder_name = key

    os.mkdir(folder_name)
    
    # write m3u file
    with open(f"{folder_name}/{key}.m3u", "w") as file:
        for f in hash[key]:
            file.write(f'{f}\n')
            
    # move roms inside folder
    for f in hash[key]:
        os.rename(f, f'{folder_name}/{f}')
    