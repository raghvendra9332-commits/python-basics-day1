import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#Training data
hours = np.array([1,2,3,4,5]).reshape(-1,1)
marks = np.array([30,40,50,60,70])

#Create and train model
model = LinearRegression()
model.fit(hours,marks)

#Predictions for plotting regression line
predicted_marks = model.predict(hours)

#Plot original data
plt.scatter(hours, marks, color='blue',label='Actual Data')

#Plot regression line
plt.plot(hours, predicted_marks, color='red', label='Regression Line')

#Label and title
plt.title('Study Hours vs Marks')
plt.xlabel('Hours Studied')
plt.ylabel('Marks Obtained')
plt.legend()
plt.grid(True)

plt.show()