from flask import Flask, request, render_template
import pickle


model=pickle.load(open("linreg.pkl","rb"))
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/Next')
def predict():
    return render_template('output.html')

@app.route('/y_predict', methods=['POST'])
def prediction():
    
    Temperature=request.form["Temperature"]
    Humidity=request.form["Humidity"]
    Light=request.form["Light"]
    CO2=request.form["CO2"]
    HumidityRatio=request.form["HumidityRatio"]
    
    p=[[float(Temperature),float(Humidity),float(Light),float(CO2),float(HumidityRatio)]]
    prediction=model.predict(p)
    
    if (prediction == 0):
        text= "It's not Occupied"
    else:
        text="It's Occupied"
    return render_template("output.html",prediction_test=text)    
    
    
if __name__=='__main__':
    app.run(debug=True)

