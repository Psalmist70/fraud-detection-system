FRAUD DETECTION SYSTEM

OVERVIEW

This project implements a Credit Card Fraud Detection System using machine learning and a cloud-hosted API. Users can input transaction details (amount, time, transaction type) to check whether a transaction is fraudulent or legitimate.

Features Implemented

⇒ Machine Learning Models

Ensemble model combining Random Forest and XGBoost for best performance.

Models trained on the Credit Card dataset with SMOTE for class imbalance.

Numerical features (Amount and Time) are scaled before prediction.

⇒ Backend API

Built with Flask.

Endpoint: /predict-custom accepts JSON input (amount, time) and returns:

prediction (Fraud / Legitimate)

probability (risk score)

Hosted on Render, fully live and accessible via public URL.

⇒ Frontend GUI

Developed using Tkinter.

Allows user input for transaction amount, time, and type.

Sends requests to the deployed API and displays results.

⇒ Data Handling

PCA features V1–V28 are handled internally; users do not need to see or input them.

Only amount and time are required on the GUI for prediction.

Preloaded dataset used only internally for mapping inputs to model features

⇒ Deployment

Code is hosted on GitHub.

API uses Dockerized environment to ensure dependencies are consistent.

Joblib format used for storing the trained model.

⇒ How to Use

Open the Tkinter GUI.

Input transaction amount and time (select a time slot like morning/afternoon/evening).

Click Submit.

View the prediction (Fraud or Legitimate) and risk score.

⇒ Technologies Used

Python 3.12

Flask

Tkinter

Pandas, NumPy

scikit-learn

joblib

Render (Cloud deployment)

NOTES
All API interactions are via JSON.
The client never sees internal PCA features (V1–V28).
The system is ready for testing with realistic transaction inputs
