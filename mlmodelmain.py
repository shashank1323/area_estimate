import pickle
from flask import Flask, render_template, request

esapp = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

# self hosted url i.e of local host/
@esapp.route('/')
def index():
    return render_template('index.html')

@esapp.route('/predict',methods=['GET', 'POST'])
def predict():
    try:
        prediction = model.predict([[request.form.get('price')]])
        output = round(prediction[0],2)
        return render_template('index.html', prediction_text=f'Total price estimated is Rs. {output}/-')
    except:
        return render_template('index.html', prediction_text=f'Invalid input ')
if __name__=='__main__':
    esapp.run(debug=True)
