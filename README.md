#Fleiss' Kappa - Statistic to measure inter rater agreement
##Python implementation of Fleiss' Kappa (Joseph L. Fleiss, Measuring Nominal Scale Agreement Among Many Raters, 1971.)

INPUT **rate** - ratings matrix containing number of ratings for each subject per category 
      [size - *N* X *k* where *N* = #subjects and *k* = #categories]
      **n** - number of raters   
      
OUTPUT **fleiss' kappa**
