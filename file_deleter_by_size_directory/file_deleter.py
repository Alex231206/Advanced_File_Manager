import os, shutil, pprint, send2trash
from datetime import datetime

def delete_files_by_its_sizes():

    path: str = input('Enter absolute path to folder: ')

    if os.path.isabs(path):
        try:
            max_size: float = float(input('Enter maximum size of files (in Megabytes) to delete: '))

        except ValueError:
            print('Incorect data!\n')


        else:
            files_list: list = []

            for foldername, subfolders, files in os.walk(path):
                for file in files:
                    file_location = f'{foldername}\\{file}'
                    file_extension = file[file.rfind('.') + 1:]
                    file_size = os.path.getsize(file_location) / 1024 / 1024

                    if file_size > max_size:
                        each_file_dict: dict = {
                            'FileName': '',
                            'Location': '',
                            'Size (in Megabytes)': '',
                        }

                        each_file_dict['FileName'] = file
                        each_file_dict['Location'] = file_location
                        each_file_dict['Size (in Megabytes)'] = file_size

                        files_list.append(each_file_dict)

                        send2trash.send2trash(file_location)

            pprint.pprint(files_list)
            print()


            print('The program has successfully finished running')


    else:
        print(f"The path {path} doesn't exist\n")