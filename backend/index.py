import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
model = load_model("my_model.keras")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    address = request.json['address']
    name = request.json['name']
    type = request.json['type']
    bedrooms = request.json['bedrooms']
    bathrooms = request.json['bathrooms']
    size = request.json['size']
    age = request.json['age']
    tenure = request.json['tenure']
    units = request.json['units']
    district = request.json['district']
    amenities = request.json['amenities']

    model(address,name,type)

if __name__ == "__main__":
    app.run(debug=True)