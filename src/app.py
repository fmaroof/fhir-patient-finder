import requests
import os
from flask import Flask, request, render_template
from dotenv import load_dotenv


app = Flask(__name__)

# FHIR_SERVER_BASE_URL="http://pwebmedcit.services.brown.edu:8081/fhir"
FHIR_SERVER_BASE_URL="http://localhost:8888/fhir"

load_dotenv()

username = os.getenv("FHIR_USERNAME")
password = os.getenv("FHIR_PASSWORD")


def request_patient(patient_id, credentials):

    req = requests.get(
        FHIR_SERVER_BASE_URL + "/Patient/" + str(patient_id), auth=credentials
    )

    print(f"Requests status: {req.status_code}")

    response = req.json()
    print(response.keys())

    return response


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    credentials = (username, password)

    if request.method == "POST":
        try:
            patient_id = request.form["number"].strip()
            result = request_patient(patient_id, credentials=credentials)
    
        except ValueError:
            result = "Invalid input. Please enter a number."

    return render_template("index.html", result=result)


# def request_medications(code_id, credentials):

#     #url = f"{FHIR_SERVER_BASE_URL}/MedicationRequest?patient={patient_id}"
#     url = f"{FHIR_SERVER_BASE_URL}/MedicationRequest?_has:Observation:code={code_id}"
#     req = requests.get(url, auth = credentials)

#     medications = req.json().get("entry",[])
#     return medications

# @app.route('/', methods=['GET', 'POST'])
# def index():

#     result = None
#     credentials = (username, password)

#     if request.method == 'POST':
#         try:
#             number = int(request.form['number'])
#             result = request_medications(number, credentials=credentials)
#         except ValueError:
#             result = 'Invalid input. Please enter a SNOMED code.'

#     return render_template('index.html', medications=result)

if __name__ == '__main__':
    port = int(os.environ.get("FHIR_PORT", 5001))
    app.run(debug=True, port=port)
