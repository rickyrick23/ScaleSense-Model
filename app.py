from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model (use the path where you saved the model.pkl)
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the API endpoint to predict daily calorie target and give recommendations
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the POST request
        user_data = request.get_json()

        # Convert user data to a DataFrame
        user_df = pd.DataFrame([user_data])

        # Preprocess user data if needed (e.g., scaling or encoding)

        # Make predictions using the trained model
        prediction = model.predict(user_df)

        # Generate exercise and food recommendations (can be customized)
        exercise_recommendation = "30 minutes cardio"
        food_suggestions = "Turkey breast, avocado, brown rice"

        # Return the response as JSON
        return jsonify({
            'Daily Calorie Target': prediction[0],
            'Exercise Recommendation': exercise_recommendation,
            'Food Suggestions': food_suggestions
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
