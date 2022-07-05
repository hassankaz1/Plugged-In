from datetime import datetime
from email.policy import default
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )
    
    first_name = db.Column(
        db.Text,
        nullable=False,
    )

    last_name = db.Column(
        db.Text,
        nullable=False,
    )

    bio = db.Column(
        db.Text,
    )

    image_url = db.Column(
        db.Text,
        default="https://t4.ftcdn.net/jpg/00/64/67/63/360_F_64676383_LdbmhiNM6Ypzb3FM4PPuFP9rHe7ri8Ju.jpg",
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    stations_visited = db.relationship('CheckIn', backref='users_visited')

    reviews = db.relationship('Review', backref='users_reviewed')

    @classmethod
    def signup(cls, username, first_name, last_name, email, password, image_url):
        """Sign up user.
        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_pwd,
            image_url=image_url,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.
        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.
        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


class Review(db.Model):
    """An individual review."""

    __tablename__ = 'reviews'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )

    station = db.Column(
        db.Integer,
        db.ForeignKey('stations.id', ondelete='CASCADE'),
        nullable=False,
    )

    rating=db.Column(
        db.Float,
        nullable=False
    )

    title= db.Column(
        db.String(50),
        nullable=False,
    )

    description = db.Column(
        db.String(250),
        nullable=False,
    )

    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )



class CheckIn(db.Model):
    """Association table for visited chargers among users"""

    __tablename__ = 'checkins'
    
    user_id = db.Column(
      db.Integer, 
      db.ForeignKey('users.id'), 
      primary_key = True)

    station_id = db.Column(
        db.Integer, 
        db.ForeignKey('stations.id'), 
        primary_key = True)


class Station(db.Model):

    __tablename__ = 'stations'
    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    lat = db.Column(
        db.Float,
        nullable=False,
    )

    lng = db.Column(
        db.Float,
        nullable=False,
    )

    connection_type = db.Column(
        db.Integer,
        nullable=False,
    )

    supercharger = db.Column(
        db.Boolean,
        default=False
    )

    address = db.Column(
        db.Text,
        nullable = False
    )

    level=db.Column(
        db.Integer,
    )

    usage_cost= db.Column(
        db.Text,
    )
    
    telephone = db.Column(
        db.String(15),
    )

    email=db.Column(
        db.String(20),
    )

    chargers_avail=db.Column(
        db.Integer,
    )

    users_visited = db.relationship("CheckIn", backref="stations_visited")

    reviews = db.relationship("Review", backref="stations_reviewed")



def connect_db(app):
    """Connect this database to provided Flask app.
    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)