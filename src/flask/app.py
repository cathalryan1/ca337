from flask import Flask
from flask import render_template
import pickle

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    ''' home page of app '''
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
 model = pickle.load(open('ca337-nb1000-model.pkl','rb'))
 features = pickle.load(open('ca337-nb1000-features.pkl','rb')
 review = request.form(['review'])
 prediction = model.predict(features.transform([review]))[0]
 return render_template('predict.html',result={'text':review,'prediction':prediction})
