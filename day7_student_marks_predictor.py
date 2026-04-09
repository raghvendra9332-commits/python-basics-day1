import numpy as np
from sklearn.linear_model import LinearRegression

print("=== Student Marks Predictor ===")

# Training data (Hours studied vs Marks obtained)
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([30, 40, 50, 60, 70])

# Create and train the model
model = LinearRegression()
model.fit(hours, marks)

# Display learned model parameters
print("\nModel Trained Successfully!")
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Take user input
study_hours = float(input("\nEnter the number of hours studied: "))

# Predict marks
predicted_marks = model.predict([[study_hours]])

print(f"Predicted Marks for {study_hours} hours of study: {predicted_marks[0]:.2f}")