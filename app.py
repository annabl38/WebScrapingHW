from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

app=Flask(__name__)

mongo=PyMongo(app,uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    mars_data=mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_data)

@app.route('/scrape')
def data():
    mars_info=scrape()
    
    mongo.db.collection.update({},mars_info,upsert=True)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)