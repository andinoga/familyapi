import os
from flask import Flask, jsonify, request

app = Flask(__name__)

person2 = {}
obj = {}
obj['name'] = "John"
obj['lastname'] = "Doe"

person1 = {}
obj = {}
obj['name'] = "Mary"
obj['lastname'] = "Doe"

person3 = {}
obj = {}
obj['name'] = "Benjamin"
obj['lastname'] = "Doe"

family = {}


@app.route('/', methods=['GET'])
def hello():
    family = [
        {
         "id": '1',
         "name": "John",
         "last name": "Doe",
         "age": '54',
         "gender": "male",
         "lucky numbers": '2''10''19', 
        },
        {
         "id": '2',
         "name": "Mary",
         "last name": "Doe",
         "age": '52',
         "gender": "female",
         "lucky numbers": '15''22''23',  
        },
        {
         "id": '3',
         "name": "Benjamin",
         "last name": "Doe",
         "age": '23',
         "gender": "male",
         "lucky numbers": '7''20''30', 
        },
         ]
@app.route('/members/<int:id>')
def get_member(id):
  return 'member'
  

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))