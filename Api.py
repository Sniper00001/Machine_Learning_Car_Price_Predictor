from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)


model = joblib.load('car_price_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json

        carName = input_data.get('carName', None)
        company = input_data.get('company', None)
        year = input_data.get('year', None)
        fuel_type = input_data.get('fuel_type', None)

     
        if not carName or not company or not year or not fuel_type:
            return jsonify({'error': 'Missing required information'}), 400

       
        model_input = [[carName, company, int(year), fuel_type]] 
       
        predictions = model.predict(model_input)

        return jsonify({'predictions': predictions.tolist()})

    except Exception as e:

        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

