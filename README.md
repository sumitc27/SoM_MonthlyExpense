# Monthly Expenses Predictor namely "KharchaKitna"
LINK for the Web App of this deployed ML Mode :- https://iiitdmj-student-monthly-expense-predictor-kharchakitna.streamlit.app/

## About the project
This is a ML Project named "KharchaKitna" which will predict the Monthlty Expense of a student (specially of our IIITDMJ Campus) The dataset 
for this model is intutively prepared by myself by taking expenses ideas for fellow batchmates.It consists of 200 data points. It takes account
of various factors(mention as columns of CSV File) like:-

MessTaken :- Opted for Mess or Not.(1 means opted ✅ / 0 means not opted ❌)                     

NOTE :- If you have opted for mess then your monthly mess amount will be not included with the MonthlyExpense, since it is already paid at the start of the Semester.

CanteenVisit :- No. of days you visit canteen/Hexa/Nescafe(all included) per week.

RelationshipStatus :- whether the student is single🗿 or mingle😁.(0 means single / 1 means mingle)

OnlineFood :- No. of times the student order food online from city.(per month)

CityVisit :- No. of times the student visit the city from campus.(per month)

MonthlyExpense which is our last column is out target column.

This will include :-                                             
->Recharge                             								
->Basic Needs(Groceries)					
->Outside Food (Hexa/Canteen/Nescafe)
->The used feature column and the other daily basis expenses.
_________________________________________________________________________________________________

## Algoritms Accuracy
I trained and tested the data with 2 Algorithms (Linear Regression & Random Forest)
Both gave good accuracy.
Accuracy for Linear Regression = 93.7 %
Accuracy for Random Forest = 98% 
_________________________________________________________________________________________________

## Algoritms Selection

While random forests often providing higher accuracy, I'm selecting a linear regression model, which can be justified by the following factor with their explaination.

1. Interpretability :-
Linear Regression: The coefficients in a linear regression model directly indicate the relationship between each feature and the target variable. This makes it easy to understand how each factor (like CanteenVisit, RelationshipStatus, etc.) impacts the monthly expenses.
Random Forest: While random forests can provide feature importance, they do not offer the same level of interpretability as linear regression.

2. Simplicity and Transparency :-
Linear Regression: Simple to implement and understand. It provides a clear mathematical relationship that is easy to explain to non-technical users.
Random Forest: More complex with multiple decision trees, making the model harder to understand and explain.

3. Data Size Considerations :-
Linear Regression: Performs well with smaller datasets. With only 200 students in your dataset, a simpler model like linear regression might generalize better.
Random Forest: Typically requires larger datasets to perform optimally and to avoid overfitting.

4. Prediction Consistency:-
Linear Regression: Provides consistent predictions. Small changes in the input data do not significantly alter the model.
Random Forest: Small changes in the data can result in different trees being built, potentially leading to varied predictions.

5. Ease of Maintenance:-
Linear Regression: Easier to maintain and update with new data. Changes to the model can be easily tracked and managed.
Random Forest: Requires more effort to update and maintain, especially if hyperparameter tuning or retraining is needed frequently.

6. Theoretical Alignment
Linear Regression: If you have domain knowledge suggesting a linear relationship between the features and the target, linear regression is theoretically appropriate.
Random Forest: While flexible and powerful, it may model non-linear relationships that do not exist, leading to overfitting.
__________________________________________________________________________________________________

## About Files in this Repository
1. KharchaKitna.ipynb :- It is the Python Notebook in which the model is being trained.
2. MonthlyExp.cpp :- The dataset is prepared by using the C++ Program File.
3. MonthlyExp1.0.csv :- This is the Dataset which is used for training/testing this model.
4. requirements.txt :- This is the txt file containing the name of necessary library to deploy this mode as a webpage using Streamlit.
5. trained_model.sav :- This is Trained model.
6. webapp.py :- Contains all the code for the web app to predict the Monthly Expenses.
__________________________________________________________________________________________________

## Explaination for Wrong Prediction
If you think that the model is giving wrong prediction of you monthly expense then these can be the following reason.
-> The dataset for training this model was small around 200 data point, its most likely that the model can make wrong prediction.
-> It can be the case that the data you have entered is a outliner.
I hope you are statisfied with my explaination.
I will try to work on improving this model with time.

Thank You for Reading the README 😁
Have a great day :)
