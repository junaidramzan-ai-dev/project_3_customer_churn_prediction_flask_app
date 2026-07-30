from flask import Blueprint
from flask import render_template
from flask import request

from services.prediction_service import PredictionService

prediction_bp = Blueprint(
    "prediction",
    __name__
)


@prediction_bp.route("/")
def home():

    return render_template("index.html")


@prediction_bp.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "GET":

        return render_template("predict.html")

    form_data = {

        "gender": request.form["gender"],

        "SeniorCitizen": int(request.form["SeniorCitizen"]),

        "Partner": request.form["Partner"],

        "Dependents": request.form["Dependents"],

        "tenure": int(request.form["tenure"]),

        "PhoneService": request.form["PhoneService"],

        "MultipleLines": request.form["MultipleLines"],

        "InternetService": request.form["InternetService"],

        "OnlineSecurity": request.form["OnlineSecurity"],

        "OnlineBackup": request.form["OnlineBackup"],

        "DeviceProtection": request.form["DeviceProtection"],

        "TechSupport": request.form["TechSupport"],

        "StreamingTV": request.form["StreamingTV"],

        "StreamingMovies": request.form["StreamingMovies"],

        "Contract": request.form["Contract"],

        "PaperlessBilling": request.form["PaperlessBilling"],

        "PaymentMethod": request.form["PaymentMethod"],

        "MonthlyCharges": float(request.form["MonthlyCharges"]),

        "TotalCharges": float(request.form["TotalCharges"])
    }

    prediction, stay_probability, churn_probability = PredictionService.predict(form_data)

    return render_template(
        "result.html",
        prediction=prediction,
        stay_probability=stay_probability,
        churn_probability=churn_probability,
        form_data=form_data
)
    