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
set.seed(42)
x <- rnorm(100)
e <- rnorm(100, mean = 0, sd = 10)
y <- x*1.5+e
countries <- sample(c("CAN", "GRC", "PRT", "THA", "NZL"), size=100, replace=T)
birth_cohorts <- sample(c("1980", "1990", "2000", "2010"), size=100, replace=T)
```
where y is your dependent variable, x your explanatory variable, and countries and birth_cohorts are categorical variables which you want to include in your regressions as fixed effects. Next, you would set up 4 different models from model`1` to `4` including more fixed effects. This could look like this:
```
model1 <- lm(y ~ x)
model2 <- lm(y ~ x + countries - 1)
model3 <- lm(y ~ x + birth_cohorts - 1)
model4 <- lm(y ~ x + countries + birth_cohorts - 1)
```
Of course, you want to not only look at your regression models in R (how boring), but also want to create some beautifully formatted LaTeX tables with Stargazer. The code to do this could look like this:
```
stargazer(model1, model2, model3, model4,
          type = "text")
```
But, omg, this regression table has so many rows, and actually I am only interested in the coefficient for x. How annoying! That's why you would specify the `omit` and `omit.labels` parameters. When entering them, the dummy variables that you have included in the regression do not get shown in the regression table. Pretty cool. This is how the code would look like:
```
stargazer(model1, model2, model3, model4,
          type = "text",
          omit = c("countries", "birth_cohorts"),
          omit.labels = c("Country-fixed effects", "Cohort-fixed effects"))
```

And it gives the following `Output`:
```
=======================================================================================================
                                                     Dependent variable:                               
                      ---------------------------------------------------------------------------------
                                                              y                                        
                              (1)                  (2)                 (3)                 (4)         
-------------------------------------------------------------------------------------------------------
x                           1.772**              1.671*              1.703*               1.587*       
                            (0.877)              (0.866)             (0.868)             (0.853)       
                                                                                                       
Constant                     -0.884                                                                    
                            (0.909)                                                                    
                                                                                                       
-------------------------------------------------------------------------------------------------------
Country-fixed effects          No                  Yes                 No                  Yes         
Cohort-fixed effects           No                  No                  Yes                  No         
-------------------------------------------------------------------------------------------------------
Observations                  100                  100                 100                 100         
R2                           0.040                0.120               0.097               0.177        
Adjusted R2                  0.030                0.064               0.049               0.095        
Residual Std. Error     9.083 (df = 98)      8.916 (df = 94)     8.984 (df = 95)     8.764 (df = 91)   
F Statistic           4.084** (df = 1; 98) 2.133* (df = 6; 94) 2.041* (df = 5; 95) 2.173** (df = 9; 91)
=======================================================================================================
Note:                                                                       *p<0.1; **p<0.05; ***p<0.01
```
But, wait... The row that tells you whether Cohort-fixed effects were included in the regression does not always give you the value that you would have expected. In this example the error is in Model (column) 4 where it shows a `No` even though we all know it should be a `Yes`, because we included it just seconds before in `model 4`. So what to do about it? 
One way to solve this is to wait for an updated version of stargazer which would hopefully solve this. If you don't have the time but need it now, another possible solution to get the right `Yes`/`No` outputs is to pass the regression models in reversed order into the `stargazer()` function like this:
```
stargazer(model4, model3, model2, model1,
          type = "text",
          omit = c("countries", "birth_cohorts"),
          omit.labels = c("Country-fixed effects", "Cohort-fixed effects"))
```
Weirdly enough this solves the issue. And gives you the correct `Yes`/`No` values:
```
=======================================================================================================
                                                     Dependent variable:                               
                      ---------------------------------------------------------------------------------
                                                              y                                        
                              (1)                  (2)                 (3)                 (4)         
-------------------------------------------------------------------------------------------------------
x                            1.587*              1.703*              1.671*              1.772**       
                            (0.853)              (0.868)             (0.866)             (0.877)       
                                                                                                       
Constant                                                                                  -0.884       
                                                                                         (0.909)       
                                                                                                       
-------------------------------------------------------------------------------------------------------
Country-fixed effects         Yes                  No                  Yes                  No         
Cohort-fixed effects          Yes                  Yes                 No                   No         
-------------------------------------------------------------------------------------------------------
Observations                  100                  100                 100                 100         
R2                           0.177                0.097               0.120               0.040        
Adjusted R2                  0.095                0.049               0.064               0.030        
Residual Std. Error     8.764 (df = 91)      8.984 (df = 95)     8.916 (df = 94)     9.083 (df = 98)   
F Statistic           2.173** (df = 9; 91) 2.041* (df = 5; 95) 2.133* (df = 6; 94) 4.084** (df = 1; 98)
=======================================================================================================
Note:                                                                       *p<0.1; **p<0.05; ***p<0.01
```

However, this leaves you with the issue that the models do not appear in the order that you originally wanted them to appear in the regression table. This is where the code from this repository comes into play. `reverse_stargazer_table.py` is a Python script that can reverse multiple text files containing LaTeX code and reverse its columns such that the models will appear in the LaTeX Regression Table as originally intended and without the buggy `Yes`/`No` values.
The final output after having run `reverse_stargazer_table.py` to reverse the columns is a text file with LaTeX code that if you include into a LaTeX file would produce a LaTeX regression table similar to the following output (but obviously in beautiful LaTeX format):
```
=======================================================================================================
                                                     Dependent variable:                               
                      ---------------------------------------------------------------------------------
                                                              y                                        
                              (1)                  (2)                 (3)                 (4)         
-------------------------------------------------------------------------------------------------------
x                           1.772**              1.671*              1.703*               1.587*       
                            (0.877)              (0.866)             (0.868)             (0.853)       
                                                                                                       
Constant                     -0.884                                                                    
                            (0.909)                                                                    
                                                                                                       
-------------------------------------------------------------------------------------------------------
Country-fixed effects          No                  Yes                 No                  Yes         
Cohort-fixed effects           No                  No                  Yes                 Yes         
-------------------------------------------------------------------------------------------------------
Observations                  100                  100                 100                 100         
R2                           0.040                0.120               0.097               0.177        
Adjusted R2                  0.030                0.064               0.049               0.095        
Residual Std. Error     9.083 (df = 98)      8.916 (df = 94)     8.984 (df = 95)     8.764 (df = 91)   
F Statistic           4.084** (df = 1; 98) 2.133* (df = 6; 94) 2.041* (df = 5; 95) 2.173** (df = 9; 91)
=======================================================================================================
Note:                                                                       *p<0.1; **p<0.05; ***p<0.01
```

## Sounds great. What do I have to do?
* Set up your `stargazer()` function in R and assign it to a variable, which I called here `latex_code_as_text`. Also make sure to reverse the models and specify the `type` as `latex`. In summary with the four models from the previous example this could look like this: 
* ```latex_code_as_text <- stargazer(model.4, model.3, model.2, model.1, type="latex", omit = c("countries", "birth_cohorts"), omit.labels = c("Country-fixed effects", "Cohort-fixed effects"))```. Don't forget to also reverse the standard errors if you are using robust standard errors.
* Save the output of the `stargazer()` function as a .txt file. This could be one possible way to do so: ```fileConn<-file("C:/your/file/path/filename.txt")
writeLines(latex_code_as_text, fileConn)  
close(fileConn)``` 
* If you want to reverse the columns of multiple stargazer regression tables at the same time, no problem, just make sure to save them all in the same directory.
* **Attention**: Also make sure that no other .txt files are in the same folder as this will throw an error when executing the code. Other filetypes such as .xlsx etc. should not be a problem. They will just be skipped.
* Download the reverse_stargazer folder and store it in a working directory of your choice.
* In the same working directory create a new python file in which you do the following  (explained in detail in example.py)
    ```
    import revregtable as rrt
    import os
    path = "example_txt_files"

    files = os.listdir(path)
    txt_files = (file for file in files if ".txt" in file)
    
    for file in txt_files:
        rt = rrt.read_reg_tbl_txt(f"{path}/{file}")
        #rt.show()
        rt.reverse()
        #rt.show()
        rt.save_to_txt(f"{path}/{file}")
    ```
* That's it. Enjoy your Regression Tables with reversed column order.

## Some comments
* If executing the python script throws you an `IndexError: list index out of range`: most probably because in the file path you have selected are .txt files other than the ones that contain Regression Tables
* I've tested the script for 
          * `lm` and `ivreg()` regression models
          * For omitting two or three fixed-effects variables from the Regression Tables as well as
          * For 4 to 8 columns in the regression tables
* If you would like to contribute on how to improve the code or make it more robust, feel free to drop a comment
