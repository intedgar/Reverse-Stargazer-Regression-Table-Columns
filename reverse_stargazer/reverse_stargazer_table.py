import re
import os
import sys

# function definitions
def get_columns_number(latex_code):
    paragraphs = latex_code.split("\\hline \\\\[-1.8ex]")
    pattern = re.compile("multicolumn[{](\d)[}]")
    re.search("multicolumn[{](\d)[}]", paragraphs[1])
    matches = pattern.findall(paragraphs[1])
    column_size = matches[0]
    return column_size


def reorder_row(row, columns_number):
    if re.search('&', row):
        #split string into a list
        row_bricks = re.split(r"&|\\\\", row)
        #reorder the list
        new_order = list(reversed(range(0, int(columns_number) + 1)))
        new_order.insert(0, 0)
        new_order.pop()
        
        row_bricks = [row_bricks[i] for i in new_order]
        #write modified list into string again
        new_row = ""
        for i in range(len(row_bricks)-1):
            new_row = new_row + row_bricks[i] + "&"
        #add the last brick with
        new_row = new_row + row_bricks[-1] + '\\\\ '
        return new_row
    else:
        return row


def reorder_paragraph(paragraph, columns_number):
    rows = paragraph.split('\n')
    new_paragraph = ""
    for i in range(len(rows)-1):
        new_row = reorder_row(rows[i], columns_number)
        if new_row != "":
            new_paragraph = new_paragraph + new_row + '\n'
    return new_paragraph


def new_latex_code(latex_code, columns_number):
    paragraphs = latex_code.split("\\hline \\\\[-1.8ex]")
    new_latex_code = ""
    for i in range(2):
        new_latex_code = new_latex_code + paragraphs[i] + "\\hline \\\\[-1.8ex]"
    for i in range(2, 5):
        new_latex_code = new_latex_code + reorder_paragraph(paragraphs[i], columns_number) + "\\hline \\\\[-1.8ex]"
    for i in range(5, len(paragraphs)-1):
        new_latex_code = new_latex_code + paragraphs[i] + "\\hline \\\\[-1.8ex]"
    new_latex_code = new_latex_code + paragraphs[-1]
    return new_latex_code


def remove_ending_backslash(path):
    if path.endswith('/') or path.endswith('\\'):
        path = path[:-1]
    return path.replace('\\', '/')

def is_q(input):
    """Check whether user input is "q". If it is "q", then stop the program."""
    if input == "q":
        sys.exit()


# Set up the file paths where to load from and where to store
def ask_for_file_location():
    while (True):
        load_path = remove_ending_backslash(input("Enter the file path where your .txt files with latex code are stored: "))
        is_q(load_path)
        if not os.path.isdir(load_path):
            print('Please enter a valid file path or enter "q" to exit the script.\n')
        else:
            return load_path
def ask_for_save_file_location():
    while (True):
        store_path = remove_ending_backslash(input("Enter the file path where you want to save the transformed .txt files: "))
        is_q(store_path)
        if not os.path.isdir(store_path):
            print('Please enter a valid file path or enter "q" to exit the script.\n')
        else:
            return store_path

def reverse():
    load_path = ask_for_file_location()
    store_path = ask_for_save_file_location()

    files = os.listdir(load_path)
    txt_files = []

    for i in range(len(files)):
        if ".txt" in files[i]:
            txt_files.append(files[i])

    # Loop over each of the files in files, apply the new_latex_code function and save the new file
    for i in range(len(txt_files)):
        #load file
        fhandle = open(f"{load_path}/{txt_files[i]}",'r')
        latex_code = fhandle.read()
        fhandle.close()
        #set up variable for latex_code
        columns_number = get_columns_number(latex_code)
        #save the new file
        fhandle = open(f"{store_path}/{txt_files[i]}", 'w+') 
        fhandle.write(new_latex_code(latex_code, columns_number))
        fhandle.close()
    print(f"Complete. Changed {len(txt_files)} file(s). You can find them in the following directory: \n{store_path}\n")
    if (len(txt_files)<10):
        print("File(s) changed: ")
        for file in txt_files:
            print(file)









