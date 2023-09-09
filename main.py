import os, shutil, annotation_and_commands
from datetime import datetime
import parser_directory.parser as parser
import file_searcher_directory.file_searcher as file_searcher
import file_deleter_by_size_directory.file_deleter as file_deleter
import file_deleter_by_location.file_deleter_by_location as file_deleter_by_location
import copies_deleter_directory.copies_deleter as copies_deleter

print(annotation_and_commands.print_annotation(), '\n')
print(annotation_and_commands.print_commands())

while True:
    print()
    user_choice = input('Enter your choice: ')

    if user_choice == '0':
        break

    elif user_choice == '1':
        user_command = input('Enter command number: ')

        if user_command == '2':
            file_searcher.search_for_files()

        elif user_command == '3':
            file_deleter.delete_files_by_its_sizes()

        elif user_command == '4':
            file_deleter_by_location.delete_files_by_location()

        elif user_command == '5':
            copies_deleter.delete_copies_of_files()

        elif user_command == '6':
            parser.print_html_code()

        elif user_command == '7':
            continue

        elif user_command == '8':
            print(annotation_and_commands.print_annotation())
            continue

        elif user_command == '9':
            print(annotation_and_commands.print_commands())
            continue

        else:
            print('You have entered incorrect command\n')
            continue

    else:
        print('You have entered incorrect command\n')
        continue



