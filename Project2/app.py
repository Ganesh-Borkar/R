from flask import Flask,request,render_template
import joblib

model = joblib.load("../../ResoluteAI/Project2/Models/GNBFix.pkl")

app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():

    return "<h1>Welcome !!!</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h1>Welcome to the Index page<h1>"


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="GET":

        return render_template("predict.html")
    
    else:
        
        T1=float(request.form["T1"])
        T2=float(request.form["T2"])
        T3=float(request.form["T3"])
        T4=float(request.form["T4"])
        T5=float(request.form["T5"])
        T6=float(request.form["T6"])
        T7=float(request.form["T7"])
        T8=float(request.form["T8"])
        T9=float(request.form["T9"])
        T10 = float(request.form["T10"])
        T11 = float(request.form["T11"])
        T12 = float(request.form["T12"])
        T13 = float(request.form["T13"])
        T14 = float(request.form["T14"])
        T15 = float(request.form["T15"])
        T16 = float(request.form["T16"])
        T17 = float(request.form["T17"])
        T18 = float(request.form["T18"])

        Prediction = model.predict([[T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,T18]])

        return render_template("predict.html",Target=Prediction)

        
    


if __name__=='__main__':
    app.run(debug=True)