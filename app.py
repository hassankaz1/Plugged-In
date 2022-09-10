import os
import imp
import re
from types import MethodType
import requests
from API_KEYS import google_api, charge_key
from flask import Flask, redirect, render_template, request, flash, session, g, abort
from sqlalchemy import desc
from forms import SearchForm, UserAddForm, LoginForm
from models import db, connect_db, User, Review, CheckIn, Station
from sqlalchemy.exc import IntegrityError


CURR_USER_KEY = "curr_user"

app = Flask(__name__)

key = charge_key




app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///capstone'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()


url = "https://api.openchargemap.io/v3/poi"


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None
    
    g.google_api = google_api


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route("/")
def home_page():
    """Return Home Page"""

    return render_template("home.html")




@app.route('/signup', methods=["POST"])
def signup():
    """Handle user signup.
    Create new user and add to DB. Redirect to home page.
    If form not valid, present form.
    If the there already is a user with that username: flash message
    and re-present form.
    """

    username = request.form["username"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    password = request.form["password"]
    email = request.form["email"]
    image_url = request.form["image_url"]

    try:
        user = User.signup(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
            image_url=image_url or User.image_url.default.arg,
        )

        db.session.commit()

    except IntegrityError:
        flash("Username already taken", 'danger')
        return render_template('login-sign.html')

    do_login(user)

    return redirect("/")


@app.route('/login', methods=["POST"])
def login():
    """Handle user login."""

    username = request.form["username"]
    password = request.form["password"]

    user = User.authenticate(username, password)

    if user:
        print(user.id)
        do_login(user)
        flash(f"Hello, {user.username}!", "success")
        return redirect(f"/profile/{user.id}")

    flash("Invalid credentials.", 'danger')

    return render_template('login-sign.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()
    flash("LOGGED OUT", "success")
    return redirect("/")


@app.route("/search")
def search_charge():
    """Finds chargers and marks on map"""
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    max = request.args.get('max')
    port = request.args.get('port')

    r = requests.get(
        url,
        params={
            "key": key,
            "latitude": lat,
            "longitude": lng,
            "maxresults": max,
            "connectiontypeid": port
        })

    data = r.json()

    newList = []

    origin = {
        "lat": lat,
        "lng": lng,
        "address": "happy",
    }

    for i in data:
        charger = Station.query.get(i["ID"])

        if charger:
            print("hello")
        else:
            print(i["AddressInfo"]["ContactTelephone1"])
            line1 = i["AddressInfo"]["AddressLine1"] or ""
            town = i["AddressInfo"]["Town"] or ""
            state = i["AddressInfo"]["StateOrProvince"] or ""
            zip = i["AddressInfo"]["Postcode"] or ""

            address = f"{line1} {town}, {state} {zip}"

            lat = i["AddressInfo"]["Latitude"]
            lng = i["AddressInfo"]["Longitude"]
            address = address
            id = i["ID"]
            chargers_avail = i["Connections"][0]["Quantity"]
            connection_type = i["Connections"][0]["ConnectionType"]["ID"]
            supercharger = True if i["Connections"][0]["LevelID"] == 3 else False
            usage_cost = i["UsageCost"]
            telephone = i["AddressInfo"]["ContactTelephone1"]
            if telephone:
                telephone = telephone[:12]
            email = i["AddressInfo"]["ContactEmail"]
            level = i["Connections"][0]["LevelID"] 
            print("level----------", level) 

            charger = Station(
                id=id, lat=lat, lng=lng, address=address, chargers_avail=chargers_avail,
                connection_type=connection_type, supercharger=supercharger, usage_cost=usage_cost, telephone=telephone,
                email=email, level=level
            )

            db.session.add(charger)
            db.session.commit()

        newList.append(charger)

    review_list = []

    if g.user != None:
        for review in g.user.reviews:
            review_list.append(review.stations_reviewed.id)

    return render_template("map.html", origin=origin, data=newList, review_list=review_list, zoom=12)


@app.route("/search-charger", methods=["GET"])
def form():
    """Return page to search for charger"""


    return render_template('form.html')

@app.route("/formfor", methods=["POST"])
def form_validate():
    """Handle user searching for chargers.
    Redirect to search
    """

    lat = request.form['lat']
    lng = request.form['lng']
    port = request.form['port']
    max = request.form['max']


    return redirect(f"/search?lat={lat}&lng={lng}&port={port}&max={max}")




@app.route("/quick-search", methods=["POST"])
def form_quick_search():
    """Handle Quick Search.
    Take user current location and show search results
    """

    lat = request.form['latq']
    lng = request.form['lngq']
    max = 50


    return redirect(f"/search?lat={lat}&lng={lng}&max={max}")



@app.route("/review/<int:charger_id>", methods=["POST"])
def review(charger_id):
    """Handle form to review charging station"""
    rating = float(request.form["rating"])
    title = request.form["title"]
    description = request.form["description"]

    review = Review(
        user_id=g.user.id, rating=rating, station=charger_id, title=title, description=description
    )

    db.session.add(review)
    db.session.commit()


    return redirect(f"/profile/{g.user.id}")




@app.route("/profile/<int:user_id>")
def profile(user_id):
    user = User.query.get(user_id)
    return render_template("profile.html", user=user)


@app.route("/editreview/<int:review_id>", methods=["POST"])
def edit_review(review_id):
    review = Review.query.get(review_id)

    review.rating = float(request.form["rating"])
    review.title = request.form["title"]
    review.description = request.form["description"]

    db.session.commit()

    return redirect(f"/profile/{review.users_reviewed.id}")

@app.route("/edit-profile/<int:user_id>", methods=["POST"])
def edit_profile(user_id):
    user = User.query.get(user_id)
    if(user != g.user):
        flash("Not authorized to edit the profile")
        return redirect("/")


    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.last_name = request.form["last_name"]
    user.email = request.form["email"]
    user.image_url = request.form["picture"]
    user.cover_photo = request.form["cover_photo"]
    db.session.commit()

    return redirect(f"/profile/{user.id}")

@app.route("/viewmap/<int:user_id>")
def view_map(user_id):
    user = User.query.get(user_id)
    charger_list = []

    for review in user.reviews:
        charger = review.stations_reviewed
        charger_list.append(charger)


    origin = {
        "lat": 39.5,
        "lng": -98.35,
        "address": "happy",
    }


    review_list = []
    if g.user != None:
        for review in g.user.reviews:
            review_list.append(review.stations_reviewed.id)
    
    return render_template("map.html", origin=origin, data=charger_list, review_list=review_list, zoom=5)


@app.route("/login-sign")
def new_pro():
    return render_template("login-sign.html")
