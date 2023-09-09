import requests, os
from bs4 import BeautifulSoup
from datetime import datetime


def print_html_code():
    url = input('Enter the url of website: ')

    try:
        req = requests.get(url)

    except requests.exceptions.MissingSchema:
        print(f"\nWebsite url '{url}' doesn't exist. Would you like to continue or to quit parser program (print 'continue' or 'quit'")

        user_choice = input('Enter your choice: ')

        if user_choice == 'continue':
            print()
            print_html_code()

        elif user_choice == 'quit':
            print('\nThe program has been disrupted.\tSee you soon!')
            quit()

        else:
            print('\nYou have entered incorrect choice\n')
            print_html_code()

    else:
        if req.status_code == 200:
            bs = BeautifulSoup(req.text, 'html.parser')

            print("\nThe program has received html-code of the website. What would you like to do with it \n\t('save' - to save code in a file, 'print' - to print code, 'both' - to do both of them)?")

            user_choice = input('Enter your choice: ')

            if user_choice == 'print':
                print('\n\n\n', bs, '\n\n\n')
                print_html_code()

            elif user_choice == 'save':
                absolute_path = input('Enter absolute path to directory you want to save file with code in: ')

                if os.path.isabs(absolute_path):
                    os.chdir(absolute_path)

                    file_name = input('Input the name of txt file you want to save code in: ')

                    with open(file_name, 'a', encoding = 'utf-8') as file:
                        file.write(f'Request {datetime.today()}\n')
                        file.write(f'Website {url}')
                        file.write(str(bs))
                        file.write('\n\n\n\n')


                else:
                    print('You have entered incorrect path to directory\n')
                    print_html_code()


            elif user_choice == 'both':
                print(bs, '\n')

                absolute_path = input('Enter absolute path to directory you want to save file with code in: ')

                if os.path.isabs(absolute_path):
                    os.chdir(absolute_path)

                    file_name = input('Input the name of txt file you want to save code in: ')

                    with open(file_name, 'a', encoding='utf-8') as file:
                        file.write(f'Request {datetime.today()}\n')
                        file.write(f'Website {url}')
                        file.write(str(bs))
                        file.write('\n\n\n\n')


                else:
                    print('You have entered incorrect path to directory\n')
                    print_html_code()


        elif req.status_code == 404:
            print('Something has gone wrong (error 404 has been occurred)\n')

    finally:
        print('Program has finished running')