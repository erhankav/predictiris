"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask,request,jsonify
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.externals.joblib import dump
from sklearn.externals.joblib import load


app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
   

    return "Hello World!"

@app.route('/<a>,<b>,<c>,<d>', methods=['GET'])
def get_product(a,b,c,d):
    filename = 'finalized_model.pkl'
    loaded_model = load(filename)
    result = loaded_model.predict([[float(a),float(b),float(c),float(d)]])
   
    return jsonify({'prediction': list(result)})

    
#@app.route("/predict", methods=['GET'])
def predict():
    prediction = 0.5
    return jsonify({
        'prediction': prediction
    })

if __name__ == '__main__':

    app.run()





