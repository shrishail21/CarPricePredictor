import numpy as np
import math
from flask import Flask, render_template, request
import pickle

app= Flask(__name__)
model = pickle.load(open('RandomForestReg.pkl', 'rb'))

@app.route("/")
def project():
    return  render_template("project.html")


@app.route("/projectform")
def projectform():
    return render_template('projectform.html')


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        company = request.form["brands"]
        owner = request.form["owners"]
        color = request.form["colors"]
        mileage = request.form["mileage"]
        kilometers_driven = request.form["Running"]
        year= request.form["Year"]
        fuel = request.form["fuel"]
    a= float(mileage)
    M=math.log(a)
    K=math.log(float(kilometers_driven))
    company_dict={'Audi':0, 'BMW':1, 'Bently':2, 'Chevrolet':3, 'Datsun':4, 'Ferrari':5, 'Fiat':6, 'Ford':7, 'Honda':9,  
                  'Hyundai':9, 'Isuzu':10, 'Jaguar':11, 'Jeep':12, 'Kia':13, 'Land Rover':14, 'Lexus':15, 'MG':16, 'Mini':17, 
                  'Mahindra':18, 'Mahindra-Renault':19, 'Maruti Suzuki':20, 'Maserati':21, 'Mercedes-Benz':22, 'Mitsubishi':23, 
                  'Nissan':24, 'Porsche':25, 'Renault':26, 'Skoda':27, 'Ssangyong':28, 'Tata':29, 'Toyota':30, 'Volkswagen':31,
                  'Volvo':32}
    Cn=company_dict.get(company)
    Y=int(year)
    Fuel_dict={'CNG':0, 'Diesel':1, 'Hybrid':2, 'LPG':3, 'Petrol':4}
    F=Fuel_dict.get(fuel)
    Color_dict={'Beige':0, 'Black':1, 'Blue':2, 'Bronze':3, 'Brown':4, 'Gold':5, 'Green':6, 'Grey':7, 'Maroon':8,  
                'Orange':9, 'Purple':10, 'Red':11, 'Silver':12, 'White':13, 'Yellow':14}
    C=Color_dict.get(color)
    owner_dict={'4 or More':0, 'First':1, 'Fourth':2, 'Second':3, 'Third':4, 'UnRegistered Car':5}
    O=owner_dict.get(owner)

    prediction =np.exp(model.predict([[M,Cn,Y,K,C,F,O]]))
    P=format(prediction[0],'.3f')
    
    return render_template("predict.html",M=mileage, Cn=company, Y=year, K=kilometers_driven, C=color, F=fuel, O=owner, P=P, m=M)


if __name__ == "__main__":
    app.run(debug=True) 