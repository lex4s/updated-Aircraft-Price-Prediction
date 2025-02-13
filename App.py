import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# تحميل النموذج والمحول مع معالجة اختلاف الإصدارات
try:
    model = joblib.load("airplane_price_model.pkl")
    scaler = joblib.load("scaler.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# عنوان التطبيق
st.title("Aircraft Price Prediction App")

# تحميل البيانات الأصلية لاستخراج القيم الفريدة للخيارات
try:
    df = pd.read_csv("dataset.csv")
except FileNotFoundError:
    st.error("Dataset file not found. Please upload the correct dataset.")
    st.stop()

numeric_features = df.select_dtypes(include=[np.number]).columns.tolist()
if "Price_USD" in numeric_features:
    numeric_features.remove("Price_USD")

# اختيار موديل الطائرة
st.sidebar.header("Select Aircraft Model")
unique_models = df["Model"].unique().tolist()
selected_aircraft_model = st.sidebar.selectbox("Aircraft Model", unique_models)

# إدخال بيانات المستخدم
st.sidebar.header("Enter Aircraft Details")
input_data = {"Model": selected_aircraft_model}
for feature in numeric_features:
    input_data[feature] = st.sidebar.number_input(feature, value=int(df[feature].mean()), step=1, format="%d")

# تحويل الإدخالات إلى DataFrame
input_df = pd.DataFrame([input_data])
input_df = input_df.drop(columns=["Model"], errors='ignore')  # إزالة العمود النصي قبل المعالجة

# التأكد من صحة البيانات قبل التنبؤ
try:
    input_scaled = scaler.transform(input_df)
except ValueError as e:
    st.error(f"Error in input data transformation: {e}")
    st.stop()

# زر التنبؤ
if st.sidebar.button("Predict Price"):
    try:
        prediction = model.predict(input_scaled)[0]
        st.write(f"### Predicted Price for {selected_aircraft_model}: ${prediction:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")