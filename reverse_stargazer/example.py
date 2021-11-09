################################################################################################################
# This is an example demonstration of how the revregtable package can be used to create one or multiple        #
# RegressionTable objects from .txt files, reverse the RegressionTable object's column orders and save them    #
# again as .txt files                                                                                          #
################################################################################################################


# import the libraries needed for this example
import revregtable as rrt
import os

#set up the path where you have stored your .txt files from which you want to generate RegressionTable objects
#here I use a relative path, since the .txt files are stored in a folder "example_txt_files" that is saved in 
# the same directory as example.py
path = "example_txt_files"

# get all the .txt files from the path
files = os.listdir(path)
txt_files = (file for file in files if ".txt" in file)

# loop over all files in txt_files, read the latex_code from each file to create a RegressionTable object, 
# call the object's reverse() method and save it again to a .txt file (here the same path is used). If you 
# would like to see the latex_code of the RegressionTable object before and after applying the reverse() 
# method on the object, just uncomment lines 27 and 29. 
for file in txt_files:
    rt = rrt.read_reg_tbl_txt(f"{path}/{file}")
    #rt.show()
    rt.reverse()
    #rt.show()
    rt.save_to_txt(f"{path}/{file}")

# You will find the updated latex_code .txt file(s) in the following print(f"{path}/{file}")