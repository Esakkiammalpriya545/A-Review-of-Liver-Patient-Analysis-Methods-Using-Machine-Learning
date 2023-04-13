from flask import Flask, render_template, request
import keras 
from keras.models import load_model
import numpy as np


app = Flask(__name__)

model = load_model("liver.h5")

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/submit')
def submitform():
	return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predicted():
    
    x=[[int(x) for x in request.form.values()]]
    print(x)
    
    x = np.array(x)
    print(x.shape)
    
    print(x)
    pred = model.predict(x)
    print(pred)

    output=pred[0]
    if(output==1):
        return render_template('result.html',prediction_text="You have a liver disease problem.")
    else:
        return render_template('result.html',prediction_text="You don't have liver disease problem.")

if __name__ == '__main__':
	app.run(debug=True)