from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('Model.pkl', 'rb'))
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def home():
    data_1 = int(request.form.get('Time'))
    data_2 = float(request.form.get('val1'))
    data_3 = float(request.form.get('val2'))
    data_4 = float(request.form.get('val3'))
    data_5 = float(request.form.get('val4'))
    data_6 = int(request.form.get('val5'))
    data_7 = int(request.form.get('val6'))
    data_8 = int(request.form.get('val7'))
    data_9 = int(request.form.get('val8'))
    data_10 = int(request.form.get('val9'))
    data_11 = int(request.form.get('val10'))
    

    arr = np.array([[data_1, data_2, data_3, data_4, data_5, data_6, data_7,data_8,data_9,data_10,data_11]])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)