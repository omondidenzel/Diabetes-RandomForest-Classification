from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Create your views here.
def index(request):
    num_preg = float(request.GET["num_preg"])
    glucose_conc = float(request.GET["glucose_conc"])
    diastolic_bp = float(request.GET["diastolic_bp"])
    thickness = float(request.GET["thickness"])
    insulin = float(request.GET["insulin"])
    bmi = float(request.GET["bmi"])
    diab_pred = float(request.GET["diab_pred"])
    age = float(request.GET["age"])
    skin = float(request.GET["skin"])

    usingJoblib = joblib.load("diabetes_rf_model")
    result = usingJoblib.predict([[num_preg, glucose_conc, diastolic_bp, thickness, insulin, bmi, diab_pred, age, skin]])
    return render(request, "index.html", {result: "output"})