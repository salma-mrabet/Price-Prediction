
from flask import Flask, request, render_template
import pickle

#app = Flask(__name__) : Creates an instance of the Flask class. __name__ is a variable that represents the name of the application’s module (this helps Flask know where to look for resources like “templates” 
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))  # loading the model

# @app.route("/"): @ represents decorators (they modify the behavior of a function or class). 
# The route() decorator tells Flask what URL should trigger our function. 
# In our example, the homepage (/) should trigger the hello_world() function.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """Grabs the input values and uses them to make prediction"""
    rooms = int(request.form["rooms"])
    distance = int(request.form["distance"])
    prediction = model.predict([[rooms, distance]])  # this returns a list e.g. [127.20488798], so pick first element [0]
    output = round(prediction[0], 2) 

    return render_template('index.html', prediction_text=f'A house with {rooms} rooms and located {distance} meters from the city center has a value of ${output}')

if __name__ == "__main__":
    app.run()