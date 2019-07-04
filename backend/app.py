from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import json
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/internship"
mongo = PyMongo(app)
CORS(app)

@app.route("/")
def index():
        return "API ENDPOINT IS OPEN"

@app.route("/add",methods = ['POST'])
def add():
        name = request.form.get('name')
        rating = request.form.get('rating')
        res = mongo.db.movies.insert({"name": name,"rating": rating})
        return res

@app.route("/autocomplete",methods = ['POST'])
def autocomplete():
        name = json.loads(request.data)['prefix']
        limit = json.loads(request.data)['limit']
        offset = json.loads(request.data)['offset']
        db_response = mongo.db.movies.find(
                {"name":  { "$regex": f"^{name}", '$options' : 'i' }},
                {"_id":0}
                ).sort("rating").limit(limit).skip(offset)

        res = []
        for response in db_response:
                print(response)
                res.append(response)
        return jsonify(res)

@app.route("/movies/<movie_id>")
def movies(movie_id):
        db_response = mongo.db.movies.find(
                {"_id":  ObjectId(movie_id)},
                {"_id":0})
        
        res = []
        for response in db_response:
                print(response)
                res.append(response)
        return jsonify(res)

@app.errorhandler(404) 
def not_found(e):
        return "not found"

if __name__ == '__main__':
    app.run(debug=True)