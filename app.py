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

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Establish Connection
engine = create_engine(
'sqlite:///rent_house.sqlite',
connect_args={'check_same_thread': False}
)

conn = engine.connect()

house_df = pandas.read_csv("static/data/house_filtered.csv")
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
    return render_template("models.html", title="Models", rent=rent_list, choices=choices)

@app.route("/marymodels")
def marymodels():

    results = session.query(Rent.City, Rent.Year, Rent.Month).all()

    cities_no_copy = [result[0] for result in results if result[2] == 1 if result[1] == 2020]

    # Redirect back to home page
    return render_template("marymodels.html", title="Mary Models", cities=cities_no_copy)

@app.route("/housemap")
def housemap():

    # Redirect back to home page
    return render_template("housemap.html", title="House Index Density Map")

@app.route("/rentmap")
def rentmap():

    # Redirect back to home page
    return render_template("rentmap.html", title="Rent Index Density Map")

@app.route("/api/rent_data")
def rent_data():

    results = session.query(Rent.RegionId, Rent.State, Rent.City, Rent.Lat, Rent.Lng, Rent.Year, Rent.Month, Rent.Price).all()

    RegionId = [result[0] for result in results]
    State = [result[1] for result in results]
    City = [result[2] for result in results]
    Lat = [result[3] for result in results]
    Lng = [result[4] for result in results]
    Year = [result[5] for result in results]
    Month = [result[6] for result in results]
    Price = [result[7] for result in results]

    rent_data = [{
        "RegionId": RegionId,
        "State": State,
        "City": City,
        "Lat": Lat,
        "Lng": Lng,
        "Year": Year,
        "Month": Month,
        "Price": Price
    }]

    return jsonify(rent_data)

@app.route("/api/house_data")
def house_data():

    results = session.query(House.RegionId, House.State, House.City, House.Lat, House.Lng, House.Year, House.Month, House.Price).all()

    RegionId = [result[0] for result in results]
    State = [result[1] for result in results]
    City = [result[2] for result in results]
    Lat = [result[3] for result in results]
    Lng = [result[4] for result in results]
    Year = [result[5] for result in results]
    Month = [result[6] for result in results]
    Price = [result[7] for result in results]

    house_data = [{
        "RegionId": RegionId,
        "State": State,
        "City": City,
        "Lat": Lat,
        "Lng": Lng,
        "Year": Year,
        "Month": Month,
        "Price": Price
    }]

    return jsonify(house_data)

@app.route("/api/house_data/1/2020/")
def jan_twentytwenty_data():

    results = session.query(House.RegionId, House.State, House.City, House.Lat, House.Lng, House.Year, House.Month, House.Price).all()

    RegionId = [result[0] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 309433]
    State = [result[1] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 309433]
    City = [result[2] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 309433]
    Lat = [result[3] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 309433]
    Lng = [result[4] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 309433]
    Year = [result[5] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 309433]
    Month = [result[6] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 309433]
    Price = [result[7] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 309433]

    heatmap_data = [{
        "RegionId": RegionId,
        "State": State,
        "City": City,
        "Lat": Lat,
        "Lng": Lng,
        "Year": Year,
        "Month": Month,
        "Price": Price
    }]

    return jsonify(heatmap_data)

@app.route("/api/rent_data/1/2020/")
def jan_twentytwenty_rent_data():

    results = session.query(Rent.RegionId, Rent.State, Rent.City, Rent.Lat, Rent.Lng, Rent.Year, Rent.Month, Rent.Price).all()

    RegionId = [result[0] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 1691]
    State = [result[1] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 1691]
    City = [result[2] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 1691]
    Lat = [result[3] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 1691]
    Lng = [result[4] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 1691]
    Year = [result[5] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 1691]
    Month = [result[6] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 1691]
    Price = [result[7] for result in results if result[6] == 1 if result[5] == 2020 if result[7] >= 1691]

    heatmap_data = [{
        "RegionId": RegionId,
        "State": State,
        "City": City,
        "Lat": Lat,
        "Lng": Lng,
        "Year": Year,
        "Month": Month,
        "Price": Price
    }]

    return jsonify(heatmap_data)

@app.route("/api/1/rent_data")
def rent_jan_data():

    results = session.query(Rent.RegionId, Rent.State, Rent.City, Rent.Lat, Rent.Lng, Rent.Year, Rent.Month, Rent.Price).all()

    RegionId = [result[0] for result in results if result[6] == 1]
    State = [result[1] for result in results if result[6] == 1]
    City = [result[2] for result in results if result[6] == 1]
    Lat = [result[3] for result in results if result[6] == 1]
    Lng = [result[4] for result in results if result[6] == 1]
    Year = [result[5] for result in results if result[6] == 1]
    Month = [result[6] for result in results if result[6] == 1]
    Price = [result[7] for result in results if result[6] == 1]

    rent_data = [{
        "RegionId": RegionId,
        "State": State,
        "City": City,
        "Lat": Lat,
        "Lng": Lng,
        "Year": Year,
        "Month": Month,
        "Price": Price
    }]

    return jsonify(rent_data)

if __name__ == "__main__":
    app.run()



