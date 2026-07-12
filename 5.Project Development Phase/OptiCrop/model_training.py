import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

def train_model():
    print("Loading dataset...")
    try:
        df = pd.read_csv('Crop_recommendation.csv')
    except FileNotFoundError:
        print("Error: Crop_recommendation.csv not found. Please place the dataset in the root folder or run generate_mock_data.py.")
        return

    print("Dataset shape:", df.shape)
    print("Checking for null values:")
    print(df.isnull().sum())

    # Preprocessing (Handle outliers - Log transformation on Potassium as requested)
    print("Applying log transformation on 'K' (Potassium)...")
    df['K'] = np.log1p(df['K'])

    # Features and Target
    X = df.drop('label', axis=1)
    y = df['label']

    # Splitting data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaling features (important for Logistic Regression and K-Means)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Epic 4: Model Building - K-Means Clustering (For Pattern Analysis)
    print("Applying K-Means Clustering...")
    kmeans = KMeans(n_clusters=4, random_state=42)
    kmeans.fit(X_train_scaled)
    print("K-Means clustering completed.")

    # Epic 4: Model Building - Logistic Regression
    print("Training Logistic Regression Model...")
    log_reg = LogisticRegression(max_iter=1000, random_state=42)
    log_reg.fit(X_train_scaled, y_train)

    # Evaluation
    y_pred = log_reg.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    print(f"Logistic Regression Accuracy: {acc * 100:.2f}%")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # Saving the model and scaler
    with open('model.pkl', 'wb') as f:
        pickle.dump(log_reg, f)
    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print("Model saved as model.pkl and Scaler saved as scaler.pkl")

if __name__ == "__main__":
    train_model()
