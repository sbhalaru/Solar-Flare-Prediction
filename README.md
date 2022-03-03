# Solar-Flare-Prediction README
**Version 1.0.0**

preprocessing.py

This file contains the follwing 2 functions:

parse_date(sdatex, stimex):
This is used to parse the strings from the date time data in the dataframe.
This allows us to create a more robust datetime format for its start, peak, and end.

preprocess(fname):
This allows us to read in the csv file containing the whole solar flare data that we need to use for the project.
We drop certain columns and values that are no use to our project goal and helps to save time when processing the dataframe.
We also make certain changes to the datetime formats given so that they become easier to handle in the machine learning section.
Along with the datetime, we changes values of the energy which is our main focus. Since they are in a range format,
using machine learning makes it extremely complicated, therefore we converted them into numbers from 0 to 8 and will reconvert after the machine learning process
We also drop certain unwanted columns at the end and change the duration column to a logarithmic scale since it is slightly skewed.



---
## Authors
Group 5:
Haaris Rahman, Kevin Mills, Shaan Bhalaru, Yongxing Chen, Shusen Lin



