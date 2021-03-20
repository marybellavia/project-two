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
house_df.to_sql("House", conn, if_exists='append', index=False)

rent_df = pandas.read_csv("static/data/rent_cleaned.csv")
rent_df.to_sql("Rent", conn, if_exists='append', index=False)

 # Create both the Surfer and Board tables within the database
Base.metadata.create_all(conn)

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

if __name__ == "__main__":
    app.run(debug=True)