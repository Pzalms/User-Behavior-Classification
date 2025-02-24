import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("random_forest_model.pkl")

st.title("User Behavior Classification App")
st.write("This application predicts user behavior class based on device usage patterns.")

# Information about the dataset and features
st.header("About This App")
st.write("""
This model is trained on a dataset that captures mobile device usage patterns. The selected features are key indicators of user behavior:

1. **Number of Apps Installed**: More apps typically indicate higher engagement.
2. **App Usage Time (min/day)**: Measures total time spent using applications daily.
3. **Screen On Time (hours/day)**: Higher screen-on time correlates with greater device interaction.
4. **Battery Drain (mAh/day)**: High battery consumption suggests frequent device usage.
5. **Data Usage (MB/day)**: More data consumption indicates higher app engagement.

The Random Forest model was chosen due to its robustness and high accuracy in classification tasks.
""")

# Input fields
num_apps = st.number_input("Number of Apps Installed", min_value=0, max_value=500, value=50)
app_usage = st.slider("App Usage Time (min/day)", min_value=0, max_value=1000, value=120)
screen_time = st.slider("Screen On Time (hours/day)", min_value=0, max_value=24, value=5)
battery_drain = st.slider("Battery Drain (mAh/day)", min_value=0, max_value=10000, value=2000)
data_usage = st.slider("Data Usage (MB/day)", min_value=0, max_value=5000, value=500)

# Prediction function
def predict_behavior():
    features = np.array([[num_apps, app_usage, screen_time, battery_drain, data_usage]])
    prediction = model.predict(features)[0]
    return prediction

# Predict button
if st.button("Predict User Behavior Class"):
    result = predict_behavior()
    st.success(f"Predicted User Behavior Class: {result}")