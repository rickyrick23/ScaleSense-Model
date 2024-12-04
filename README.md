Scale Sense - Health Tracking and Guidance App

Scale Sense is a health and wellness mobile app developed by my friend, designed to track and analyze users' body metrics, providing personalized health guidance, nutrition tips, and activity recommendations based on the data collected. It integrates seamlessly with Bluetooth-enabled weighing scales and provides insights into various health parameters such as BMI, body fat percentage, muscle mass, metabolic age, and more.

Table of Contents
- Project Overview
- Features
- Technology Stack
- Model Overview
- Installation
- Usage
- Future Enhancements

Project Overview

The Scale Sense app helps users track various body metrics like body impedance, BMI, weight, height, bone density, visceral fat index, and more. With a user-friendly interface and support for multiple languages, the app is designed to be accessible to families, fitness enthusiasts, and medical professionals alike.

The app uses an AI model to provide personalized nutrition guidance, suggest physical activities based on user health data, and send notifications to keep users motivated and informed.

Features

- Bluetooth Integration: Syncs with Bluetooth-enabled scales to collect health data.
- Health Metrics Tracking: Tracks metrics such as body impedance, BMI, muscle mass, fat percentage, water percentage, etc.
- AI-based Recommendations: Provides personalized nutrition guidance and suggests physical activities based on the user's health data.
- Multi-language Support: Available in 19 languages, including all Indian languages.
- Family Profile: Allows users to track health data for multiple family members.
- Progress Tracking: Visualizes health trends over time, including daily, weekly, and monthly data views.
- Notifications: Sends reminders and health tips to users.

Technology Stack

- Frontend: Flutter (or React Native)
- Backend: Firebase (for authentication and data storage)
- AI Model: Random Forest Classifier / Decision Tree (for health recommendations)
- Bluetooth Integration: BLE (Bluetooth Low Energy)
- Data Processing: Python (for model training and data preprocessing)
- Model Storage: Jupyter Notebook (.ipynb format for model training)

Model Overview

The AI model in Scale Sense is trained to analyze various health parameters (such as BMI, weight, body fat percentage, etc.) and predict personalized health guidance and activity recommendations. The model is built using scikit-learn and trained in a Jupyter Notebook.

Model Training Workflow:

1. Data Collection: Health data is collected from users (body impedance, BMI, etc.).
2. Data Preprocessing: Missing values are handled, and categorical data is encoded.
3. Model Selection: A machine learning algorithm (e.g., Random Forest Classifier) is trained on the data.
4. Evaluation: The model is evaluated based on accuracy and other metrics.
5. Model Deployment: The trained model is saved and used for real-time predictions in the app.

Installation

To run this project locally:

Prerequisites:
- Python 3.x
- Jupyter Notebook
- Libraries:
  - pandas
  - numpy
  - scikit-learn
  - joblib
  - matplotlib (optional for data visualization)

Steps to Install:

1. Clone this repository:
   git clone https://github.com/rickyrick23/scale-sense.git

2. Navigate into the project directory:
   cd scale-sense

3. Install the required libraries:
   pip install -r requirements.txt

4. Open the Jupyter Notebook for model training:
   jupyter notebook model_training.ipynb

5. In the notebook, follow the steps for loading the data, training the model, and saving the trained model.

Usage

1. Training the Model:
   The `synthetic_user_data.ipynb` notebook handles data preprocessing, model training, and evaluation. It outputs a trained model saved in .pkl format for later use in the app.

2. Making Predictions:
   After training the model, you can use the saved model to make predictions about a user’s health data. You can load the model using joblib and pass new data to predict health insights.

3. Running the App:
   The mobile app, built with Flutter or React Native, uses the trained model to provide health insights. The app communicates with a backend for storing data and receiving predictions.

Future Enhancements

- AI-based Health Recommendations: Implement AI to suggest more personalized diet plans and activities.
- Integration with Wearables: Extend the app to sync with other health tracking devices.
- Cloud Data Syncing: Allow users to sync their health data across devices.
- More Metrics: Add more body metrics to improve predictions (e.g., heart rate, step count).
!
