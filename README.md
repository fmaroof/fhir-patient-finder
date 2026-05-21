# fhir-patient-finder

> **Note:** This README applies to the `develop-fhir-app-wintehr` branch, which is configured to run against a local WintEHR (ExCITE platform) installation.

This is a proof-of-concept FHIR web application written in Python and using Flask as the backend.

## 1. Dependencies
This app depends on Python 3 and a few Python packages outlined in the `requirements.txt` file.

## 2. Prerequisites: Starting WintEHR

This app connects to a local WintEHR (ExCITE platform) FHIR server running at `http://localhost:8888/fhir`. Before starting the app, make sure WintEHR is running.

From your WintEHR directory, run:

```
docker compose up -d
```

WintEHR should then be available at `http://localhost:3000` and the FHIR server at `http://localhost:8888/fhir`.

## 3. Running the App

We begin by creating a Python virtual environment using the `venv` module. This is done by running the command below from the "root" of this repo.

```
python3 -m venv venv                 # create a virtual environment called venv

source venv/bin/activate             # activate our virtual environment

pip3 install -r requirements.txt     # install all our dependencies into the virtual environment
```

After the above steps, we should be able to launch our app using the following command.

```
python3 src/app.py
```

This will start the app on port 5001. You can open your preferred browser and see the app running on `http://localhost:5001`


