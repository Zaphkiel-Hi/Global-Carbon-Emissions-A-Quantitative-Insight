import pandas as pd
from sklearn.model_selection import train_test_split

# Load the processed dataset
file_path = "Processed_Carbon_Emission.csv"
df = pd.read_csv(file_path)

# Select Features (X) and Target (y)
X = df.drop(columns=["CarbonEmission"])
y = df["CarbonEmission"]

# Split the dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display dataset shapes
print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# Save the training and testing datasets
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)
