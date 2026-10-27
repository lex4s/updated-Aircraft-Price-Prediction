# ✈ Aircraft Price Prediction

## 📌 Project Overview
This project is a **machine learning application** designed to predict the price of aircraft based on key features such as production year, range, fuel consumption, capacity, and maintenance costs. The model is trained using a **Random Forest Regressor** and is deployed with a **Streamlit web app**.
 
## 🚀 Features
- **Data Analysis & Visualization**: Explore aircraft data with detailed insights.
- **Machine Learning Model**: Predicts aircraft prices using trained `RandomForestRegressor`.
- **Streamlit Web App**: User-friendly interface for making predictions.
- **Scalable & Reproducible**: Includes all dependencies via `requirements.txt`.

## 📂 Project Structure
```
📁 Aircraft-Price-Prediction
│── workspace.ipynb        # Jupyter Notebook for model training & analysis
│── App.py                # Streamlit app for price prediction
│── dataset.csv           # Aircraft dataset
│── airplane_price_model.pkl  # Trained ML model
│── scaler.pkl            # StandardScaler for preprocessing
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```

## 🛠 Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/lex4s/updated-Aircraft-Price-Prediction.git
cd updated-Aircraft-Price-Prediction
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run Jupyter Notebook (For Model Training & Analysis)
```sh
jupyter notebook notebook.ipynb
```

### 4️⃣ Run the Streamlit App
```sh
streamlit run App.py
```

## 📊 Model & Data Insights
The dataset contains various aircraft models with detailed specifications. The Jupyter Notebook (`notebook.ipynb`) provides:
- Exploratory Data Analysis (EDA)
- Feature correlation heatmaps
- Model training & evaluation metrics (MAE, RMSE, R² Score)
- Predictions vs Actual visualization

## 🎯 Usage
1. Select an aircraft model in the Streamlit app.
2. Enter specifications (e.g., production year, fuel consumption, capacity).
3. Click "Predict Price" to get the estimated aircraft price.

## 🏗 Future Improvements
- Add more aircraft types & historical price data.
- Implement additional ML models for comparison.
- Enhance UI with better visualization tools.

## 👨‍💻 Author
Developed by **Amr Ashraf**

## 📜 License
This project is open-source under the **MIT License**.

