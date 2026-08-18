from flask import Flask, request
from flask_cors import CORS
from extensions import db, jwt
from models import User, Course
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

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

    @app.route("/api/login", methods=["POST"])
    def login():
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return{"error": "Email and Password are required!"}, 400

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return{"error": "Invalid email or password"}, 401

        access_token = create_access_token(identity=str(user.id))

        return{"message": "Login successfully",
                "access_token" : access_token,
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email
                    }
               },200

    @app.route("/api/me", methods=["GET"])
    @jwt_required()
    def get_current_user():
        user_id = get_jwt_identity()

        user = User.query.get(user_id)

        if not user:
            return{"error": "User not found!"}, 404

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }, 200

    @app.route("/api/courses", methods=["GET"])
    def get_courses():
        search = request.args.get("search", "").strip()
        subject = request.args.get("subject")
        grade = request.args.get("grade")
        min_price = request.args.get("min_price")
        max_price = request.args.get("max_price")
        min_rating = request.args.get("min_rating")

        try:
            if grade is not None:
                grade = int(grade)

            if min_price is not None:
                min_price = float(min_price)

            if max_price is not None:
                max_price = float(max_price)

            if min_rating is not None:
                min_rating = float(min_rating)

        except ValueError:
            return {
                "error": "Invalid filter value. grade must be an integer and price/rating values must be numbers."
            }, 400

        sort = request.args.get("sort", "default")

        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 6, type=int)

        query = Course.query

        if search:
            query = query.filter(
                db.or_(
                    Course.name.ilike(f"%{search}%"),
                    Course.subject.ilike(f"%{search}%")
                )
            )

        if subject:
            query = query.filter(Course.subject == subject)

        if grade:
            query = query.filter(Course.grade == grade)

        if min_price is not None:
            query = query.filter(Course.price >= min_price)

        if max_price is not None:
            query = query.filter(Course.price <= max_price)

        if min_rating is not None:
            query = query.filter(Course.rating >= min_rating)


        if sort == "price_asc":
            query = query.order_by(Course.price.asc())

        elif sort == "price_desc":
            query = query.order_by(Course.price.desc())

        elif sort == "rating_desc":
            query = query.order_by(Course.rating.desc())


        pagination = query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        courses = [
            {
                "id": course.id,
                "name": course.name,
                "subject": course.subject,
                "grade": course.grade,
                "price": course.price,
                "teacher": course.teacher,
                "rating": course.rating
            }
            for course in pagination.items
        ]

        return {
            "courses": courses,
            "pagination": {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total": pagination.total,
                "pages": pagination.pages,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev
            }
        }, 200

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)