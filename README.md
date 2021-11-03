# Reverse-Stargazer-Regression-Table-Columns
This repository contains a short Python script to reverse the columns of one or multiple Stargazer Regression Table(s). You would probably never use it unless when you are passing multiple `omit` and `omit.label` arguments to the `stargazer()` function and find out that this resulted in wrong output in your regression table. This is when it comes in handy. But more on that later.

The stargazer library is an R package that can produce LaTeX code to create well-formatted tables that hold
regression analysis results

More information on the Stargazer library can be found here:
* https://cran.r-project.org/web/packages/stargazer/vignettes/stargazer.pdf
* https://cran.r-project.org/web/packages/stargazer/stargazer.pdf


## Why I created this repository
Stargazer is a great package to make regression tables. However, the current version (5.2.2) has one flaw. When specifying two `omit` and `omit.labels` arguments it sometimes produces wrong outputs in the rows that indicate whether the variables were omitted. Let me give you a code example in R to visualize and replicate the error:
Imagine you have the following data:
```

```

One possible solution to get the right `Yes`/`No` outputs is to pass the regression models in reversed order into the `stargazer()` function. However, this leaves you with the issue that the models do not appear in the order that you originally wanted them to appear in the regression table. This is where the code from this repository comes into play. `reverse_stargazer_table.py` is a Python script that can reverse multiple text files containing LaTeX code and reverse its columns such that the models will appear in the LaTeX Regression Table as originally intended and without the buggy `Yes`/`No` values.

## Sounds great. What do I have to do?
* Set up your `stargazer()` function in R. Make sure to reverse the models like this: `stargazer(model.4, model.3, model.2, model.1, ...)`. Don't forget to also reverse the standard errors if you are using robust standard errors.
* Save the output of the `stargazer()` function as a .txt file. This could be one possible way to do so: ```fileConn<-file("C:/your/file/path/filename.txt")
writeLines(txt, fileConn)
close(fileConn)```
* If you want to reverse the columns of multiple stargazer regression tables at the same time, no problem, just make sure to save them all in the same directory.
* **Attention**: Also make sure that no other .txt files are in the same folder as this will throw an error when executing the code. Other filetypes such as .xlsx etc. should not be a problem. They will just be skipped.
* Next, execute the `reverse_stargazer_table.py` file
* The script will ask for two user inputs that you will have to type in:
    1. The filepath where you have saved the .txt files that include the latex code for the regression tables. For example, your filepath could look like this: `C:/your/file/path/`. You don't have to add the actual file names in the path.
    2. The filepath where you want to save the updated .txt files. **Attention**: If using the same filepath as where the old .txt files were saved, they will be overwritten.
* That's it. Enjoy your Regression Tables with reversed columns order.
