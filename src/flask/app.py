from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    ''' home page of app '''
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        model = pickle.load(open('ca337-nb1000-model.pkl', 'rb'))
        features = pickle.load(open('ca337-nb1000-features.pkl', 'rb'))

        review = request.form['review']
        prediction = model.predict(features.transform([review]))[0]

        return render_template('predict.html', result={'text': review, 'prediction': prediction})

    return render_template('predict.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
