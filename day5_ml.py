from sklearn.linear_model import LinearRegression
import numpy as np
# Data (hours studied vs marks)
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([30, 40, 50, 60, 70])

# Create model
model = LinearRegression()

# Train model
model.fit(hours, marks)

# Predict
new_hours = np.array([[6]])
predicted_marks = model.predict(new_hours)

print("Predicted marks for 6 hours study:", predicted_marks[0])