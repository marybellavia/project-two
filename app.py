# import necessary libraries
from models import create_house, create_rent
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# flask setup
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Rent = create_rent(db)
House = create_house(db)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html", title="Rent & House Index Analysis")

@app.route("/about")
def about():
    # Return template and data
    return render_template("about.html", title="About")

# Route that will trigger the scrape function
@app.route("/models")
def models():

    # Redirect back to home page
    return render_template("models.html", title="Models")

@app.route("/maps")
def maps():

    # Redirect back to home page
    return render_template("maps.html", title="Maps")

if __name__ == "__main__":
    app.run(debug=True)