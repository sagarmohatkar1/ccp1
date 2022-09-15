from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open("ccp.pkl", "rb"))
columns_list = pickle.load(open("columns_list.obj", "rb"))

app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    
    Geography = request.form["Geography"]
    if Geography =='Maharashtra':
        Geography=0
    elif Geography =='Gujrat':
        Geography=1
    elif Geography =='Kerla':
        Geography=2
    Gender = request.form["Gender"]
    if Gender =='Female':
        Gender=1
    elif Gender =='Male':
        Gender=0
    Age = request.form["Age"]
    Tenure = request.form["Tenure"]
    CreditScore =request.form["CreditScore"]
    Balance = request.form["Balance"]
    NumOfProducts = request.form["NumOfProducts"]
    HasCrCard = request.form["HasCrCard"]
    IsActiveMember = request.form["IsActiveMember"]
    EstimatedSalary = request.form["EstimatedSalary"]
    noofComplaints = request.form["noofComplaints"]
    
    data= (Geography,Gender,Age,Tenure,CreditScore,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,noofComplaints)

    array = np.array(data)

    array = array.reshape(1, -1)
    
    prediction = model.predict(array)
    return render_template('after.html', data=prediction ,d1=int(CreditScore) ,d2=int(noofComplaints))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)   

# @app.route('/predict1')
# def predict1():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     c = int(request.args.get('c'))
#     d = int(request.args.get('d'))

#     arr = np.array([[a, b, c, d]])
#     pred = model.predict(arr)
#     return render_template('after.html', data=pred)
    
