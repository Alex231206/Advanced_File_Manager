import os, shutil

def delete_files_by_location():
    try:
        filenum = int(input('Enter the number of files you want to delete: '))

    except ValueError:
        print('You have entered incorrect data\n')
        delete_files_by_location()

    else:
        for index in range(filenum):
            path_to_folder = input('Enter absolute path to directory which contains file you want to delete: ')

            if os.path.isabs(path_to_folder):
                filename = input('Enter the full name of file: ')

                if filename in os.listdir(path_to_folder):
                    os.unlink(f'{path_to_folder}\\{filename}')

                else:
                    print(f"Directory {path_to_folder} doesn't contain file {filename}\n")
                    continue

            else:
                print(f"Path {path_to_folder} doesn't exist\n")
                continue

    print('Program has successfully finished running')