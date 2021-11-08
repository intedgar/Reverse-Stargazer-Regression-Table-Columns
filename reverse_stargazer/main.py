import reverse_stargazer_table as rst
import os

load_path = rst.ask_for_file_location()
store_path = rst.ask_for_save_file_location()

files = os.listdir(rst.load_path)
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
    columns_number = rst.get_columns_number(latex_code)
    #save the new file
    fhandle = open(f"{store_path}/{txt_files[i]}", 'w+') 
    fhandle.write(rst.new_latex_code(latex_code, columns_number))
    fhandle.close()
print(f"Complete. Changed {len(txt_files)} file(s). You can find them in the following directory: \n{store_path}\n")
if (len(txt_files)<10):
    print("File(s) changed: ")
    for file in txt_files:
        print(file)
