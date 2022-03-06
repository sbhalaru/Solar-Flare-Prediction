# Solar-Flare-Prediction README

**Version 1.1.0**

**Include a readme file that explains your file structure, how to run your code, and name all third-party modules you are using.**


## Solar Flare.ipynb

This notebook shows all the visualizations for our presentation and includes the machine learning models we use for the prediction of energy, duration, x_pos, and y_pos.


## Modules

#### preprocessing.py

-function parse_date(sdatex, stimex)

This is used to parse the strings from the date time data in the dataframe.
This allows us to create a more robust datetime format for its start, peak, and end.

-function preprocess(fname)

This allows us to read in the csv file containing the whole solar flare data that we need to use for the project.

1. We drop certain columns and values that are no use to our project goal and helps to save time when processing the dataframe.
2. We also make certain changes to the datetime formats given so that they become easier to handle in the machine learning section.
3. Along with the datetime, we changes values of the energy which is our main focus. Since they are in a range format, using machine learning makes it extremely complicated, therefore we converted them into numbers from 0 to 8 and will reconvert after the machine learning process
4. We also drop certain unwanted columns at the end and change the duration column to a logarithmic scale since it is slightly skewed.

#### ML_prediction.py

-function train_test_spilt(df)

Takes in a pandas DataFrame, splits it into train/test set and retunrs.

-function duration_prediction(cols = [])

Takes in the columns name using to predict the duration, returns the regressor, confidence score, and MSE.

-function energy_prediction(cols = [])

Takes in the columns name using to predict the energy_kev, returns the classifier and accuracy score.

-function x_y_pos_prediction(cols = [])

Takes in the columns name using to predict the x_pos and y_pos, returns the regressor, confidence score, and MSE.

#### Add your python files...

- function ...

## Third-party modules
numpy, pandas, matplotlib, seaborn, scikit-learn, scipy, datetime


## Authors
Group 5:
Haaris Rahman, Kevin Mills, Shaan Bhalaru, Yongxing Chen, Shusen Lin



