import re
import os

# function definitions
def get_columns_number(latex_code):
    paragraphs = latex_code.split("\\hline \\\\[-1.8ex]")
    pattern = re.compile("multicolumn[{](\d)[}]")
    re.search("multicolumn[{](\d)[}]", paragraphs[1])
    matches = pattern.findall(paragraphs[1])
    column_size = matches[0]
    return column_size


def reorder_row(row):
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


def reorder_paragraph(paragraph):
    rows = paragraph.split('\n')
    new_paragraph = ""
    for i in range(len(rows)-1):
        new_row = reorder_row(rows[i])
        if new_row != "":
            new_paragraph = new_paragraph + new_row + '\n'
    return new_paragraph


def new_latex_code(latex_code):
    paragraphs = latex_code.split("\\hline \\\\[-1.8ex]")
    new_latex_code = ""
    for i in range(2):
        new_latex_code = new_latex_code + paragraphs[i] + "\\hline \\\\[-1.8ex]"
    for i in range(2, 5):
        new_latex_code = new_latex_code + reorder_paragraph(paragraphs[i]) + "\\hline \\\\[-1.8ex]"
    for i in range(5, len(paragraphs)-1):
        new_latex_code = new_latex_code + paragraphs[i] + "\\hline \\\\[-1.8ex]"
    new_latex_code = new_latex_code + paragraphs[-1]
    return new_latex_code


# Loop over each of the files in files, apply the new_latex_code function and save the new file

for i in range(len(files)):
    #load file
    fhandle = open(f"{path}/{files[i]}",'r')
    latex_code = fhandle.read()
    fhandle.close()
    #set up variable for latex_code
    columns_number = get_columns_number(latex_code)
    #save the new file
    fhandle = open(f"C:/Users/ESchu/Desktop/Studium/Master/Thesis/Regression Tables/check/{files[i]}", 'w+')
    fhandle.write(new_latex_code(latex_code))
    fhandle.close()






