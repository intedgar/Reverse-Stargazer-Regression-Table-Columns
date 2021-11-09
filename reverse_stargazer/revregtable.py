import re
import os
import sys

class RegressionTable:
    
    def __init__(self, latex_code):
        self.latex_code = latex_code
        self.columns_count = self.get_columns_count()
    
    def show(self):
        """Method to print the latex_code attribute of the RegressionTable object to the console."""
        print(self.latex_code)

    def get_columns_count(self):
        """Method to extract the number of columns the RegressionTable has."""
        paragraphs = self.latex_code.split("\\hline \\\\[-1.8ex]")
        pattern = re.compile("multicolumn[{](\d)[}]")
        re.search("multicolumn[{](\d)[}]", paragraphs[1])
        matches = pattern.findall(paragraphs[1])
        column_size = matches[0]
        return column_size


    def reorder_row(self, row):
        """Method to reorder a row of a RegressionTable paragraph. Reordering occurs only if the row contains an '&' symbol."""
        if re.search('&', row):
            #split string into a list
            row_bricks = re.split(r"&|\\\\", row)
            #reorder the list
            new_order = list(reversed(range(0, int(self.columns_count) + 1)))
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


    def reorder_paragraph(self, paragraph):
        """Method to reorder a paragraph of a RegressionTable object. Works by calling the reorder_row() method 
        of the RegressionTable object for each row in the paragraph."""
        rows = paragraph.split('\n')
        new_paragraph = ""
        for i in range(len(rows)-1):
            new_row = self.reorder_row(rows[i])
            if new_row != "":
                new_paragraph = new_paragraph + new_row + '\n'
        return new_paragraph


    def new_latex_code(self):
        """Method to generate new latex_code for a RegressionTable object. The method splits the RegressionTable
        latex_code into paragraphs and then calls the reorder_paragraph() method of the RegressionTable object
        for all paragraphs that need to be reordered."""
        paragraphs = self.latex_code.split("\\hline \\\\[-1.8ex]")
        new_latex_code = ""
        for i in range(2):
            new_latex_code = new_latex_code + paragraphs[i] + "\\hline \\\\[-1.8ex]"
        for i in range(2, 5):
            new_latex_code = new_latex_code + self.reorder_paragraph(paragraphs[i]) + "\\hline \\\\[-1.8ex]"
        for i in range(5, len(paragraphs)-1):
            new_latex_code = new_latex_code + paragraphs[i] + "\\hline \\\\[-1.8ex]"
        new_latex_code = new_latex_code + paragraphs[-1]
        return new_latex_code
    
    def reverse(self):
        """Method to reverse the columns of a RegressionTable object. Internally calls the RegressionTable
        object's new_latex_code() method and assigns the return value to the instance's latex_code attribute."""
        self.latex_code = self.new_latex_code()

    def save_to_txt(self, path):
        """Method to save the RegressionTable object's latex_code attribute to a text file."""
        fhandle = open(path, 'w+') 
        fhandle.write(self.latex_code)
        fhandle.close()



def read_reg_tbl_txt(path):
    fhandle = open(path, 'r') 
    latex_code = fhandle.read()
    fhandle.close()
    return RegressionTable(latex_code)


