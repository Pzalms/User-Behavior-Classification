# User Behavior Classification App

## Overview
This is a **Streamlit web application** that predicts a user's behavior class based on mobile device usage patterns. The application leverages a **Random Forest Classifier**, trained on key features that influence user behavior.

## Features
- **User-friendly interface** for inputting device usage details.
- **Predicts user behavior class (1-5)** based on trained data.
- **Uses a Random Forest model** for high accuracy and performance.

## Dataset & Feature Selection
The model was trained on a dataset containing mobile usage data. The selected features are:

1. **Number of Apps Installed** - More apps typically indicate higher engagement.
2. **App Usage Time (min/day)** - Total daily time spent using applications.
3. **Screen On Time (hours/day)** - Measures device interaction time.
4. **Battery Drain (mAh/day)** - Higher battery consumption correlates with frequent usage.
5. **Data Usage (MB/day)** - Higher data consumption suggests higher engagement.

## Installation & Setup
1. Clone the repository or download the script.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run main.py
   ```

## Usage
- Open the app in your browser after running the command.
- Enter your device usage statistics.
- Click **"Predict User Behavior Class"** to see the predicted category.



