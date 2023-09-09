import os, shutil

def delete_copies_of_files():
    absolute_path = input('Enter absolute path to directory (copies will be deleted in this folder and in all its subfolders): ')

    if os.path.isabs(absolute_path):
        filelist = []

        for foldername, subfolders, filenames in os.walk(absolute_path):
            for filename in filenames:
                if filename in filelist:
                    os.unlink(f'{foldername}\\{filename}')

                else:
                    filelist.append(filename)