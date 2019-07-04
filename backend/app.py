from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import json

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
        name = json.loads(request.data)['name']
        db_response = mongo.db.movies.find(
                {"name":  { "$regex": f"^{name}", '$options' : 'i' }},
                {"_id":0}
                ).sort("rating").limit(5)

        res = []
        for response in db_response:
                print(response)
                res.append(response)
        return jsonify(res)

@app.route("/movies/<movie_id>")
def movies(movie_id):
        return render_template("index.html", online_users=online_users)

@app.errorhandler(404) 
def not_found(e):
        return "not found"

if __name__ == '__main__':
    app.run(debug=True)