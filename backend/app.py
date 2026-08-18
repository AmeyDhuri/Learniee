from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///learnee.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def home():
        return{"message": "Learniee API is running!!"}

    @app.route("/api/signup", methods=["POST"])
    def signup():
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return{"error": "All field are required"}, 400

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return{"error": "Email already registered!"}, 409

        hashed_password = generate_password_hash(password)

        user = User(name=name, email=email, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        return{"message": "Account created successfully!"}, 201

    with app.app_context():
        db.create_all()

    return app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    teacher = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)