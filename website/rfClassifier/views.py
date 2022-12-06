from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    num_preg = float(request.GET["num_preg1"])
    glucose_conc = float(request.GET["glucose_conc1"])
    diastolic_bp = float(request.GET["diastolic_bp1"])
    thickness = float(request.GET["thickness1"])
    insulin = float(request.GET["insulin1"])
    bmi = float(request.GET["bmi1"])
    diab_pred = float(request.GET["diab_pred1"])
    age = float(request.GET["age1"])
    skin = float(request.GET["skin1"])

    with open("/Users/omondidenzel/Desktop/DIABETES-ROJECT/website/rfClassifier/diabetes_rf_model.pkl", "rb") as f:
        usingJoblib = joblib.load(f)
        result = usingJoblib.predict([[num_preg, glucose_conc, diastolic_bp, thickness, insulin, bmi, diab_pred, age, skin]])
    #Testing purpose
    #result =10000
    return render(request, "result.html", {"result": result})