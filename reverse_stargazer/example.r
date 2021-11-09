library(stargazer)

set.seed(42)
x <- rnorm(100, mean = 100, sd = 5)
e <- rnorm(100, mean = 0, sd = 10)
y <- x*1.5+e
countries <- sample(c("CAN", "GRC", "PRT", "THA", "NZL"), size=100, replace=T)
birth_cohorts <- sample(c("1980", "1990", "2000", "2010"), size=100, replace=T)

model1 <- lm(y ~ x)
sum1 <- summary(model1)
sum1
model2 <- lm(y ~ x + countries - 1)
sum2 <- summary(model2)
sum2
model3 <- lm(y ~ x + birth_cohorts - 1)
sum3 <- summary(model3)
sum3
model4 <- lm(y ~ x + countries + birth_cohorts - 1)
sum4 <- summary(model4)
sum4

txt <- stargazer(model4, model3, model2, model1,
          type = "latex",
          omit = c("countries", "birth_cohorts"),
          omit.labels = c("Country-fixed effects", "Cohort-fixed effects"),
          omit.yes.no = c("Yes", "No"))

#set here the working directory to the path of where you have the reverse_stargazer package lying
setwd("C:/~/~/~/reverse_stargazer")
fileConn<-file("example_txt_files/example.txt") #enter here the path where your example_txt_files lie
writeLines(txt, fileConn)
close(fileConn)

