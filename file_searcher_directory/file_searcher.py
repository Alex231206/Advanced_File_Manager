import os, shutil
import datetime
from pprint import pprint


def search_for_files():
    abs_path: str = input('Enter the absolute path to the directory for searching: ')

    try:
        os.chdir(abs_path)

    except FileNotFoundError:
        print('The path you entered is incorrect')


    else:
        files_extensions: str = input(
            'Enter the extensions of files you want to receive (separated by a space): ')

        files_extensions_list: list = files_extensions.split()

        result_location: str = input(
            'Enter the location of the future results of the program (absolute path): ')

        if os.path.isabs(result_location):
            files_dict: dict = {}
            all_files_list: list = []

            date = datetime.datetime.today()

            try:
                os.makedirs(
                    f'{result_location}\\result_{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}-{date.second}')

            except FileExistsError:
                print('The directory for saving results already exists. Delete it or rename it\n')

            else:
                for extension in files_extensions_list:
                    files_dict[extension] = []
                    os.chdir(
                        f'{result_location}\\result_{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}-{date.second}')
                    os.makedirs(
                        f'{result_location}\\result_{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}-{date.second}\\{extension}')

                for folder_name, subfolders, filenames in os.walk(abs_path):
                    for file in filenames:
                        for extension in files_extensions_list:
                            if file.endswith(extension):

                                each_file_dict: dict = {
                                    'Filename': '',
                                    'Location': '',
                                    'Size(bytes)': ''
                                }

                                file_location = f'{folder_name}\\{file}'
                                file_size = os.path.getsize(file_location)

                                each_file_dict['Filename'] = file
                                each_file_dict['Location'] = file_location
                                each_file_dict['Size(bytes)'] = file_size

                                files_dict[extension] += [each_file_dict]

                                if file not in all_files_list:
                                    all_files_list.append(file)
                                    files_dict[extension] += [each_file_dict]
                                    shutil.copy(f'{folder_name}\\{file}',
                                                f'{result_location}\\result_{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}-{date.second}\\{extension}')

                os.chdir(
                    f'{result_location}\\result_{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}-{date.second}')

                result = open(f'result.txt', 'w')

                result.write(f'Date: {date}\n')

                try:
                    pprint(files_dict, stream=result)

                except UnicodeEncodeError:
                    result.write("There's a problem with encoding suddenly occured\n")

                else:
                    print('The program has successfully finished running\n')

                finally:
                    result.close()

        else:
            print("The folder you entered didn't exist\n")