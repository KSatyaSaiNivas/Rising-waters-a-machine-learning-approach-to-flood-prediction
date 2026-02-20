
from flask import Flask, render_template, request
from joblib import load

# Create Flask app
app = Flask(__name__)

# Load saved model and scaler
model = load('floods.save')
sc = load('transform.save')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    return render_template('index.html')

@app.route('/data_predict', methods=['POST'])
def predict():
    temp = request.form['temp']
    Hum = request.form['Hum']
    db = request.form['db']
    ap = request.form['ap']
    aa1 = request.form['aa1']

    data = [[float(temp), float(Hum), float(db), float(ap), float(aa1)]]

    prediction = model.predict(sc.transform(data))
    output = prediction[0]

    if output == 1:
        result = "Possibility of Severe Flood"
    else:
        result = "No Possibility of Severe Flood"



    return render_template("chance.html", prediction=result)


# Run app
if __name__ == '__main__':
    app.run(debug=True)
