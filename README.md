# Car-Price-Predictor-Regression-Project



## Libraries Used :
* BeautifulSoup (Web Scraping)
* Pandas/Numpy  (Data analysis)
* Matplotlib/Seaborn (Data visualisation)
* Scikit-Learn libraries (Building Regression model and evaluating scores)
* Streamlit (Web App development)


## About Data:
* I gathered data through web scraping from a well-known American company's website that  sells used cars.
* It originally consisted of 6 columns and ~2800 Rows.


## Project Information:
* I divided the project into  six parts:


  
> First: Web Scraping


 * Where I web scraped the data using BeautifulSoup library on jupyter notebook.





> Second : Data Cleaning

* Using Pandas and numpy
  
*   droping duplicates,

 * Handling Outliers,
 
*  Feature engineering
     (created Brand column out of car 'name' column using string operations,
     removed characters and alphabets from numeric columns,
     created exterior and interior color columns out of 'color' column,
     created accidents and past_owners  columns out of 'condition' column).





> Third: Exploratory Data Analysis

* Using matplotlib & Seaborn

* Univariate analysis:
    
  Most common Car brands.
  
  Most common car interior & exterior colors.
  
  Distribution of cars by years/miles/price.
  
  Percentage of cars by accident & past_owners.
   
* Bivariate analysis:
    
  Top ten most and least expensive Car brands by average price.
  
  Trends of Price change over car model year & miles driven.
 
  Average price of cars by exterior & interior color.
 
  Average price of cars by No of accidents and past owners they've had.






> Fourth : ML Regression model building

* Data preprocessing using scikit-learns Simple-imputer, OneHotEncoder, Standard Scaler and spliting the Data using train_test_split (Taking Price as the Target Variable)
  
* Prediction Model Building using Scikit-learns models DecisionTreeRegressor,RandomForestRegressor,GradientBoostingRegressor, SVR 
and Also XGBoost.

* Used Pipeline to column Transform and predict the features.






> Fifth : Visualising Results


* Using R2_score and mean_absolute_error as metric score the scores were
      
  
  r2_score:
  
     SVR : 0.857
      
     Decision Tree : 0.59

     XGBoost : 0.849

     Random Forest : 0.77

     GradientBoost : 0.856


         
   Mean_absolute_error:

   SVR : 0.12

   Decision Tree : 0.21

  XGBoost : 0.129

   Random Forest : 0.15

   GradientBoost : 0.126





> Sixth: Model Web App develpment:

* Used pickle to dump and load dataframe and SVR model to a new IDE

* Used Streamlit Library To Create a Web App which takes the input from user and displays the predicted price for the given car specification













































