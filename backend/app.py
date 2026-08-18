from flask import Flask, request
from flask_cors import CORS
from extension import db, jwt
from models import User, Course
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    jwt.init_app(app)

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

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)