Decision Tree Regression on Traffic Delay Data

This project demonstrates how to build and evaluate a Decision Tree Regression model using Python and Scikit-Learn.  
The goal is to predict the average delay (in minutes) caused by various traffic and environmental factors.

What This Project Does
- Reads and processes traffic delay data from a CSV file.
- Converts categorical data (like weather and signal timing) into numeric form using get_dummies().
- Splits data into training and testing sets.
- Trains a Decision Tree Regression model.
- Evaluates model performance using:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
- Visualizes:
  - The Decision Tree structure
  - Actual vs Predicted Delay comparison chart

Libraries Used
- pandas  
- numpy  
- scikit-learn  
- matplotlib  

Results
- R² Score: Around 0.97 (indicating high model accuracy)
- Low Mean Absolute Error and Mean Squared Error values show excellent performance.


Output

A Decision Tree visualization showing the model’s decision rules.

A bar and scatter chart comparing actual vs predicted delay values.
