# import necessary libraries
from models import create_house, create_rent
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import pandas, sqlite3, csv

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float

# flask setup
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Establish Connection
engine = create_engine("sqlite:///rent_house.sqlite")
conn = engine.connect()

house_df = pandas.read_csv("static/data/house_cleaned.csv")
house_df.to_sql("House", conn, if_exists='replace', index=False)

rent_df = pandas.read_csv("static/data/rent_cleaned.csv")
rent_df.to_sql("Rent", conn, if_exists='replace', index=False)

Rent = create_rent(db)
House = create_house(db)

from sqlalchemy.orm import Session
session = Session(bind=engine)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html", title="Rent & House Index Analysis", )
@app.route("/about")
def about():
    # Return template and data
    return render_template("about.html", title="About")

# Route that will trigger the scrape function
@app.route("/models")
def models():

    rent_list = session.query(Rent)
    # Redirect back to home page
    return render_template("models.html", title="Models", rent=rent_list)

@app.route("/maps")
def maps():

    # Redirect back to home page
    return render_template("maps.html", title="Maps")

@app.route("/api/rent_data")
def rent_data():

    results = session.query(Rent.RegionId, Rent.SizeRank, Rent.State, Rent.City, Rent.Year, Rent.Month, Rent.Price).all()

    RegionId = [result[0] for result in results]
    SizeRank = [result[1] for result in results]
    State = [result[2] for result in results]
    City = [result[3] for result in results]
    Month = [result[4] for result in results]
    Year = [result[5] for result in results]
    Price = [result[6] for result in results]

    rent_data = [{
        "RegionId": RegionId,
        "SizeRank": SizeRank,
        "State": State,
        "City": City,
        "Year": Month,
        "Month": Year,
        "Price": Price
    }]

    return jsonify(rent_data)

@app.route("/api/house_data")
def house_data():

    results = session.query(House.RegionId, House.SizeRank, House.State, House.City, House.Year, House.Month, House.Price).all()

    RegionId = [result[0] for result in results]
    SizeRank = [result[1] for result in results]
    State = [result[2] for result in results]
    City = [result[3] for result in results]
    Month = [result[4] for result in results]
    Year = [result[5] for result in results]
    Price = [result[6] for result in results]

    rent_data = [{
        "RegionId": RegionId,
        "SizeRank": SizeRank,
        "State": State,
        "City": City,
        "Year": Month,
        "Month": Year,
        "Price": Price
    }]

    return jsonify(rent_data)


@app.route("/api/heatmap_data")
def heatmap_data():

    

    # results = session.query(House.RegionId, House.SizeRank, House.State, House.City, House.Year, House.Month, House.Price).all()

    # RegionId = [result[0] for result in results]
    # SizeRank = [result[1] for result in results]
    # State = [result[2] for result in results]
    # City = [result[3] for result in results]
    # Month = [result[4] for result in results]
    # Year = [result[5] for result in results]
    # Price = [result[6] for result in results]

    # rent_data = [{
    #     "RegionId": RegionId,
    #     "SizeRank": SizeRank,
    #     "State": State,
    #     "City": City,
    #     "Year": Month,
    #     "Month": Year,
    #     "Price": Price
    # }]

    return jsonify(heatmap_data)

if __name__ == "__main__":
    app.run(debug=True)



