import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import matplotlib.pyplot as pyplot

data = pandas.read_csv('traffic delay data.csv')
print(data)

data = pandas.get_dummies(data, columns=['Weather', 'Signal_Timing'], drop_first=True)

x = data[['Traffic_Volume', 'Accidents', 'Average_Speed', 'Weather_Rainy', 'Signal_Timing_Normal', 'Signal_Timing_Short']]
y = data['Average_Delay']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)
model = DecisionTreeRegressor(random_state=10)
model.fit(x_train,y_train)
predicted_y = model.predict(x_test)

print("R2 score",r2_score(y_test,predicted_y))
print("Mean Absolute Error:", mean_absolute_error(y_test, predicted_y))
print("Mean Squared Error:", mean_squared_error(y_test, predicted_y))

from sklearn import tree

pyplot.figure(figsize=(18,12))
tree.plot_tree(model,filled=True,feature_names = x.columns, fontsize=8)
pyplot.show()

pyplot.scatter(range(len(y_test)),y_test, color='blue', label = "Actual Data")
pyplot.bar(range(len(predicted_y)),predicted_y, color='red', label = "Predicted Data")
pyplot.xlabel("Actual Delay")
pyplot.ylabel("Predicted Delay")
pyplot.title("Decision Tree Regression: Actual vs Predicted")
pyplot.legend()
pyplot.show()