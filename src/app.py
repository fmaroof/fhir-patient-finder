import requests
import os
from flask import Flask, request, render_template
from dotenv import load_dotenv


app = Flask(__name__)

FHIR_SERVER_BASE_URL="http://pwebmedcit.services.brown.edu:8081/fhir"

load_dotenv()

username = os.getenv("FHIR_USERNAME")
password = os.getenv("FHIR_PASSWORD")

def request_medications(patient_id, credentials):

    url = f"{FHIR_SERVER_BASE_URL}/MedicationRequest?patient={patient_id}"
    
    req = requests.get(url, auth = credentials)
    
    medications = req.json().get("entry",[])
    return medications

@app.route('/', methods=['GET', 'POST'])
def index():
    
    result = None
    credentials = (username, password)

    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            result = request_medications(number, credentials=credentials)
        except ValueError:
            result = 'Invalid input. Please enter a number.'

    return render_template('index.html', medications=result)

if __name__ == '__main__':
    app.run(debug=True)

