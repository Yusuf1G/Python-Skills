import os

directory = r'C:\\Users\\yusuf\\Downloads\\Compressed\\Complete-Python-3-Bootcamp-master\\Complete-Python-3-Bootcamp-master'
output_file = r'C:\\Users\\yusuf\\Documents\\Git\\Python\\Web Scraping Project\\directory_listing2.txt'

def list_files(directory, output_file):
    with open(output_file, 'w') as file:
        for folder, sub_folders, files in os.walk(directory):
            # Get the base name of the current folder
            folder_name = os.path.basename(folder)
            
            # Only process the main folders
            if folder == directory:
                continue

            file.write(f'{folder_name}\n')
            file.write('\n')

            for f in files:
                if f.endswith('.ipynb'):
                    file.write(f'\t{f}\n')

            # Write a newline for better readability
            file.write('\n') 

list_files(directory, output_file)